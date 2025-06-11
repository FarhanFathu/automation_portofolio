from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.get("https://the-internet.herokuapp.com/login")

original_tab = driver.current_window_handle


driver.find_element(By.LINK_TEXT,"Elemental Selenium").click()

WebDriverWait(driver,10).until(EC.number_of_windows_to_be(2))
tabs = driver.window_handles

for tab in tabs :
    if tab != original_tab:
        driver.switch_to.window(tab)
        break

try:
    WebDriverWait(driver,5).until(EC.url_contains("elementalselenium.com"))
    print("LOGIN BERHASIL")
except:
    print("GAGALLLLL")


input("TUNGGU SAMPAI ENTER....")

driver.quit()

