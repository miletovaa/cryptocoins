import telegram_send
import openpyxl


def send_message():
    wb = openpyxl.load_workbook('result.xlsx', data_only=True)
    sheet = wb.active
    data = sheet['Y1'].value
    if data != None:
        telegram_send.send(messages=[str(data)])
