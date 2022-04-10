from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime, time

coin_list = ['juno', 'atom', 'ust', 'btsg', 'luna', 'osmo', 'stars', 'huahua', 'akt', 'xprt', 'cmdx', 'dig', 'scrt',
             'neta', 'canlab', 'tuck', 'hulc', 'bcna', 'hope', 'rac', 'marble', 'coin', 'primo', 'daisy', 'future',
             'bfot', 'phmn', 'arto']


class getInfo:
    class JunoSwap:
        def get_all_coins():
            start = datetime.datetime.now()

            path = './chromedriver'
            driver = webdriver.Chrome(path)
            url = "https://junoswap.com/"
            driver.get(url)

            button = driver.find_element_by_class_name('c-fkNNfJ')
            button.click()

            all_coins = driver.find_elements_by_class_name('c-frhyQ')
            i = 0
            list_of_coins = []
            for coin in all_coins:
                try:
                    i += 1
                    el = coin.find_element_by_tag_name('div').find_element_by_tag_name('div').find_elements_by_tag_name(
                        'p')[0]
                    list_of_coins.append(el.text.lower())
                except Exception as e:
                    continue

            delay = datetime.datetime.now() - start
            print(f'\nDelay: {delay.seconds}.{delay.microseconds}\n')

            return list_of_coins

        ###################################################################
        def get_prices(main_coin_id, values, add_coins):
            try:
                # Start time
                start_main = datetime.datetime.now()

                # Prices of coins (response)
                prices = []

                # Configs
                path = './chromedriver'
                driver = webdriver.Chrome(path)
                url = "https://junoswap.com/"
                driver.get(url)

                # Open list to choose main coin
                driver.find_element(by=By.CLASS_NAME, value='c-fkNNfJ-cjOYsE-state-selected').click()

                # Get list of all coins ???????????????????????????????
                all_coins = driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')

                # Choose a main coin
                driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')[main_coin_id].click()

                # Get main coin input
                mainCoinInput = driver.find_elements(by=By.CLASS_NAME, value='c-dwExUq')[0]

                for el2 in add_coins:
                    if main_coin_id != el2:
                        # Button for choosing an addiction coins
                        addCoinsButton = driver.find_elements(by=By.CLASS_NAME, value='c-gejiUb')[1]

                        # Click button for choosing an addiction coin
                        addCoinsButton.click()
                        addCoins = driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')
                        addCoins[el2].click()
                        # time.sleep(2)
                        prices_of_coin = []
                        for el in values:
                            start = datetime.datetime.now()
                            mainCoinInput.send_keys(Keys.CONTROL + "a")
                            mainCoinInput.send_keys(Keys.DELETE)
                            mainCoinInput.send_keys(str(el))

                            coin_name = coin_list[el2]
                            input_value = mainCoinInput.get_property('value')
                            time.sleep(0.3)
                            response_value = driver.find_elements(by=By.CLASS_NAME, value='c-dwExUq')[1].get_property(
                                'value')
                            flip = driver.find_element(by=By.CLASS_NAME, value='c-PJLV')
                            flip.click()
                            time.sleep(0.4)

                            flipped_value = driver.find_elements(by=By.CLASS_NAME, value='c-dwExUq')[1].get_property(
                                'value')
                            flip.click()

                            print(
                                f'[{(datetime.datetime.now() - start).seconds}.{(datetime.datetime.now() - start).microseconds} sec]')
                            prices_of_coin.append([coin_name, input_value, response_value, flipped_value])
                        prices.append(prices_of_coin)
                    else:
                        continue

                driver.close()
                delay_main = datetime.datetime.now() - start_main
                print(delay_main)
                return prices
            except Exception as e:
                print(str(e))
                time.sleep(100000)


print(getInfo.JunoSwap.get_prices(0, [80, 100], range(0, 20)))
