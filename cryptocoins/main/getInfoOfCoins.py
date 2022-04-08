from selenium import webdriver
import datetime, time


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
                        'p')[1]
                    list_of_coins.append([i, el.text.lower()])
                except Exception as e:
                    continue

            print(datetime.datetime.now() - start)

            return list_of_coins

        def get_prices(main_coin_id, values, addCoins):

            path = './chromedriver'
            driver = webdriver.Chrome(path)
            url = "https://junoswap.com/"
            driver.get(url)

            button = driver.find_element_by_class_name('c-fkNNfJ')
            button.click()

            all_coins = driver.find_elements_by_class_name('c-frhyQ')

            main_coin = all_coins[main_coin_id]

            print(main_coin.find_element_by_tag_name('div').find_element_by_tag_name('div').find_elements_by_tag_name(
                        'p')[1].text)

            main_coin.click()
            time.sleep(5)

            # inputs = driver.find_elements_by_class_name('c-dwExUq')
            # input = inputs[0]
            # info_input = inputs[1]
            # input.send_keys('80')
            # print('\nInput: ' + str(input.get_property('value')))
            # print('\nValue:' + str(info_input.get_property('value')))
            driver.close()


# print(getInfo.JunoSwap.get_all_coins())

getInfo.JunoSwap.get_prices(3, [],[])
