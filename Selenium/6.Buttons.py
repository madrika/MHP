from telegram.ext import Updater , CommandHandler , MessageHandler , Filters
from telegram import ReplyKeyboardMarkup


token = Updater('1863100350:AAFG0pG-P86ZDv9BE7lCd1sNa4rnxHnNTU4' , use_context=True)

def start(update , context):
    key = [['وبسایت Madrika'] , ['کانال Madrika' , 'اینستاگرام Madrika']]
    key_2 = ReplyKeyboardMarkup(key)
    context.bot.send_message(chat_id= update.message.chat_id , text='سلام به ربات Madrika خوش اومدید.' , reply_markup=key_2)
def techone24_info(update , context):
    if update.message.text == 'وبسایت Madrika':
        context.bot.send_message(chat_id= update.message.chat_id , text= 'https://Madrika.com')
    elif update.message.text == 'کانال Madrika':
        context.bot.send_message(chat_id= update.message.chat_id , text= '@Madrika')
    elif update.message.text == 'اینستاگرام Madrika':
        context.bot.send_message(chat_id= update.message.chat_id , text = 'https://www.instagram.com/Madrika/')


token.dispatcher.add_handler(CommandHandler('start' , start))
token.dispatcher.add_handler(MessageHandler(Filters.text , techone24_info))

token.start_polling()
token.idle()