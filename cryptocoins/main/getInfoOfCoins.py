from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime, time, pickle
from multiprocessing import Process

junoswap_list = ['juno', 'atom', 'ust', 'btsg', 'luna', 'osmo', 'stars', 'huahua', 'akt', 'xprt', 'cmdx', 'dig', 'scrt',
                 'neta', 'canlab', 'tuck', 'hulc', 'bcna', 'hope', 'rac', 'marble', 'coin', 'primo', 'daisy', 'future',
                 'bfot', 'phmn', 'arto']

osmosis_list = ['atom', 'ion', 'akt', 'dvpn', 'iris', 'cro', 'xprt', 'regen', 'iov', 'ngm', 'eeur', 'juno', 'like',
                'ixo', 'ust', 'luna', 'bcna', 'btsg', 'xki', 'scrt', 'med', 'boot', 'cmdx', 'cheq', 'stars', 'huahua',
                'lum', 'vdl', 'dsm', 'dig', 'grav', 'somm', 'rowan', 'band', 'darc', 'neta', 'umee', 'dec', 'pstake',
                'marble', 'swth']

marbledao_list = ['block', 'marble', 'juno', 'atom', 'ust', 'luna', 'osmo', 'scrt', 'neta']

sifchain_list = ['rowan', '1inch', 'aave', 'akro', 'akt', 'ant', 'atom', 'axs', 'b20', 'bal', 'band', 'bat', 'bnt',
                 'bond', 'btsg (erc-20)', 'cocos', 'comp', 'conv', 'cream', 'cro', 'csms', 'dai', 'daofi', 'dfyn',
                 'dino', 'dnxc', 'don', 'dvpn', 'eeur', 'enj', 'ern', 'esd', 'eth', 'frax', 'ftm', 'fxs', 'grt', 'iotx',
                 'iris', 'ixo', 'juno', 'keep', 'kft', 'ldo', 'leash', 'lgcy', 'lina', 'link', 'lon', 'lrc', 'luna',
                 'mana', 'matic', 'metis', 'ngm', 'ocean', 'ogn', 'oh', 'osmo', 'paid', 'pols', 'pond', 'quick', 'rail',
                 'ratom', 'reef', 'regen', 'rfuel', 'rly', 'rndr', 'rune', 'saito', 'sand', 'shib', 'snx', 'srm',
                 'susd', 'sushi', 'sxp', 'tidal', 'toke', 'tshp', 'tusd', 'ufo', 'uma', 'uni', 'usdc', 'usdt', 'ust',
                 'ust', 'wbtc', 'wfil', 'wscrt', 'xprt', 'yfi', 'zcn', 'zcx', 'zrx']

driver_path = './chromedriver'


class getInfo:
    class JunoSwap:
        def get_all_coins():
            start = datetime.datetime.now()

            path = driver_path
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
                start = datetime.datetime.now()
                # Prices of coins (response)
                prices = []

                # Configs
                path = driver_path
                driver = webdriver.Chrome(path)
                url = "https://junoswap.com/"
                driver.get(url)
                print(f'\n')

                # Open list to choose main coin
                driver.find_element(by=By.CLASS_NAME, value='c-fkNNfJ-cjOYsE-state-selected').click()

                # # Get list of all coins ???????????????????????????????
                # all_coins = driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')

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

                            prices_of_coin.append([input_value, response_value, flipped_value])
                        prices.append(prices_of_coin)
                    else:
                        continue

                driver.close()
                print(f'[JunoSwap: {datetime.datetime.now() - start}]')
                return prices
            except Exception as e:
                print(str(e))
                time.sleep(100000)

    class Sifchain:
        def get_all_coins():
            # Configs
            path = driver_path
            driver = webdriver.Chrome(path)
            url = "https://sifchain-dex.forbole.com/#/swap?from=uatom&to=rowan&slippage=1.0"
            driver.get(url)
            time.sleep(1)

            # Click on button of all coins
            driver.find_elements(by=By.TAG_NAME, value='button')[7].click()

            return [el.text.split('\n')[0].lower() for el in
                    driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')]
            # # Click on button of all addiction coins
            # driver.find_elements(by=By.TAG_NAME, value='button')[10].click()

            # # # Click on button to swipe coins
            # driver.find_elements(by=By.TAG_NAME, value='button')[9].click()

        def get_prices(main_coin_id, values, add_coins):
            start = datetime.datetime.now()
            # Configs
            path = driver_path
            driver = webdriver.Chrome(path)
            url = "https://sifchain-dex.forbole.com/#/swap?from=uatom&to=rowan&slippage=1.0"
            driver.get(url)
            print(f'\n')
            time.sleep(3)

            # Click on button of all coins
            driver.find_elements(by=By.TAG_NAME, value='button')[7].click()
            driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')[main_coin_id].click()

            # driver.find_elements(by=By.CLASS_NAME, value='token-input')[1].send_keys('100')
            # driver.find_elements(by=By.CLASS_NAME, value='token-input')[3].get_attribute('value')

            prices_of_coins = []
            for el in add_coins:
                prices_of_coin = [sifchain_list[el]]
                if main_coin_id != el:
                    # Click on button of all addiction coins
                    driver.find_elements(by=By.TAG_NAME, value='button')[10].click()
                    driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')[el].click()

                    time.sleep(0.2)
                    for el2 in values:
                        mainCoinInput = driver.find_elements(by=By.CLASS_NAME, value='token-input')[1]
                        mainCoinInput.send_keys(Keys.CONTROL + 'a')
                        mainCoinInput.send_keys(Keys.DELETE)
                        mainCoinInput.send_keys(str(el2))
                        # print(driver.find_elements(by=By.CLASS_NAME, value='token-input')[3].get_attribute('value'))
                        response = driver.find_elements(by=By.CLASS_NAME, value='token-input')[3].get_attribute('value')

                        # Click on button to swipe coins
                        flip = driver.find_elements(by=By.TAG_NAME, value='button')[9]
                        flip.click()

                        time.sleep(0.2)
                        response_flipped = driver.find_elements(by=By.CLASS_NAME, value='token-input')[1].get_attribute(
                            'value')
                        flip.click()
                        prices_of_coin.append([float(el2), response, response_flipped])
                    prices_of_coins.append(prices_of_coin)
                else:
                    continue
            print(f'[Sifchain: {datetime.datetime.now() - start}]')
            return prices_of_coins

    class Marbledao:
        def get_all_coins():
            # Configs
            path = driver_path
            driver = webdriver.Chrome(path)
            url = "https://app1.marbledao.finance/"
            driver.get(url)
            print(f'\n')

            # Click on button of all coins
            driver.find_elements(by=By.CLASS_NAME, value='c-feNcEI')[0].click()

            coins = [el.text.lower() for el in
                     driver.find_element(by=By.CLASS_NAME, value='c-fPFUuh').find_elements(by=By.CLASS_NAME,
                                                                                           value='c-dOfGRD-ihyvuql-css')[
                     ::2]]
            return coins

        def get_prices(main_coin_id, values, add_coins):
            start = datetime.datetime.now()
            allCoins = marbledao_list

            # Configs
            path = driver_path
            driver = webdriver.Chrome(path)
            url = "https://app1.marbledao.finance/"
            driver.get(url)
            print(f'\n')

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
            print(f'[Marbledao: {datetime.datetime.now() - start}]')
            return prices_of_coins

    class Osmosis:
        def get_all_coins():
            # Configs
            path = driver_path
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
            start = datetime.datetime.now()
            # Configs
            path = driver_path
            driver = webdriver.Chrome(path)
            url = "https://app.osmosis.zone"
            driver.get(url)
            print(f'\n')

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
            print(f'[Osmosis: {datetime.datetime.now() - start}]')
            return prices_of_coins


# Junoswap (done)
# print(getInfo.JunoSwap.get_prices(0, [80, 100], range(0, 20)))

# Sifchain
# print(getInfo.Sifchain.get_all_coins())
# print(getInfo.Sifchain.get_prices(5, [80, 100], [1, 2, 3, 4]))

# Marbledao (done)
# print(getInfo.Marbledao.get_all_coins())
# print(getInfo.Marbledao.get_prices(6, [80, 100], range(9)))

# Osmosis (done)
# print(getInfo.Osmosis.get_all_coins())
# print(getInfo.Osmosis.get_prices(3, [80, 100], [1, 2, 3, 4]))

if __name__ == '__main__':

    def save_junoswap():
        try:
            data = getInfo.JunoSwap.get_prices(0, [80, 100], range(11))
            with open('junoswap.pickle', 'wb') as f:
                pickle.dump(data, f)
            print(f'[Junoswap is loaded]')
        except:
            print(f'[Junoswap is not loaded!]')


    def save_sifchain():
        try:
            data = getInfo.Sifchain.get_prices(0, [80, 100], range(11))
            with open('sifchain.pickle', 'wb') as f:
                pickle.dump(data, f)
            print(f'[Sifchain is loaded]')
        except Exception as e:
            print(str(e))
            print(f'[Sifchain is not loaded!]')


    def save_marbledao():
        try:
            data = getInfo.Marbledao.get_prices(0, [80, 100], range(11))
            with open('marbledao.pickle', 'wb') as f:
                pickle.dump(data, f)
            print(f'[Marbledao is loaded]')
        except Exception as e:
            print(str(e))
            print(f'[Marbledao is not loaded!]')


    def save_osmosis():
        try:
            data = getInfo.Osmosis.get_prices(0, [80, 100], range(11))
            with open('osmosis.pickle', 'wb') as f:
                pickle.dump(data, f)
            print(f'[Osmosis is loaded]')
        except:
            print(f'[Osmosis is not loaded!]')


    junoswap = Process(target=save_junoswap)
    junoswap.start()
    sifchain = Process(target=save_sifchain)
    sifchain.start()
    marbledao = Process(target=save_marbledao)
    marbledao.start()
    osmosis = Process(target=save_osmosis)
    osmosis.start()

    # data = {}
    # data['junoswap'] = getInfo.JunoSwap.get_prices(0, [80, 100], range(0, 20))
    # data['sifchain'] = getInfo.Sifchain.get_prices(5, [80, 100], [1, 2, 3, 4])
    # data['marbledao'] = getInfo.Marbledao.get_prices(6, [80, 100], range(9))
    # data['osmosis'] = await getInfo.Osmosis.get_prices(3, [80, 100], [1, 2, 3, 4])

    # Saving to the file
