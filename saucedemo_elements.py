from selenium.webdriver.common.by import By

url = "https://www.saucedemo.com/"
username =(By.XPATH,"//input[@id='user-name']")
pw = (By.XPATH,"//input[@id='password']")
login = (By.XPATH,"//*[@id='login-button']")
error_massage = (By.XPATH,"//h3[@data-test='error']")
