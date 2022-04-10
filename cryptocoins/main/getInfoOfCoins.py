from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime, time

junoswap_list = ['juno', 'atom', 'ust', 'btsg', 'luna', 'osmo', 'stars', 'huahua', 'akt', 'xprt', 'cmdx', 'dig', 'scrt',
                 'neta', 'canlab', 'tuck', 'hulc', 'bcna', 'hope', 'rac', 'marble', 'coin', 'primo', 'daisy', 'future',
                 'bfot', 'phmn', 'arto']

osmosis_list = ['atom', 'ion', 'akt', 'dvpn', 'iris', 'cro', 'xprt', 'regen', 'iov', 'ngm', 'eeur', 'juno', 'like',
                'ixo', 'ust', 'luna', 'bcna', 'btsg', 'xki', 'scrt', 'med', 'boot', 'cmdx', 'cheq', 'stars', 'huahua',
                'lum', 'vdl', 'dsm', 'dig', 'grav', 'somm', 'rowan', 'band', 'darc', 'neta', 'umee', 'dec', 'pstake',
                'marble', 'swth']

marbledao_list = ['block', 'marble', 'juno', 'atom', 'ust', 'luna', 'osmo', 'scrt', 'neta']


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
                        prices_of_coin = [junoswap_list[el2]]
                        for el in values:
                            start = datetime.datetime.now()
                            mainCoinInput.send_keys(Keys.CONTROL + "a")
                            mainCoinInput.send_keys(Keys.DELETE)
                            mainCoinInput.send_keys(str(el))

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
                            prices_of_coin.append([input_value, response_value, flipped_value])
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

    class Sifchain:
        def get_all_coins():
            # Configs
            path = './chromedriver'
            driver = webdriver.Chrome(path)
            url = "https://sifchain-dex.forbole.com/#/swap?from=uatom&to=rowan&slippage=1.0"
            driver.get(url)
            time.sleep(4)
            print(len(driver.find_elements(by=By.TAG_NAME, value='button')))

            # Click on button of all coins
            driver.find_elements(by=By.TAG_NAME, value='button')[7].click()
            time.sleep(10000)

    class Marbledao:
        def get_all_coins():
            # Configs
            path = './chromedriver'
            driver = webdriver.Chrome(path)
            url = "https://app1.marbledao.finance/"
            driver.get(url)

            # Click on button of all coins
            driver.find_elements(by=By.CLASS_NAME, value='c-feNcEI')[0].click()

            coins = [el.text.lower() for el in
                     driver.find_element(by=By.CLASS_NAME, value='c-fPFUuh').find_elements(by=By.CLASS_NAME,
                                                                                           value='c-dOfGRD-ihyvuql-css')[
                     ::2]]
            return coins

        def get_prices(main_coin_id, values, add_coins):

            allCoins = marbledao_list

            # Configs
            path = './chromedriver'
            driver = webdriver.Chrome(path)
            url = "https://app1.marbledao.finance/"
            driver.get(url)

            # Click on button of all coins
            driver.find_elements(by=By.CLASS_NAME, value='c-feNcEI')[0].click()

            # Choose a main coin
            driver.find_element(by=By.CLASS_NAME, value='c-fPFUuh').find_elements(by=By.CLASS_NAME,
                                                                                  value='c-dOfGRD-ihyvuql-css')[::2][
                main_coin_id].click()

            prices_of_coins = []

            for el in add_coins:
                if el != main_coin_id:
                    # Click on button of all addiction coins
                    driver.find_elements(by=By.CLASS_NAME, value='c-feNcEI')[1].click()
                    # Choose an addiction coin
                    driver.find_element(by=By.CLASS_NAME, value='c-fPFUuh').find_elements(by=By.CLASS_NAME,
                                                                                          value='c-dOfGRD-ihyvuql-css')[
                    ::2][el].click()

                    prices_of_coin = [allCoins[el]]
                    # Loop
                    for el2 in values:
                        mainCoinInput = driver.find_elements(by=By.CLASS_NAME, value='c-GGohk')[0]
                        mainCoinInput.send_keys(Keys.CONTROL + 'a')
                        mainCoinInput.send_keys(Keys.DELETE)
                        mainCoinInput.send_keys(str(el2))

                        addCoinInput = driver.find_elements(by=By.CLASS_NAME, value='c-GGohk')[1]
                        value = float(el2)
                        value2 = float(addCoinInput.get_attribute('value'))
                        flip = driver.find_element(by=By.CLASS_NAME, value='kOSkYZ')
                        flip.click()
                        value_flipped = float(
                            driver.find_elements(by=By.CLASS_NAME, value='c-GGohk')[0].get_attribute('value'))
                        flip.click()
                        prices_of_coin.append([value, value2, value_flipped])
                    prices_of_coins.append(prices_of_coin)
                else:
                    continue
            return prices_of_coins

    class Osmosis:
        def get_all_coins():
            # Configs
            path = './chromedriver'
            driver = webdriver.Chrome(path)
            url = "https://app.osmosis.zone"
            driver.get(url)

            try:
                driver.find_element(by=By.CLASS_NAME, value='mr-5').click()
                driver.find_element(by=By.CLASS_NAME, value='px-8').click()
            except:
                pass

            driver.find_elements(by=By.CLASS_NAME, value='css-1de6nk0')[0].click()

            return [el.find_element(by=By.TAG_NAME, value='h5').text.lower() for el in
                    driver.find_elements(by=By.CLASS_NAME, value='ml-3')]

        def get_prices(main_coin_id, values, add_coins):
            # Configs
            path = './chromedriver'
            driver = webdriver.Chrome(path)
            url = "https://app.osmosis.zone"
            driver.get(url)

            try:
                driver.find_element(by=By.CLASS_NAME, value='mr-5').click()
                driver.find_element(by=By.CLASS_NAME, value='px-8').click()
            except:
                pass

            driver.find_elements(by=By.CLASS_NAME, value='css-1de6nk0')[0].click()
            driver.find_elements(by=By.CLASS_NAME, value='css-1dlj0eh')[main_coin_id].click()

            prices_of_coins = []
            for el in add_coins:
                driver.find_elements(by=By.CLASS_NAME, value='css-1de6nk0')[1].click()
                driver.find_elements(by=By.CLASS_NAME, value='css-1dlj0eh')[el].click()
                prices_of_coin = [osmosis_list[el]]
                for el2 in values:
                    main_coin_input = driver.find_elements(by=By.CLASS_NAME, value='css-1ui17as')[0]
                    main_coin_input.send_keys(Keys.CONTROL + 'a')
                    main_coin_input.send_keys(Keys.DELETE)
                    main_coin_input.send_keys(str(el2))
                    time.sleep(1)
                    response_input = driver.find_elements(by=By.CLASS_NAME, value='css-1alvqnw')[0].text.split(' ')[1]
                    flip = driver.find_element(by=By.CLASS_NAME, value='css-1so39r0')
                    flip.click()
                    flipped_input = driver.find_elements(by=By.CLASS_NAME, value='css-1alvqnw')[0].text.split(' ')[1]
                    prices_of_coin.append([el2, response_input, flipped_input])
                    time.sleep(1)
                    flip.click()
                prices_of_coins.append(prices_of_coin)

            return prices_of_coins


# Junoswap (done)
# print(getInfo.JunoSwap.get_prices(0, [80, 100], range(0, 20)))

# Sifchain
# getInfo.Sifchain.get_all_coins()

# Marbledao (done)
# print(getInfo.Marbledao.get_all_coins())
# print(getInfo.Marbledao.get_prices(6, [80, 100], range(9)))

# Osmosis
# print(getInfo.Osmosis.get_all_coins())
print(getInfo.Osmosis.get_prices(3, [80, 100], [1, 2, 3, 4]))
