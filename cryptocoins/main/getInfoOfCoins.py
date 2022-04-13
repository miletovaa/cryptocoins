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


def artificial_delay():
    # time.sleep(2)
    pass


class getInfo:
    class JunoSwap:
        def get_all_coins():

            path = driver_path
            driver = webdriver.Chrome(path)
            url = "https://junoswap.com/"
            driver.get(url)
            artificial_delay()

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
                junoswap_list = [el.text.split()[0].lower() for el in
                                 driver.find_elements(by=By.CLASS_NAME, value='c-jVTssZ')]
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
                            time.sleep(0.4)
                            artificial_delay()
                            response_value = driver.find_elements(by=By.CLASS_NAME, value='c-dwExUq')[1].get_property(
                                'value')
                            flip = driver.find_element(by=By.CLASS_NAME, value='c-PJLV')
                            flip.click()
                            time.sleep(0.4)
                            artificial_delay()

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
            artificial_delay()

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
            artificial_delay()

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
                    for el2 in values:
                        mainCoinInput = driver.find_elements(by=By.CLASS_NAME, value='token-input')[1]
                        mainCoinInput.send_keys(Keys.CONTROL + 'a')
                        mainCoinInput.send_keys(Keys.DELETE)
                        mainCoinInput.send_keys(str(el2))
                        time.sleep(0.3)
                        # print(driver.find_elements(by=By.CLASS_NAME, value='token-input')[3].get_attribute('value'))
                        response = driver.find_elements(by=By.CLASS_NAME, value='token-input')[3].get_attribute('value')

                        # Click on button to swipe coins
                        flip = driver.find_elements(by=By.TAG_NAME, value='button')[9]
                        flip.click()

                        time.sleep(0.3)
                        artificial_delay()
                        response_flipped = driver.find_elements(by=By.CLASS_NAME, value='token-input')[1].get_attribute(
                            'value')
                        flip.click()
                        prices_of_coin.append(
                            [float(el2) if el2 != '' else 0.0, float(response) if response != '' else 0.0,
                             float(response_flipped) if response_flipped != '' else 0.0])
                        # print([float(el2) if el2 != '' else 0.0, float(response) if response != '' else 0.0,
                        #      float(response_flipped) if response_flipped != '' else 0.0])
                    prices_of_coins.append(prices_of_coin)
                else:
                    continue
            print(prices_of_coins)
            return prices_of_coins

    class Marbledao:
        def get_all_coins():
            # Configs
            path = driver_path
            driver = webdriver.Chrome(path)
            url = "https://app1.marbledao.finance/"
            driver.get(url)
            print(f'\n')
            artificial_delay()

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
                        artificial_delay()

                        addCoinInput = driver.find_elements(by=By.CLASS_NAME, value='c-GGohk')[1]
                        value = float(el2)
                        value2 = float(addCoinInput.get_attribute('value'))
                        flip = driver.find_element(by=By.CLASS_NAME, value='kOSkYZ')
                        flip.click()
                        time.sleep(0.3)
                        artificial_delay()
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
            artificial_delay()

            try:
                driver.find_element(by=By.CLASS_NAME, value='mr-5').click()
                driver.find_element(by=By.CLASS_NAME, value='px-8').click()
            except:
                pass

            driver.find_elements(by=By.CLASS_NAME, value='css-1de6nk0')[0].click()

            return [el.find_element(by=By.TAG_NAME, value='h5').text.lower() for el in
                    driver.find_elements(by=By.CLASS_NAME, value='ml-3')]

        def get_prices(main_coin, values, add_coins_names):
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
            main_all_coins_names = [el.find_element(by=By.TAG_NAME, value='h5').text.lower() for el in
                                    driver.find_elements(by=By.CLASS_NAME, value='ml-3')]
            main_coin_id = main_all_coins_names.index(main_coin)
            driver.find_elements(by=By.CLASS_NAME, value='css-1dlj0eh')[main_coin_id].click()

            driver.find_elements(by=By.CLASS_NAME, value='css-1de6nk0')[1].click()
            all_coins_names = [el.find_element(by=By.TAG_NAME, value='h5').text.lower() for el in
                               driver.find_elements(by=By.CLASS_NAME, value='ml-3')]
            add_coins = [all_coins_names.index(el) for el in add_coins_names]
            driver.find_elements(by=By.CLASS_NAME, value='css-1de6nk0')[1].click()

            prices_of_coins = []
            for el in add_coins:
                driver.find_elements(by=By.CLASS_NAME, value='css-1de6nk0')[1].click()
                driver.find_elements(by=By.CLASS_NAME, value='css-1dlj0eh')[el].click()
                time.sleep(4)
                prices_of_coin = [all_coins_names[el]]
                for el2 in values:
                    main_coin_input = driver.find_elements(by=By.CLASS_NAME, value='css-1ui17as')[0]
                    main_coin_input.send_keys(Keys.CONTROL + 'a')
                    main_coin_input.send_keys(Keys.DELETE)
                    main_coin_input.send_keys(str(el2))
                    time.sleep(0.5)
                    artificial_delay()
                    response_input = driver.find_elements(by=By.CLASS_NAME, value='css-1alvqnw')[0].text.split(' ')[1]
                    flip = driver.find_element(by=By.CLASS_NAME, value='css-1so39r0')
                    flip.click()
                    time.sleep(0.5)
                    flipped_input = driver.find_elements(by=By.CLASS_NAME, value='css-1alvqnw')[0].text.split(' ')[1]
                    prices_of_coin.append(
                        [float(el2) if el2 != '' else 0.0,
                         float(response_input.replace(',', '')) if response_input != '' else 0.0,
                         float(flipped_input.replace(',', '')) if flipped_input != '' else 0.0])
                    time.sleep(1)
                    artificial_delay()
                    flip.click()
                prices_of_coins.append(prices_of_coin)
            return prices_of_coins


configs_data = pickle.load(open('configs.pickle', 'rb'))


def save_junoswap():
    try:
        start = datetime.datetime.now()
        data = getInfo.JunoSwap.get_prices(configs_data['main_coin'], configs_data['values'],
                                           configs_data['add_coins']['junoswap'])
        with open('junoswap.pickle', 'wb') as f:
            pickle.dump(data, f)
        xlsx_writer.write()
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
        print(data)
        with open('sifchain.pickle', 'wb') as f:
            pickle.dump(data, f)
        xlsx_writer.write()
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
        data = getInfo.Osmosis.get_prices(configs_data['main_coin'], configs_data['values'],
                                          configs_data['add_coins']['osmosis'])
        with open('osmosis.pickle', 'wb') as f:
            pickle.dump(data, f)
        xlsx_writer.write()
        print(f'[Osmosis is loaded ({datetime.datetime.now() - start})]')
    except Exception as e:
        with open('osmosis.pickle', 'wb') as f:
            pickle.dump(None, f)
        print(f'[Osmosis is not loaded! ({str(e)})]')


if __name__ == '__main__':
    junoswap = Process(target=save_junoswap)
    junoswap.start()
    sifchain = Process(target=save_sifchain)
    sifchain.start()
    marbledao = Process(target=save_marbledao)
    marbledao.start()
    osmosis = Process(target=save_osmosis)
    osmosis.start()
