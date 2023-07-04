from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://www.saucedemo.com/')
time.sleep(2)

username = driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
time.sleep(2)
password = driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
time.sleep(2)
send = driver.find_element(By.CSS_SELECTOR, '#login-button').click()

time.sleep(2)
driver.quit()
