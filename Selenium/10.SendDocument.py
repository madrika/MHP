from telegram.ext import Updater , CommandHandler

token = Updater('1863100350:AAFG0pG-P86ZDv9BE7lCd1sNa4rnxHnNTU4' , use_context= True)

def start(update,context):
    context.bot.send_message(text='سلام به ربات Madrika خوش اومدی . \n برای اطلاعات بیشتر روی دستور /help   کلیک نمایید',chat_id=update.message.chat_id)


def send_document(update,context):
    chat_id = update.message.chat_id
    document = open('python.pdf','rb')
    context.bot.sendDocument(chat_id,document)

token.dispatcher.add_handler(CommandHandler('start',start))
token.dispatcher.add_handler(CommandHandler('document',send_document))

token.start_polling()
token.idle()

