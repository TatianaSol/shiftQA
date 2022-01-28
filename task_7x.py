from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options, service=Service('C:/Selenium/chromedriver.exe'))
browser.get("https://demoqa.com/alerts")

alert_button = browser.find_element(By.ID, 'alertButton')
alert_button.click()
alert = browser.switch_to.alert
alert_text_1 = alert.text
alert.accept()
print('Содержимое сообщения 1:', alert_text_1)

timer_alert_button = browser.find_element(By.ID, 'timerAlertButton')
timer_alert_button.click()
try:
    WebDriverWait(browser, 6).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert_text_2 = alert.text
    alert.accept()
    print('Содержимое сообщения 2:', alert_text_2)
except TimeoutException:
    print('Нет всплывающего окна')

confirm_button = browser.find_element(By.ID, 'confirmButton')
confirm_button.click()
alert = browser.switch_to.alert
alert.accept()
alert_text_3_ok = browser.find_element(By.ID, 'confirmResult').text
print('Содержимое сообщения 3 при согласии:', alert_text_3_ok)

confirm_button = browser.find_element(By.ID, 'confirmButton')
confirm_button.click()
alert = browser.switch_to.alert
alert.dismiss()
alert_text_3_no = browser.find_element(By.ID, 'confirmResult').text
print('Содержимое сообщения 3 при отмене:', alert_text_3_no)

confirm_button = browser.find_element(By.ID, 'promtButton')
confirm_button.click()
alert = browser.switch_to.alert
alert.send_keys('Sierra')
alert.accept()
alert_text_4 = browser.find_element(By.ID, 'promptResult').text
print('Содержимое сообщения 4:', alert_text_4)
