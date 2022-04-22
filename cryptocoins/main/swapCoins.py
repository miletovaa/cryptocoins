from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

driver_path = './chromedriver'
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')


class SwapCoins:
    class JunoSwap:
        def swapCoins(self):
            # Configs
            path = driver_path
            driver = webdriver.Chrome(path)
            url = "https://junoswap.com/"
            driver.get(url)
            time.sleep(10000000)


junoswap = SwapCoins.JunoSwap()
junoswap.swapCoins()
