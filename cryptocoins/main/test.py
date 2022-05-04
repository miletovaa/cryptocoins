from selenium.webdriver.common.by import By
import swapCoins
from selenium import webdriver
import time
import subprocess

sifchain_count_coins = swapCoins.SwapCoins.Sifchain()
driver = webdriver.Chrome(swapCoins.driver_path, options=swapCoins.chrome_options)
swapCoins.login(driver)

url = 'https://sifchain-dex.forbole.com/#/swap?from=uatom&to=rowan&slippage=1.0'

driver.get(url)
time.sleep(8)

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

time.sleep(1)

print(sifchain_count_coins.countCoins(driver))
driver.close()
