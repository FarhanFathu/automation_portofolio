from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


chrome_options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.get("https://www.google.com")

search = driver.find_element(By.NAME,"q").send_keys("Youtube")



time.sleep(5)

input("WAIT FOR...")

driver.quit()
