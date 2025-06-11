from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


chrome_options = Options()


from saucedemo_elements import *

# Setup driver secara otomatis
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

# Buka situs
driver.get(url)

driver.find_element(*username).send_keys("xerosss1")
driver.find_element(*pw).send_keys("secret_sauce")

driver.find_element(*login).click()
alert = driver.find_element(*error_massage).text


print("FLASH NYA : "+ alert)

input("Tekan Enter untuk menutup browser...")

driver.quit()
# Tutup browser
