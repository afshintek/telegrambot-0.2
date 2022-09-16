import constens as keys
from telegram.ext import *
import responses as kir

print("bot started...")

def start_command(update, context):
    update.message.reply_text('lets get started')


def help_command(update, context):
    update.message.reply_text('if you need help go fuck your self')

def userm_command(update, context):
    text = str(update.message.text).lower()
    responses = kir.jav(text)

    update.message.reply_text(responses)
def error(update, context):
    print(f"update {update} cased eror {context.error}")

def main():
    updater = Updater(keys.api_key, use_context= True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("start",help_command))

    dp.add_handler(MessageHandler(Filters.text, userm_command))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
main()



