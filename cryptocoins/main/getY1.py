import telebot
import openpyxl
import pandas as pd
import xlsxwriter

BOT_TOKEN = '5187298061:AAH8PJ0VRfbQkpiOmFUQ-1kroZqkCM4a24I'
CHANNEL_ID = '-1001261505666'


def send_message():
    wb = openpyxl.load_workbook('result.xlsx', data_only=True)
    sheet = wb.active
    wb.iso_dates = True
    data = sheet['Y1'].value

    print(f'[Y1 - {data}]')

    bot = telebot.TeleBot(BOT_TOKEN)
    if data != None:
        bot.send_message(chat_id=CHANNEL_ID, text='(TEST) '+str(data))
