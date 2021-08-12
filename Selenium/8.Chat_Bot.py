# -*- coding:utf-8 -*-
from telegram.ext import Updater , CommandHandler , MessageHandler , Filters , CallbackQueryHandler
from telegram import InlineKeyboardButton , InlineKeyboardMarkup

token = Updater('1863100350:AAFG0pG-P86ZDv9BE7lCd1sNa4rnxHnNTU4' , use_context= True)

se = 0
re = 0
B = []

def start(update , context):
    contact_key = [[InlineKeyboardButton('📞ارتباط با ما' , callback_data='1')]]
    contact_key2 = InlineKeyboardMarkup(contact_key)
    if update.message.from_user.username != None:
        if update.message.chat_id != 696616087:
            context.bot.send_message(chat_id = update.message.chat_id , text = ' 👋🏻سلام {}  به ربات Madrika خوش اومدی'.format(update.message.from_user.first_name) , reply_markup=contact_key2)
            context.bot.send_message(chat_id = update.message.chat_id , text= 'برای راهنمایی بیشتر از دستور /help استفاده کنید.')
        else :
            context.bot.send_message(chat_id = 696616087 ,text = 'سلام ، شما ادمین هستید.' )
    else :
        context.bot.send_message(chat_id = update.message.chat_id , text= 'با عرض پوزش برای استفاده از این ربات شما نیاز به یک یوزرنیم تلگرامی دارید. در صورت انتخاب یوزر نیم مجددا /start  بزنید.')

def send (update , context):
    global se , re , sender , B
    key = [[InlineKeyboardButton('پاسخ' , callback_data='2') , InlineKeyboardButton('بلاک کردن ❌' , callback_data='3')] , [InlineKeyboardButton('آنبلاک کردن ✅' , callback_data='4')]]
    key_2 = InlineKeyboardMarkup(key)
    if se != 0 :
        if update.message.chat_id not in B :
            context.bot.send_message(chat_id = 87085659 , text= update.message.text , reply_markup= key_2)
            context.bot.send_message(chat_id = 87085659, text= 'این پیام از طرف https://t.me/{} میباشد.'.format(update.message.from_user.username))
            context.bot.send_message(chat_id = update.message.chat_id , text='پیام شما ارسال گردید.')
            sender = update.message.chat_id
            se = 0
        else :
            context.bot.send_message(chat_id = update.message.chat_id , text='شما بلاک شده اید.')
    if re != 0 :
        context.bot.send_message(chat_id = sender , text='پاسخ ادمین به شما : \n {}'.format(update.message.text))
        context.bot.send_message(chat_id = 87085659 , text='پاسختان ارسال شد.')
        re = 0

def contact_buttons(update , context):
    global se , re , B , sender
    query = update.callback_query
    if query.data == '1':
        se = 1
        context.bot.send_message(chat_id = query.message.chat_id , text='پیام خود را وارد نمایید.')
    if query.data == '2':
        context.bot.send_message(chat_id = 87085659 , text= 'پاسخ خود را وارد نمایید.')
        re = 1
    if query.data == '3':
        B.append(sender)
        context.bot.send_message(chat_id = 87085659 , text='کاربر مورد نظظر با چت ایدی {} بلاک شد'.format(sender))
    if query.data == '4':
        if sender in B :
            B.remove(sender)
            context.bot.send_message(chat_id = 87085659 , text= 'کاربر مورد نظر با چت آیدی {} آنبلاک شد'.format(sender))
        else :
            context.bot.send_message(chat_id = 87085659 , text= 'کاربر مورد نظر بلاک نبوده است.')
def help1(update , context):
    context.bot.send_message(chat_id = update.message.chat_id , text= 'برای ارتباط با ادمین /start بزنید و از دکمه ی ارتباط با ما استفاده نمایید. \n  برای دریافت ادرس وبسایت و چنل Madrika روی دستور /info کلیک نمایید.')

def info(update , context):
    button_1 = [[InlineKeyboardButton('وبسایت  Madrika' , callback_data='5' , url='https://Madrika.com')] , [InlineKeyboardButton('چنل  Madrika' , callback_data='6' , url='https://t.me/Madrika')]]
    button_2 = InlineKeyboardMarkup(button_1)
    context.bot.send_message(chat_id = update.message.chat_id , text= 'انتخاب نمایید.'  , reply_markup = button_2)


token.dispatcher.add_handler(CommandHandler('start' , start))
token.dispatcher.add_handler(CommandHandler('help' , help1))
token.dispatcher.add_handler(CommandHandler('info' , info))
token.dispatcher.add_handler(MessageHandler(Filters.text , send))
token.dispatcher.add_handler(CallbackQueryHandler(contact_buttons))


token.start_polling()
token.idle()