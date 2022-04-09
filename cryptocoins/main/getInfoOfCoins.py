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
        def get_prices(self, main_coin_id, values, add_coins):

            start_main = datetime.datetime.now()

            prices = []

            path = './chromedriver'
            driver = webdriver.Chrome(path)
            url = "https://junoswap.com/"
            driver.get(url)

            mainCoinInput = driver.find_element(by=By.CLASS_NAME, value='c-fkNNfJ')
            all_coins = driver.find_elements(by=By.CLASS_NAME, value='c-frhyQ')
            main_coin = all_coins[main_coin_id]

            inputs = driver.find_elements(by=By.CLASS_NAME, value='c-dwExUq')
            mainCoinInput = inputs[0]
            info_input = inputs[1]
            mainCoinInput.send_keys(u'\ue009' + u'\ue003')

            ################
            mainCoinInput.click()
            main_coin.click()

            addCoins = driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')

            addCoins[1].click()

            ################
            for el2 in add_coins:
                # Click button for choosing an addiction coins
                addCoinsButton = driver.find_elements(by=By.CLASS_NAME, value='xeLnj')
                addCoinsButton[1].click()
                # print(addCoins[main_coin_id+2])
                addCoins = driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')
                addCoins[el2].click()
                price_of_coin = []
                for el in values:
                    start = datetime.datetime.now()
                    mainCoinInput.send_keys(Keys.CONTROL + "a")
                    mainCoinInput.send_keys(Keys.DELETE)
                    mainCoinInput.send_keys(str(el))

                    coin_name = coin_list[el2]
                    input_value = mainCoinInput.get_property('value')
                    time.sleep(0.35)
                    response_value = driver.find_elements(by=By.CLASS_NAME, value='c-dwExUq')[1].get_property('value')

                    flip = driver.find_element(by=By.CLASS_NAME, value='jBRuXC')
                    flip.click()
                    time.sleep(0.35)

                    flipped_value = driver.find_elements(by=By.CLASS_NAME, value='c-dwExUq')[1].get_property('value')
                    flip.click()

                    print(
                        f'[{(datetime.datetime.now() - start).seconds}.{(datetime.datetime.now() - start).microseconds} sec]')
                    price_of_coin.append([coin_name, input_value, response_value, flipped_value])
                prices.append(price_of_coin)

            driver.close()
            delay_main = datetime.datetime.now() - start_main
            return prices
            print(delay_main)


print(getInfo.JunoSwap.get_prices(self=None, main_coin_id=3, values=[80, 100],
                            add_coins=range(1,10)))

# print(getInfo.JunoSwap.get_all_coins())
