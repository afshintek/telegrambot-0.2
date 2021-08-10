import socket
import sys
from _thread import *
def main():
    global listen_port, buffer_size, max_conn
    try:
        listen_port = int (input("enter a listening port: "))
    except KeyboardInterrupt :
        sys.exit(0)

    max_conn = 5
    buffer_size = 8192

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('',listen_port))
        s.listen(max_conn)
        print("[*] initalizing socket... done. ")
        print("[*] socket binded successfully...")
        print("[*] server started successfully[{}]".format(listen_port))
    except Exception as e :
        print(e)
        sys.exit(2)
    while True:
        try:
            conn, addr = s.accept()
            data = conn.recv(buffer_size)
            start_new_thread(conn_string, (conn, data , addr))

        except KeyboardInterrupt:
            s.close()
            print("\n [*] shutting down...")
            sys.exit(1)
    s.close

def conn_string(conn, data, addr):
    try:
        fist_line = data.split("\n")[0]
        url = fist_line.split(" ")[1]

        http_pos = url.find ("://")
        if http_pos == -1:
            temp = url
        else:
            temp = url[(http_pos +3):]

        port_pos = temp.find(":")

        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)
        webserver = ""
        port = -1

        if port_pos == -1 or webserver_pos < port_pos:
            port = 80
            webserver = temp[:webserver_pos]
        else:
            port = int(temp[(port_pos+1):][:webserver_pos - port_pos - 1])
            webserver = temp[:port_pos]

        print(webserver)
        proxy_server(webserver, port, conn, data, addr)
    except Exception as e:
        print(e)

def proxy_server(webserver, port, conn, data, addr ):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, port))
        s.send(data)

        while True:
            reply = s.recv(buffer_size)

            if len(reply) > 0:
                conn.send(reply)

                dar = float(len(reply))
                dar = float(dar / 1024)
                dar = "{}.3s".format(dar)
                print("[*] requset done: {} => {} <= {}".format(addr[0], dar, webserver))
            else:
                break
        s.close()
        conn.close()
    except socket.error, (value, msg):
        s.close()
        conn.close
        sys.exit(1)

if __name__ == "__main__":
    main()
