from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


# Setup driver secara otomatis
chrome_options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

# Buka situs
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID,"username").send_keys("xerosss1")
pw = driver.find_element(By.ID,"password").send_keys("1234556")

time.sleep(3)

login = driver.find_element(By.CSS_SELECTOR,".radius").click()

flash = driver.find_element(By.ID,"flash").text
print("FLASH NYA : "+flash)

input("Tekan Enter untuk menutup browser...")

driver.quit()
# Tutup browser
