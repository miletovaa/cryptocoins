import requests

BOT_TOKEN = '5187298061:AAH8PJ0VRfbQkpiOmFUQ-1kroZqkCM4a24I'
CHANNEL_ID = '-1001261505666'


def send_message(data):
    requests.get(
        f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&text={str(data)}')
