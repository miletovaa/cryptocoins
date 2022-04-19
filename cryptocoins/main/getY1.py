import openpyxl
import requests

BOT_TOKEN = '5187298061:AAH8PJ0VRfbQkpiOmFUQ-1kroZqkCM4a24I'
CHANNEL_ID = '-1001261505666'


def send_message():
    wb = openpyxl.load_workbook('result.xlsx', data_only=True)
    sheet = wb.active
    wb.iso_dates = True
    data = sheet['Y1'].value

    print(f'[Y1 - {data}]')

    if data is not None:
        requests.get(
            f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&text=(TEST) {str(data)}')


requests.get(
    f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&text={"The service is stopped for a while"}')
