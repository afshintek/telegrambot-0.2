from datetime import datetime

def jav(text):
    user_m = str(text).lower()

    if user_m in ("hello","hi"):
        return "hey! welcome to my bot"

    if user_m in ("how you doing?","whats up?"):
        return "thanks \n how you doing?"

    if user_m in ("time","time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    return "i dont understand what youre saying"
print("xx")