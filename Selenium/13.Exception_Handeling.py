from telegram.ext import Updater, CommandHandler
from telegram.error import BadRequest
import logging

token = Updater('1863100350:AAFG0pG-P86ZDv9BE7lCd1sNa4rnxHnNTU4', use_context=True)


logging.basicConfig(filename='mylog.txt',format = '%(asctime)s - %(name)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(update.message.chat_id, 'a' * 4097)
    print("SALAM")


def Bad_Request(update, context, error):
    print("Hi")
    try:
        raise error
    except BadRequest:
        print("Bad Request")
        context.bot.send_message(update.message.chat_id, "Bad Request")
        logging.getLogger().info("Bad Request")


token.dispatcher.add_handler(CommandHandler('start', start))
token.dispatcher.add_error_handler(Bad_Request)

token.start_polling()
token.idle()
