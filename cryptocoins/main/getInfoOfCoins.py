from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime, time, pickle
from multiprocessing import Process
import xlsx_writer

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

            return list_of_coins

        ###################################################################
        def get_prices(main_coin, values, add_coins_names):
            try:
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
                main_coin_id = [el.text.split()[0].lower() for el in
                                driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')].index(main_coin)
                add_coins = []
                for item in add_coins_names:
                    try:
                        add_coins.append([el.text.split()[0].lower() for el in
                                          driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')].index(item))
                    except:
                        continue

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

                            prices_of_coin.append([float(input_value) if input_value != '' else 0.0,
                                                   float(response_value) if response_value != '' else 0.0,
                                                   float(flipped_value) if flipped_value != '' else 0.0])
                        prices.append(prices_of_coin)
                    else:
                        continue

                driver.close()
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

        def get_prices(main_coin, values, add_coins_names):
            # Configs
            path = driver_path
            driver = webdriver.Chrome(path)
            url = "https://sifchain-dex.forbole.com/#/swap?from=uatom&to=rowan&slippage=1.0"
            driver.get(url)
            print(f'\n')
            time.sleep(3)

            # Click on button of all coins
            driver.find_elements(by=By.TAG_NAME, value='button')[7].click()
            all_coins = [el.text.split('\n')[0].lower() for el in
                         driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')]
            main_coin_id = all_coins.index(main_coin)
            add_coins = []
            for el in add_coins_names:
                try:
                    add_coins.append(all_coins.index(el))
                except:
                    continue
            driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')[main_coin_id].click()
            # print(driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')[main_coin_id].text)

            # driver.find_elements(by=By.CLASS_NAME, value='token-input')[1].send_keys('100')
            # driver.find_elements(by=By.CLASS_NAME, value='token-input')[3].get_attribute('value')

            prices_of_coins = []
            for el in add_coins:
                prices_of_coin = [all_coins[el]]
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
                        prices_of_coin.append(
                            [float(el2) if el2 != '' else 0.0, float(response) if response != '' else 0.0,
                             float(response_flipped) if response_flipped != '' else 0.0])
                    prices_of_coins.append(prices_of_coin)
                else:
                    continue
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

        def get_prices(main_coin, values, add_coins_names):
            allCoins = marbledao_list

            # Configs
            path = driver_path
            driver = webdriver.Chrome(path)
            url = "https://app1.marbledao.finance/"
            driver.get(url)
            print(f'\n')

            # Click on button of all coins
            driver.find_elements(by=By.CLASS_NAME, value='c-feNcEI')[0].click()

            all_coins_names = [el.text.lower() for el in
                               driver.find_element(by=By.CLASS_NAME, value='c-fPFUuh').find_elements(by=By.CLASS_NAME,
                                                                                                     value='c-dOfGRD-ihyvuql-css')[
                               ::2]]

            add_coins = []
            for el in add_coins_names:
                add_coins.append(all_coins_names.index(el))
            main_coin_id = all_coins_names.index(main_coin)

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

                        time.sleep(0.35)

                        addCoinInput = driver.find_elements(by=By.CLASS_NAME, value='c-GGohk')[1]
                        value = float(el2)
                        value2 = float(addCoinInput.get_attribute('value'))
                        flip = driver.find_element(by=By.CLASS_NAME, value='kOSkYZ')
                        flip.click()
                        time.sleep(0.3)
                        value_flipped = float(
                            driver.find_elements(by=By.CLASS_NAME, value='c-GGohk')[1].get_attribute('value'))
                        flip.click()
                        prices_of_coin.append(
                            [float(value) if value != '' else 0.0, float(value2) if value2 != '' else 0.0,
                             float(value_flipped) if value_flipped != '' else 0.0])
                    prices_of_coins.append(prices_of_coin)
                else:
                    continue
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
                    prices_of_coin.append(
                        [float(el2) if el2 != '' else 0.0, float(response_input) if response_input != '' else 0.0,
                         float(flipped_input) if flipped_input != '' else 0.0])
                    time.sleep(1)
                    flip.click()
                prices_of_coins.append(prices_of_coin)
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

    configs_data = pickle.load(open('configs.pickle', 'rb'))


    def save_junoswap():
        try:
            start = datetime.datetime.now()
            data = getInfo.JunoSwap.get_prices(configs_data['main_coin'], configs_data['values'],
                                               configs_data['add_coins']['junoswap'])
            with open('junoswap.pickle', 'wb') as f:
                pickle.dump(data, f)
            print(f'[Junoswap is loaded ({datetime.datetime.now() - start})]')
        except Exception as e:
            with open('junoswap.pickle', 'wb') as f:
                pickle.dump(None, f)
            print(f'[Junoswap is not loaded! ({str(e)})]')


    def save_sifchain():
        try:
            start = datetime.datetime.now()
            data = getInfo.Sifchain.get_prices(configs_data['main_coin'], configs_data['values'],
                                               configs_data['add_coins']['sifchain'])
            with open('sifchain.pickle', 'wb') as f:
                pickle.dump(data, f)
            print(f'[Sifchain is loaded ({datetime.datetime.now() - start})]')
        except Exception as e:
            with open('sifchain.pickle', 'wb') as f:
                pickle.dump(None, f)
            print(f'[Sifchain is not loaded! ({str(e)})]')


    def save_marbledao():
        try:
            start = datetime.datetime.now()
            data = getInfo.Marbledao.get_prices(configs_data['main_coin'], configs_data['values'],
                                                configs_data['add_coins']['marbledao'])
            with open('marbledao.pickle', 'wb') as f:
                pickle.dump(data, f)
            print(f'[Marbledao is loaded ({datetime.datetime.now() - start})]')
        except Exception as e:
            with open('marbledao.pickle', 'wb') as f:
                pickle.dump(None, f)
            print(f'[Marbledao is not loaded! ({str(e)})]')


    def save_osmosis():
        try:
            start = datetime.datetime.now()
            data = getInfo.Osmosis.get_prices(0, configs_data['values'], range(11))
            with open('osmosis.pickle', 'wb') as f:
                pickle.dump(data, f)
            print(f'[Osmosis is loaded ({datetime.datetime.now() - start})]')
        except Exception as e:
            with open('osmosis.pickle', 'wb') as f:
                pickle.dump(None, f)
            print(f'[Osmosis is not loaded! ({str(e)})]')


    junoswap = Process(target=save_junoswap)
    junoswap.start()
    sifchain = Process(target=save_sifchain)
    sifchain.start()
    marbledao = Process(target=save_marbledao)
    marbledao.start()
    osmosis = Process(target=save_osmosis)
    osmosis.start()

    xlsx_writer.write()

    # data = {}
    # data['junoswap'] = getInfo.JunoSwap.get_prices(0, [80, 100], range(0, 20))
    # data['sifchain'] = getInfo.Sifchain.get_prices(5, [80, 100], [1, 2, 3, 4])
    # data['marbledao'] = getInfo.Marbledao.get_prices(6, [80, 100], range(9))
    # data['osmosis'] = await getInfo.Osmosis.get_prices(3, [80, 100], [1, 2, 3, 4])

    # Saving to the file
