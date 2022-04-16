import telebot
import openpyxl

BOT_TOKEN = '5187298061:AAH8PJ0VRfbQkpiOmFUQ-1kroZqkCM4a24I'
CHANNEL_ID = '-1001261505666'


def send_message():
    wb = openpyxl.load_workbook('result.xlsx', data_only=True)
    sheet = wb.active
    data = sheet['Y1'].value

    bot = telebot.TeleBot(BOT_TOKEN)
    if data != None:
        bot.send_message(chat_id=CHANNEL_ID, text=str(data))