from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://the-internet.herokuapp.com/')
action = ActionChains(driver)
time.sleep(3)

#Check boxes
driver.get('https://the-internet.herokuapp.com/checkboxes')
time.sleep(2)
box1 = driver.find_element(By.CSS_SELECTOR, '#checkboxes > input:nth-child(1)').click()
time.sleep(2)
box2 = driver.find_element(By.CSS_SELECTOR, '#checkboxes > input:nth-child(3)').click()
time.sleep(2)

driver.back()

#Context Menu
time.sleep(3)
driver.get('https://the-internet.herokuapp.com/context_menu')
source = driver.find_element(By.XPATH, '//*[@id="hot-spot"]')
action = ActionChains(driver)
time.sleep(2)
action.context_click(source).perform()
alert = driver.switch_to.alert
time.sleep(1)
alert.accept()
time.sleep(2)

driver.back()

#Dropdown List
time.sleep(3)
driver.get('https://the-internet.herokuapp.com/dropdown')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#dropdown').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#dropdown > option:nth-child(3)').click()
time.sleep(2)

driver.back()

#Dynamic Content
time.sleep(3)
driver.get('https://the-internet.herokuapp.com/dynamic_content?with_content=static')
time.sleep(2)
cont = 0
while cont < 2:
    driver.refresh()
    cont += 1
    time.sleep(2)

driver.back()

#Horizontal Slider
time.sleep(3)
driver.get('https://the-internet.herokuapp.com/horizontal_slider')
time.sleep(2)
element = driver.find_element(By.CSS_SELECTOR, '.sliderContainer > input:nth-child(1)')
action = ActionChains(driver)
action.drag_and_drop_by_offset(element, 5, 0).perform()
time.sleep(2)

driver.back()

#Hovers
time.sleep(3)
driver.get('https://the-internet.herokuapp.com/hovers')
time.sleep(2)
element1 = driver.find_element(By.CSS_SELECTOR, 'div.figure:nth-child(3)')
action.move_to_element(element1).perform()
time.sleep(2)
element2 = element1.find_element(By.XPATH, 'following-sibling::*[1]')
action.move_to_element(element2).perform()
time.sleep(2)
element3 = element2.find_element(By.XPATH, 'following-sibling::*[1]')
action.move_to_element(element3).perform()
time.sleep(2)

driver.back()

#Key Presses
time.sleep(3)
driver.get('https://the-internet.herokuapp.com/key_presses')
time.sleep(2)
action.send_keys(Keys.TAB).perform()
time.sleep(2)
action.send_keys(Keys.SPACE).perform()
time.sleep(2)

driver.back()

time.sleep(3)
driver.quit()
