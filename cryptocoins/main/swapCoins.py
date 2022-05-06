from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import subprocess
import time
from send_message import send_message

private_key = 'wrap indicate hello ahead saddle news decrease arctic help deposit student fiscal between potato urge resource boss robot awake move arrange fitness wild work'
account_name = 'trade'
password = 'trade2022SR!'

driver_path = './chromedriver'
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
chrome_options.add_extension('Keplr 0.10.2.0.crx')

def get_name_of_coin(s):
    i = 1
    if '.' not in s:
        return s[:-1]
    for el in s[1:]:
        if el in '0123456789.':
            return s[:i]
        else:
            i+=1


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
        def countCoins(self, driver):
            driver.get('https://junoswap.com/transfer')
            time.sleep(1.5)
            coins = [el.text for el in driver.find_elements(by=By.CLASS_NAME, value='c-dOfGRD-fyTCeL-variant-primary')][
                    1:]
            coins = coins[:coins.index('Other tokens')]
            coins = [[el.split(' ')[1].lower(), float(el.split(' ')[0])] for el in coins]
            return coins

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

                window_before = driver.window_handles[0]
                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)
                driver.close()
                driver.switch_to.window(window_before)
                driver.find_elements(by=By.CLASS_NAME, value='c-frhyQ')[1].click()
                time.sleep(1)

                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)

                while True:
                    try:
                        driver.find_elements(by=By.TAG_NAME, value='button')[-1].click()
                    except:
                        break

                driver.switch_to.window(window_before)

                time.sleep(1)

                coins_count = self.countCoins(driver)
                print(coins_count)
                driver.get(url)
                time.sleep(2)

                # Open list to choose main coin
                driver.find_element(by=By.CLASS_NAME, value='c-fkNNfJ-cjOYsE-state-selected').click()
                main_coin_id = [el.text.split()[0].lower() for el in
                                driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')].index(main_coin)
                junoswap_list = [el.text.split()[0].lower() for el in
                                 driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')]

                second_coin_id = junoswap_list.index(second_coin)
                # Choose a main coin
                driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')[main_coin_id].click()

                time.sleep(0.3)

                # Button for choosing an addiction coins
                addCoinsButton = driver.find_elements(by=By.CLASS_NAME, value='c-frhyQ')[5]

                # Click button for choosing an addiction coin
                addCoinsButton.click()
                addCoins = driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')
                addCoins[second_coin_id].click()

                # Get main coin input
                mainCoinInput = driver.find_elements(by=By.CLASS_NAME, value='c-dwExUq')[0]
                mainCoinInput.send_keys(Keys.CONTROL + "a")
                mainCoinInput.send_keys(Keys.DELETE)
                mainCoinInput.send_keys(str(float(value)))

                time.sleep(2)
                # time.sleep(10000000)
                swapButton = driver.find_elements(by=By.TAG_NAME, value='button')[5]
                swapButton.click()

                time.sleep(3)

                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)
                while True:
                    try:
                        driver.find_elements(by=By.TAG_NAME, value='button')[-1].click()
                    except:
                        break

                driver.switch_to.window(window_before)

                response_of_tr = f'(JunoSwap) Transaction was completed successfully! Main coin: {main_coin}, second coin: {second_coin}, value: {value}'
                time.sleep(8)
                coins_count2 = self.countCoins(driver)
                print(coins_count2)

                main_coin_count_before = coins_count[[el[0] for el in coins_count].index(main_coin)][1]
                second_coin_count_before = coins_count[[el[0] for el in coins_count].index(second_coin)][1]
                main_coin_count_after = coins_count2[[el[0] for el in coins_count2].index(main_coin)][1]
                second_coin_count_after = coins_count2[[el[0] for el in coins_count2].index(second_coin)][1]
                if main_coin_count_before == main_coin_count_after or second_coin_count_before == second_coin_count_after:
                    response_of_tr = '(JunoSwap) The transaction failed!'
                    send_message(response_of_tr)
                    self.swapCoins(main_coin, value, second_coin)
                else:
                    send_message(response_of_tr)
            except Exception as e:
                response_of_tr = f'(JunoSwap) The transaction failed duo to an error! Error: {str(e)}'
                send_message(response_of_tr)
                self.swapCoins(main_coin, value, second_coin)

    class Sifchain:
        def countCoins(self, driver):
            driver.get('https://sifchain-dex.redstarling.com/#/balances')
            window_after = driver.window_handles[0]
            try:
                window_before = driver.window_handles[1]
                driver.switch_to.window(window_before)
            except:
                pass
            time.sleep(1)

            while True:
                try:
                    driver.find_elements(by=By.TAG_NAME, value='button')[1].click()
                except:
                    break
            driver.switch_to.window(window_after)
            time.sleep(10)
            return [[el.text.split('\n')[0].lower(), float(el.text.split('\n')[1])] for el in
                    driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')]

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
                window_after = driver.window_handles[0]
                try:
                    window_before = driver.window_handles[1]
                    driver.switch_to.window(window_before)
                except:
                    pass
                time.sleep(1)

                while True:
                    try:
                        driver.find_elements(by=By.TAG_NAME, value='button')[1].click()
                    except:
                        break
                driver.switch_to.window(window_after)
                count_before = self.countCoins(driver)

                main_coin_count_before = count_before[[el[0] for el in count_before].index(main_coin)][1]
                second_coin_count_before = count_before[[el[0] for el in count_before].index(second_coin)][1]

                driver.get(url)
                time.sleep(3)

                # Choosing the main coin
                driver.find_elements(by=By.TAG_NAME, value='button')[6].click()
                driver.find_element(by=By.ID, value='token-search').send_keys(str(main_coin))
                # all_main_coins = [el.text.split('\n')[0].lower() for el in
                                #   driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')]
                # main_coin_id = all_main_coins.index(main_coin)
                time.sleep(1)
                driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')[0].click()

                # Choosing the second coin
                driver.find_elements(by=By.TAG_NAME, value='button')[9].click()
                time.sleep(2)
                # all_second_coins = [get_name_of_coin(el.get_attribute('textContent').lower()) for el in
                #                     driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')]
                # print(all_second_coins)
                # second_coin_id = all_second_coins.index(second_coin)
                # print(all_second_coins, second_coin_id)
                # time.sleep(1000000)
                driver.find_element(by=By.ID, value='token-search').send_keys(str(second_coin))
                time.sleep(1)
                # print(len(driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')))
                # time.sleep(1000000)
                driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')[0].click()

                mainCoinInput = driver.find_elements(by=By.CLASS_NAME, value='token-input')[1]
                mainCoinInput.send_keys(Keys.CONTROL + 'a')
                mainCoinInput.send_keys(Keys.DELETE)
                mainCoinInput.send_keys(str(count))

                
                time.sleep(6)
                driver.find_elements(by=By.TAG_NAME, value='button')[17].click()
                time.sleep(6)
                driver.find_elements(by=By.TAG_NAME, value='button')[22].click()
                time.sleep(13)

                window_after = driver.window_handles[0]
                try:
                    window_before = driver.window_handles[1]
                    driver.switch_to.window(window_before)
                except:
                    pass
                time.sleep(1)

                while True:
                    try:
                        driver.find_elements(by=By.TAG_NAME, value='button')[-1].click()
                    except:
                        break
                driver.switch_to.window(window_after)

                time.sleep(20)

                response_of_tr = f'(Sifchain) Transaction was completed successfully! Main coin: {main_coin}, second coin: {second_coin}, value: {count}'
                count_after = self.countCoins(driver)

                main_coin_count_after = count_after[[el[0] for el in count_after].index(main_coin)][1]
                second_coin_count_after = count_after[[el[0] for el in count_after].index(second_coin)][1]

                print(main_coin_count_before, main_coin_count_after)
                print(second_coin_count_before, second_coin_count_after)

                if main_coin_count_before == main_coin_count_after or second_coin_count_before == second_coin_count_after:
                    response_of_tr = f'(Sifchain) The transaction failed!'
                    send_message(response_of_tr)
                    self.swapCoins(main_coin, count, second_coin)
                else:
                    send_message(response_of_tr)
            except Exception as e:
                response_of_tr = f'(Sifchain) The transaction failed duo to an error! Error: {str(e)[:150]}'
                send_message(response_of_tr)
                self.swapCoins(main_coin, count, second_coin)

    class Osmosis:
        def countCoins(self, driver):
            driver.get('https://app.osmosis.zone/assets')
            time.sleep(2)
            # print([[el.text.split('\n')[0].lower(), el.text.split('\n')[1]] for el in driver.find_elements(by=By.CLASS_NAME, value='css-1lfky4b')])
            lst = [el.text for el in driver.find_elements(by=By.CLASS_NAME, value='css-pq4qi6')]
            return [[lst[lst.index(el) - 1].split(' ')[-1].lower(), float(el)] for el in lst[1::2] if el != '0']

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
                window_after = driver.window_handles[0]
                try:
                    window_before = driver.window_handles[1]
                    driver.switch_to.window(window_before)
                except:
                    pass
                time.sleep(1)

                while True:
                    try:
                        driver.find_elements(by=By.TAG_NAME, value='button')[-1].click()
                    except:
                        break
                driver.switch_to.window(window_after)

                count_before = self.countCoins(driver)
                driver.get(url)

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
                    driver.find_elements(by=By.CLASS_NAME, value='ml-3')[second_coin_id].click()

                main_coin_input = driver.find_elements(by=By.CLASS_NAME, value='css-1ui17as')[0]
                main_coin_input.send_keys(Keys.CONTROL + 'a')
                main_coin_input.send_keys(Keys.DELETE)
                main_coin_input.send_keys(str(count))
                time.sleep(1)

                driver.find_element(by=By.CLASS_NAME, value='css-1vfyg9u').click()

                time.sleep(3)

                window_after = driver.window_handles[0]
                try:
                    window_before = driver.window_handles[1]
                    driver.switch_to.window(window_before)
                except:
                    pass
                time.sleep(1)

                while True:
                    try:
                        driver.find_elements(by=By.TAG_NAME, value='button')[-1].click()
                    except:
                        break
                driver.switch_to.window(window_after)

                time.sleep(8)

                response_of_tr = f'(Osmosis) Transaction was completed successfully! Main coin: {main_coin}, second coin: {second_coin}, value: {count}'
                count_after = self.countCoins(driver)
                main_coin_count_before = count_before[[el[0] for el in count_before].index(main_coin)][1]
                main_coin_count_after = count_after[[el[0] for el in count_after].index(main_coin)][1]
                second_coin_count_before = count_before[[el[0] for el in count_before].index(second_coin)][1]
                second_coin_count_after = count_after[[el[0] for el in count_after].index(second_coin)][1]
                if main_coin_count_before == main_coin_count_after or second_coin_count_before == second_coin_count_after:
                    response_of_tr = f'(Osmosis) The transaction failed!'
                    send_message(response_of_tr)
                    self.swapCoins(main_coin, count, second_coin)
                else:
                    send_message(response_of_tr)
            except Exception as e:
                response_of_tr = f'(Osmosis) The transaction failed duo to an error! Error: {str(e)[:150]}'
                send_message(response_of_tr)
                self.swapCoins(main_coin, count, second_coin)

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

                response_of_tr = '(Crescent) ' + driver.find_elements(by=By.CLASS_NAME, value='text-sm')[
                    11].text + f' Main coin: {main_coin}, second coin: {second_coin}, value: {value}'
                send_message(response_of_tr)
            except Exception as e:
                response_of_tr = f'(Crescent) The transaction failed duo to an error! Error: {str(e)[:150]}'
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
