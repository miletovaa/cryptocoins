from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime, time, pickle
from multiprocessing import Process
import xlsx_writer
from selenium.webdriver.chrome.options import Options

driver_path = './chromedriver'


def artificial_delay():
    # time.sleep(2)
    pass


chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')


# chrome_options.add_argument('--disable-dev-shm-usage')


class getInfo:
    class JunoSwap:
        def get_all_coins():

            path = driver_path
            driver = webdriver.Chrome(path, chrome_options=chrome_options)
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
            # Prices of coins (response)
            prices = []

            # Configs
            path = driver_path
            driver = webdriver.Chrome(path, chrome_options=chrome_options)
            url = "https://junoswap.com/"
            driver.get(url)
            time.sleep(1)

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
                        mainCoinInput.send_keys(str(int(el)))

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

    class Sifchain:
        def get_all_coins():
            # Configs
            path = driver_path
            driver = webdriver.Chrome(path, chrome_options=chrome_options)
            url = "https://sifchain-dex.forbole.com/#/swap?from=uatom&to=rowan&slippage=1.0"
            driver.get(url)
            time.sleep(5)
            artificial_delay()

            # Click on button of all coins
            driver.find_elements(by=By.TAG_NAME, value='button')[9].click()
            return [el.text.split('\n')[0].lower() for el in
                    driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')]

        def get_prices(main_coin, values, add_coins_names):
            # Configs
            path = driver_path
            driver = webdriver.Chrome(path, chrome_options=chrome_options)
            url = "https://sifchain-dex.forbole.com/#/swap?from=uatom&to=rowan&slippage=1.0"
            driver.get(url)
            time.sleep(5)
            artificial_delay()

            # Click on button of all coins
            driver.find_elements(by=By.TAG_NAME, value='button')[6].click()
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

            prices_of_coins = []
            for el in add_coins:
                prices_of_coin = [all_coins[el]]
                if main_coin_id != el:
                    # Click on button of all addiction coins
                    driver.find_elements(by=By.TAG_NAME, value='button')[9].click()
                    driver.find_elements(by=By.CLASS_NAME, value='list-complete-item')[el].click()
                    for el2 in values:
                        mainCoinInput = driver.find_elements(by=By.CLASS_NAME, value='token-input')[1]
                        mainCoinInput.send_keys(Keys.CONTROL + 'a')
                        mainCoinInput.send_keys(Keys.DELETE)
                        mainCoinInput.send_keys(str(el2))
                        time.sleep(2)
                        # print(driver.find_elements(by=By.CLASS_NAME, value='token-input')[3].get_attribute('value'))
                        response = driver.find_elements(by=By.CLASS_NAME, value='token-input')[3].get_attribute('value')
                        provider = driver.find_elements(by=By.CLASS_NAME, value='text-md')[11].text

                        # Click on button to swipe coins
                        flip = driver.find_elements(by=By.TAG_NAME, value='button')[8]
                        flip.click()

                        time.sleep(2)
                        provider2 = driver.find_elements(by=By.CLASS_NAME, value='text-md')[11].text
                        # artificial_delay()
                        # response_flipped = driver.find_elements(by=By.CLASS_NAME, value='token-input')[1].get_attribute(
                        #     'value')
                        flip.click()
                        response_flipped = response
                        prices_of_coin.append(
                            [float(el2) if el2 != '' else 0.0, float(response) if response != '' else 0.0,
                             float(response_flipped) if response_flipped != '' else 0.0,
                             float(provider) if provider != '' else 0.0, float(provider2) if provider2 != '' else 0.0])
                        # print([float(el2) if el2 != '' else 0.0, float(response) if response != '' else 0.0,
                        #      float(response_flipped) if response_flipped != '' else 0.0])
                    prices_of_coins.append(prices_of_coin)
                else:
                    continue
            return prices_of_coins

    class Marbledao:
        def get_all_coins():
            # Configs
            path = driver_path
            driver = webdriver.Chrome(path, chrome_options=chrome_options)
            url = "https://app1.marbledao.finance/"
            driver.get(url)
            artificial_delay()

            # Click on button of all coins
            driver.find_elements(by=By.CLASS_NAME, value='c-feNcEI')[0].click()

            coins = [el.text.lower() for el in
                     driver.find_element(by=By.CLASS_NAME, value='c-fPFUuh').find_elements(by=By.CLASS_NAME,
                                                                                           value='c-dOfGRD-ihyvuql-css')[
                     ::2]]
            return coins

        def get_prices(main_coin, values, add_coins_names):

            # Configs
            path = driver_path
            driver = webdriver.Chrome(path, chrome_options=chrome_options)
            url = "https://app1.marbledao.finance/"
            driver.get(url)

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

                    prices_of_coin = [all_coins_names[el]]
                    # Loop
                    for el2 in values:
                        mainCoinInput = driver.find_elements(by=By.CLASS_NAME, value='c-GGohk')[0]
                        mainCoinInput.send_keys(Keys.CONTROL + 'a')
                        mainCoinInput.send_keys(Keys.DELETE)
                        mainCoinInput.send_keys(str(int(el2)))

                        time.sleep(0.4)
                        artificial_delay()

                        addCoinInput = driver.find_elements(by=By.CLASS_NAME, value='c-GGohk')[1]
                        value = float(el2)
                        value2 = float(addCoinInput.get_attribute('value'))
                        flip = driver.find_element(by=By.CLASS_NAME, value='kOSkYZ')
                        flip.click()
                        time.sleep(0.4)
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
            driver = webdriver.Chrome(path, chrome_options=chrome_options)
            url = "https://app.osmosis.zone"
            driver.get(url)
            artificial_delay()

            try:
                driver.find_element(by=By.CLASS_NAME, value='mr-5').click()
                driver.find_element(by=By.CLASS_NAME, value='px-8').click()
            except:
                pass

            driver.find_elements(by=By.CLASS_NAME, value='css-1de6nk0')[0].click()

            print([el.find_element(by=By.TAG_NAME, value='h5').text.lower() for el in
                   driver.find_elements(by=By.CLASS_NAME, value='ml-3')] + ['osmo'])

            return [el.find_element(by=By.TAG_NAME, value='h5').text.lower() for el in
                    driver.find_elements(by=By.CLASS_NAME, value='ml-3')] + ['osmo']

        def get_prices(main_coin, values, add_coins_names):
            # Configs
            path = driver_path
            driver = webdriver.Chrome(path, chrome_options=chrome_options)
            url = "https://app.osmosis.zone"
            driver.get(url)

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
                time.sleep(1)
                prices_of_coin = [all_coins_names[el]]
                for el2 in values:
                    main_coin_input = driver.find_elements(by=By.CLASS_NAME, value='css-1ui17as')[0]
                    main_coin_input.send_keys(Keys.CONTROL + 'a')
                    main_coin_input.send_keys(Keys.DELETE)
                    main_coin_input.send_keys(str(el2))
                    time.sleep(0.4)
                    artificial_delay()
                    response_input = driver.find_elements(by=By.CLASS_NAME, value='css-1alvqnw')[0].text.split(' ')[1]
                    # flip = driver.find_element(by=By.CLASS_NAME, value='css-1so39r0')
                    # flip.click()
                    # time.sleep(0.4)
                    # flipped_input = driver.find_elements(by=By.CLASS_NAME, value='css-1alvqnw')[0].text.split(' ')[1]
                    prices_of_coin.append(
                        [float(el2) if el2 != '' else 0.0,
                         float(response_input.replace(',', '')) if response_input != '' else 0.0,
                         0.0])
                    artificial_delay()
                    # flip.click()
                prices_of_coins.append(prices_of_coin)
            return prices_of_coins

    class Crescent:
        def get_all_coins():
            # Configs
            path = driver_path
            driver = webdriver.Chrome(path, chrome_options=chrome_options)
            url = "https://app.crescent.network/swap"
            driver.get(url)
            time.sleep(0.5)
            artificial_delay()

            driver.find_elements(by=By.CLASS_NAME, value='text-yellowCRE-200')[4].click()
            driver.find_elements(by=By.CLASS_NAME, value='text-whiteCRE')[3].click()

            # Click to view list of coins
            driver.find_elements(by=By.CLASS_NAME, value='text-blackCRE')[5].click()
            time.sleep(0.2)
            return [el.text.lower() for el in driver.find_elements(by=By.CLASS_NAME, value='sBOLD18')]

        def get_prices(main_coin, values, add_coins_names):
            path = driver_path
            driver = webdriver.Chrome(path, chrome_options=chrome_options)
            url = "https://app.crescent.network/swap"
            driver.get(url)
            time.sleep(1)
            artificial_delay()

            driver.find_elements(by=By.CLASS_NAME, value='text-yellowCRE-200')[4].click()
            driver.find_elements(by=By.CLASS_NAME, value='text-whiteCRE')[3].click()

            # Click to view list of coins
            driver.find_elements(by=By.CLASS_NAME, value='text-blackCRE')[5].click()

            main_coin_el = \
                [el for el in driver.find_elements(by=By.CLASS_NAME, value='sBOLD18') if el.text.lower() == main_coin][
                    0]
            # Click to main coin element
            main_coin_el.click()

            # Click to view all list if addiction coins
            driver.find_elements(by=By.CLASS_NAME, value='text-whiteCRE')[1].click()
            time.sleep(0.1)
            add_coins_el = [el for el in driver.find_elements(by=By.CLASS_NAME, value='sBOLD18') if
                            el.text.lower() in add_coins_names]
            # Choose the first addiction coin
            add_coins_el[0].click()

            prices_of_coins = []

            for el in add_coins_names:
                if el != main_coin:
                    prices_of_coin = [el, ]
                    driver.find_elements(by=By.CLASS_NAME, value='text-blackCRE')[8].click()
                    time.sleep(2)
                    add_coins_el = driver.find_elements(by=By.CLASS_NAME, value='sBOLD18')
                    all_add_coins_names = [el.text.lower() for el in add_coins_el]
                    add_coins_el[all_add_coins_names.index(el)].click()

                    main_coin_input = driver.find_elements(by=By.TAG_NAME, value='input')[0]

                    for el2 in values:
                        main_coin_input.send_keys(Keys.CONTROL + 'a')
                        main_coin_input.send_keys(Keys.DELETE)
                        main_coin_input.send_keys(str(el2))
                        time.sleep(0.25)
                        response = driver.find_elements(by=By.TAG_NAME, value='input')[1].get_attribute('value')

                        flip = driver.find_elements(by=By.TAG_NAME, value='button')[5]
                        flip.click()
                        time.sleep(0.25)
                        response_flipped = driver.find_elements(by=By.TAG_NAME, value='input')[1].get_attribute('value')
                        prices_of_coin.append([el2, response, response_flipped])
                        flip.click()
                    prices_of_coins.append(prices_of_coin)
            return prices_of_coins


configs_data = pickle.load(open('configs.pickle', 'rb'))


def save_junoswap():
    if configs_data['add_coins']['junoswap']:
        try:
            start = datetime.datetime.now()
            data = getInfo.JunoSwap.get_prices(configs_data['main_coin'], configs_data['values'],
                                               configs_data['add_coins']['junoswap'])
            with open('junoswap.pickle', 'wb') as f:
                pickle.dump(data, f)
            # xlsx_writer.write()
            print(f'[Junoswap is loaded ({datetime.datetime.now() - start})]')
            # send_message()
        except Exception as e:
            with open('junoswap.pickle', 'wb') as f:
                pickle.dump(None, f)
            print(f'[Junoswap is not loaded! ({str(e)[:25]})]')
    else:
        with open('junoswap.pickle', 'wb') as f:
            pickle.dump(None, f)


def save_sifchain():
    if configs_data['add_coins']['sifchain']:
        try:
            start = datetime.datetime.now()
            data = getInfo.Sifchain.get_prices(configs_data['main_coin'], configs_data['values'],
                                               configs_data['add_coins']['sifchain'])
            with open('sifchain.pickle', 'wb') as f:
                pickle.dump(data, f)
            # xlsx_writer.write()
            print(f'[Sifchain is loaded ({datetime.datetime.now() - start})]')
            # send_message()
        except Exception as e:
            with open('sifchain.pickle', 'wb') as f:
                pickle.dump(None, f)
            print(f'[Sifchain is not loaded! ({str(e)[:25]})]')
    else:
        with open('sifchain.pickle', 'wb') as f:
            pickle.dump(None, f)


def save_marbledao():
    if configs_data['add_coins']['marbledao']:
        try:
            start = datetime.datetime.now()
            data = getInfo.Marbledao.get_prices(configs_data['main_coin'], configs_data['values'],
                                                configs_data['add_coins']['marbledao'])
            with open('marbledao.pickle', 'wb') as f:
                pickle.dump(data, f)
            print(f'[Marbledao is loaded ({datetime.datetime.now() - start})]')
            # send_message()
        except Exception as e:
            with open('marbledao.pickle', 'wb') as f:
                pickle.dump(None, f)
            print(f'[Marbledao is not loaded! ({str(e)[:25]})]')
    else:
        with open('marbledao.pickle', 'wb') as f:
            pickle.dump(None, f)


def save_osmosis():
    if configs_data['add_coins']['osmosis']:
        try:
            start = datetime.datetime.now()
            data = getInfo.Osmosis.get_prices(configs_data['main_coin'], configs_data['values'],
                                              configs_data['add_coins']['osmosis'])
            with open('osmosis.pickle', 'wb') as f:
                pickle.dump(data, f)
            # xlsx_writer.write()
            print(f'[Osmosis is loaded ({datetime.datetime.now() - start})]')
            # send_message()
        except Exception as e:
            with open('osmosis.pickle', 'wb') as f:
                pickle.dump(None, f)
            print(f'[Osmosis is not loaded! ({str(e)[:25]})]')
    else:
        with open('osmosis.pickle', 'wb') as f:
            pickle.dump(None, f)


def save_crescent():
    if configs_data['add_coins']['crescent']:
        try:
            start = datetime.datetime.now()
            data = getInfo.Crescent.get_prices(configs_data['main_coin'], configs_data['values'],
                                               configs_data['add_coins']['crescent'])
            with open('crescent.pickle', 'wb') as f:
                pickle.dump(data, f)
            # xlsx_writer.write()
            print(f'[Crescent is loaded ({datetime.datetime.now() - start})]')
            # send_message()
        except Exception as e:
            with open('crescent.pickle', 'wb') as f:
                pickle.dump(None, f)
            print(f'[Crescent is not loaded! ({str(e)[:25]})]')
    else:
        with open('crescent.pickle', 'wb') as f:
            pickle.dump(None, f)


def main():
    while True:
        junoswap = Process(target=save_junoswap)
        junoswap.start()
        crescent = Process(target=save_crescent)
        crescent.start()
        sifchain = Process(target=save_sifchain)
        sifchain.start()
        marbledao = Process(target=save_marbledao)
        marbledao.start()
        osmosis = Process(target=save_osmosis)
        osmosis.start()
        junoswap.join()
        crescent.join()
        sifchain.join()
        marbledao.join()
        osmosis.join()
        print('[Saving...]')
        xlsx_writer.write()


if __name__ == '__main__':
    main()