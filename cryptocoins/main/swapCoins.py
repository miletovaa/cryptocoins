from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import subprocess
import time
import requests
from getY1 import send_message

private_key = 'wrap indicate hello ahead saddle news decrease arctic help deposit student fiscal between potato urge resource boss robot awake move arrange fitness wild work'
account_name = 'trade'
password = 'trade2022SR!'

driver_path = './chromedriver'
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
chrome_options.add_extension('Keplr 0.10.2.0.crx')


def login(driver):
    # Base login on Keplr
    link = 'chrome-extension://dmkamcknogkgcdfhhbddcghachkejeap/popup.html#/register'
    driver.get(link)
    driver.find_elements(by=By.TAG_NAME, value='button')[2].click()
    driver.find_elements(by=By.TAG_NAME, value='input')[0].send_keys(private_key)
    driver.find_elements(by=By.TAG_NAME, value='input')[1].send_keys(account_name)
    driver.find_elements(by=By.TAG_NAME, value='input')[2].send_keys(password)
    driver.find_elements(by=By.TAG_NAME, value='input')[3].send_keys(password)
    driver.find_elements(by=By.TAG_NAME, value='button')[1].click()
    time.sleep(3)


class SwapCoins:
    class JunoSwap:

        def swapCoins(self, main_coin, value, second_coin):
            try:
                # Configs
                path = driver_path
                driver = webdriver.Chrome(path, options=chrome_options)
                url = "https://junoswap.com/"

                login(driver=driver)

                driver.get(url)
                time.sleep(1)

                driver.find_element(by=By.CLASS_NAME, value='sc-bdvvtL').click()
                driver.find_elements(by=By.CLASS_NAME, value='c-frhyQ')[1].click()
                time.sleep(1)
                subprocess.Popen(['xdotool', 'key', 'ctrl+F4'])
                time.sleep(1)
                driver.find_elements(by=By.CLASS_NAME, value='c-frhyQ')[1].click()
                time.sleep(1)
                subprocess.Popen(['xdotool', 'key', '0xff09'])
                time.sleep(0.1)
                subprocess.Popen(['xdotool', 'key', '0xff09'])
                time.sleep(0.1)
                subprocess.Popen(['xdotool', 'key', 'Return'])

                time.sleep(1)

                # Open list to choose main coin
                driver.find_element(by=By.CLASS_NAME, value='c-fkNNfJ-cjOYsE-state-selected').click()
                main_coin_id = [el.text.split()[0].lower() for el in
                                driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')].index(main_coin)
                junoswap_list = [el.text.split()[0].lower() for el in
                                 driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')]

                second_coin_id = junoswap_list.index(second_coin)
                # Choose a main coin
                driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')[main_coin_id].click()

                # Button for choosing an addiction coins
                addCoinsButton = driver.find_elements(by=By.CLASS_NAME, value='c-gejiUb')[1]

                # Click button for choosing an addiction coin
                addCoinsButton.click()
                addCoins = driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')
                addCoins[second_coin_id].click()

                # Get main coin input
                mainCoinInput = driver.find_elements(by=By.CLASS_NAME, value='c-dwExUq')[0]
                mainCoinInput.send_keys(Keys.CONTROL + "a")
                mainCoinInput.send_keys(Keys.DELETE)
                mainCoinInput.send_keys(str(float(value)))

                time.sleep(0.5)
                swapButton = driver.find_elements(by=By.TAG_NAME, value='button')[7]
                swapButton.click()

                time.sleep(2)

                for i in range(8):
                    subprocess.Popen(['xdotool', 'key', '0xff09'])
                    time.sleep(0.1)
                subprocess.Popen(['xdotool', 'key', 'Return'])

                response_of_tr = f'(JunoSwap) Transaction was completed successfully! Main coin: {main_coin}, second coin: {second_coin}, value: {value}'
                send_message(response_of_tr)
            except Exception as e:
                response_of_tr = f'(JunoSwap) The transaction failed duo to an error! Error: {str(e)[:50]}'
                send_message(response_of_tr)

    class Sifchain:
        def swapCoins(self, main_coin, count, second_coin):
            try:
                # Configs
                path = driver_path
                driver = webdriver.Chrome(path, options=chrome_options)
                url = 'https://sifchain-dex.forbole.com/#/swap?from=uatom&to=rowan&slippage=1.0'

                login(driver=driver)

                driver.get(url)
                time.sleep(5)

                time.sleep(2)
                for i in range(15):
                    subprocess.Popen(['xdotool', 'key', '0xff09'])
                    time.sleep(0.1)
                    subprocess.Popen(['xdotool', 'key', '0xff09'])
                    time.sleep(0.1)
                    subprocess.Popen(['xdotool', 'key', 'Return'])
                    time.sleep(0.1)
                time.sleep(1)

                # Choosing the main coin
                driver.find_elements(by=By.TAG_NAME, value='button')[6].click()
                all_main_coins = [el.text.split('\n')[0].lower() for el in
                                  driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')]
                main_coin_id = all_main_coins.index(main_coin)
                driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')[main_coin_id].click()

                # Choosing the second coin
                driver.find_elements(by=By.TAG_NAME, value='button')[9].click()
                time.sleep(2)
                all_second_coins = [el.text.split('\n')[0].lower() for el in
                                    driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')]
                second_coin_id = all_second_coins.index(second_coin)
                # print(all_second_coins, second_coin_id)
                # time.sleep(1000000)
                driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')[second_coin_id].click()

                mainCoinInput = driver.find_elements(by=By.CLASS_NAME, value='token-input')[1]
                mainCoinInput.send_keys(Keys.CONTROL + 'a')
                mainCoinInput.send_keys(Keys.DELETE)
                mainCoinInput.send_keys(str(count))

                time.sleep(3)
                driver.find_elements(by=By.TAG_NAME, value='button')[17].click()
                time.sleep(2)
                driver.find_elements(by=By.TAG_NAME, value='button')[22].click()
                time.sleep(6)
                for i in range(12):
                    subprocess.Popen(['xdotool', 'key', '0xff09'])
                    time.sleep(0.1)
                subprocess.Popen(['xdotool', 'key', 'Return'])
                response_of_tr = f'(Sifchain) Transaction was completed successfully! Main coin: {main_coin}, second coin: {second_coin}, value: {count}'
                send_message(response_of_tr)
            except Exception as e:
                response_of_tr = f'(Sifchain) The transaction failed duo to an error! Error: {str(e)[:50]}'
                send_message(response_of_tr)

    class Osmosis:
        def swapCoins(self, main_coin, count, second_coin):
            try:
                # Configs
                path = driver_path
                driver = webdriver.Chrome(path, options=chrome_options)
                url = 'https://app.osmosis.zone/?from=ATOM&to=OSMO'

                login(driver=driver)

                driver.get(url)

                try:
                    driver.find_element(by=By.CLASS_NAME, value='mr-5').click()
                    driver.find_element(by=By.CLASS_NAME, value='px-8').click()
                except:
                    pass

                driver.find_elements(by=By.TAG_NAME, value='button')[8].click()
                driver.find_elements(by=By.TAG_NAME, value='button')[9].click()
                driver.refresh()

                time.sleep(2)

                subprocess.Popen(['xdotool', 'key', '0xff09'])
                time.sleep(0.1)
                subprocess.Popen(['xdotool', 'key', '0xff09'])
                time.sleep(0.1)
                subprocess.Popen(['xdotool', 'key', 'Return'])
                time.sleep(0.1)
                subprocess.Popen(['xdotool', 'key', 'Return'])
                time.sleep(0.1)

                if main_coin == 'osmo':
                    flip = driver.find_element(by=By.CLASS_NAME, value='css-1so39r0')
                    flip.click()

                if main_coin != 'atom':
                    driver.find_elements(by=By.CLASS_NAME, value='css-1de6nk0')[0].click()
                    time.sleep(2)
                    main_all_coins_names = [el.text.split('\n')[0].lower() for el in
                                            driver.find_elements(by=By.CLASS_NAME, value='ml-3')]
                    main_coin_id = main_all_coins_names.index(main_coin)
                    driver.find_elements(by=By.CLASS_NAME, value='ml-3')[main_coin_id].click()

                if second_coin != 'osmo':
                    driver.find_elements(by=By.CLASS_NAME, value='css-1de6nk0')[1].click()
                    time.sleep(2)
                    all_coins_names = [el.text.split('\n')[0].lower() for el in
                                       driver.find_elements(by=By.CLASS_NAME, value='ml-3')]
                    second_coin_id = all_coins_names.index(second_coin)
                    driver.find_elements(by=By.CLASS_NAME, value='ml-3')[1].click()

                main_coin_input = driver.find_elements(by=By.CLASS_NAME, value='css-1ui17as')[0]
                main_coin_input.send_keys(Keys.CONTROL + 'a')
                main_coin_input.send_keys(Keys.DELETE)
                main_coin_input.send_keys(str(count))

                driver.find_element(by=By.CLASS_NAME, value='css-1vfyg9u').click()

                time.sleep(3)

                subprocess.Popen(['xdotool', 'key', '0xff09'])
                time.sleep(0.1)
                subprocess.Popen(['xdotool', 'key', '0xff09'])
                time.sleep(0.1)
                subprocess.Popen(['xdotool', 'key', '0xff09'])
                time.sleep(0.1)
                subprocess.Popen(['xdotool', 'key', '0xff09'])
                time.sleep(0.1)
                subprocess.Popen(['xdotool', 'key', 'Return'])
                time.sleep(0.1)

                response_of_tr = f'(Osmosis) Transaction was completed successfully! Main coin: {main_coin}, second coin: {second_coin}, value: {count}'
                send_message(response_of_tr)
            except Exception as e:
                response_of_tr = f'(Osmosis) The transaction failed duo to an error! Error: {str(e)[:50]}'
                send_message(response_of_tr)

    class Crescent:
        def swapCoins(self, main_coin, value, second_coin):
            try:
                # Configs
                path = driver_path
                driver = webdriver.Chrome(path, options=chrome_options)
                url = 'https://app.crescent.network/'

                login(driver=driver)

                driver.get(url)
                time.sleep(1)

                driver.find_elements(by=By.CLASS_NAME, value='text-yellowCRE-200')[4].click()
                driver.find_elements(by=By.CLASS_NAME, value='text-whiteCRE')[3].click()

                # Click to view list of coins
                driver.find_elements(by=By.CLASS_NAME, value='text-blackCRE')[5].click()

                main_coin_el = \
                    [el for el in driver.find_elements(by=By.CLASS_NAME, value='sBOLD18') if
                     el.text.lower() == main_coin][
                        0]
                # Click to main coin element
                main_coin_el.click()

                # Click to view all list if addiction coins
                driver.find_elements(by=By.CLASS_NAME, value='text-whiteCRE')[1].click()
                time.sleep(0.1)
                add_coins_el = [el for el in driver.find_elements(by=By.CLASS_NAME, value='sBOLD18') if
                                el.text.lower() == second_coin]
                # Choose the first addiction coin
                add_coins_el[0].click()

                driver.find_elements(by=By.TAG_NAME, value='button')[7].click()
                time.sleep(.1)
                driver.find_elements(by=By.TAG_NAME, value='button')[10].click()

                time.sleep(1)

                subprocess.Popen(['xdotool', 'key', 'ctrl+F4'])
                time.sleep(1)

                driver.find_elements(by=By.TAG_NAME, value='button')[7].click()
                time.sleep(.1)
                driver.find_elements(by=By.TAG_NAME, value='button')[10].click()

                time.sleep(1)

                for i in range(3):
                    time.sleep(1)
                    subprocess.Popen(['xdotool', 'key', '0xff09'])
                    time.sleep(0.1)
                    subprocess.Popen(['xdotool', 'key', '0xff09'])
                    time.sleep(0.1)
                    subprocess.Popen(['xdotool', 'key', 'Return'])
                    time.sleep(0.1)

                main_coin_input = driver.find_elements(by=By.TAG_NAME, value='input')[0]
                main_coin_input.send_keys(Keys.CONTROL + 'a')
                main_coin_input.send_keys(Keys.DELETE)
                main_coin_input.send_keys(str(value))
                time.sleep(6)

                # print(driver.find_elements(by=By.TAG_NAME, value='button')[8].text)
                driver.find_elements(by=By.TAG_NAME, value='button')[8].click()

                time.sleep(2)

                for i in range(7):
                    subprocess.Popen(['xdotool', 'key', '0xff09'])
                    time.sleep(0.1)
                subprocess.Popen(['xdotool', 'key', 'Return'])
                time.sleep(0.1)

                time.sleep(6)

                response_of_tr = '(Crescent) ' + driver.find_elements(by=By.CLASS_NAME, value='text-sm')[11].text + f' Main coin: {main_coin}, second coin: {second_coin}, value: {value}'
                send_message(response_of_tr)
            except Exception as e:
                response_of_tr = f'(Crescent) The transaction failed duo to an error! Error: {str(e)[:50]}'
                send_message(response_of_tr)


# # Junoswap (Done)
# junoswap = SwapCoins.JunoSwap()
# print(junoswap.swapCoins('juno', 0.0001, 'atom'))

# # Sifchain (Done)
# sifchain = SwapCoins.Sifchain()
# sifchain.swapCoins('rowan', 0.001, 'atom')

# # Osmosis (Done)
# osmosis = SwapCoins.Osmosis()
# osmosis.swapCoins('osmo', 0.001, 'atom')

# # Crescent
# crescent = SwapCoins.Crescent()
# response = crescent.swapCoins('ust', 0.1, 'atom')
# print(f'Crescent: {response}')
