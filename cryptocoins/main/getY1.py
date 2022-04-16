import telebot
import openpyxl

BOT_TOKEN = '5397252848:AAHg9ZE9HLBflvI-uAUWGgDHFYVk46dr-ng'
CHANNEL_NAME = '@cryptocoinstest'
CHANNEL_ID = '-1001635996486'


def send_message():
    wb = openpyxl.load_workbook('result.xlsx', data_only=True)
    sheet = wb.active
    data = sheet['Y1'].value

    bot = telebot.TeleBot(BOT_TOKEN)
    if data != None:
        bot.send_message(chat_id=CHANNEL_ID, text=str(data))