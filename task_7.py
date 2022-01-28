from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options, service=Service('C:/Selenium/chromedriver.exe'))
browser.get("https://demoqa.com/alerts")

alert_button = browser.find_element(By.ID, 'alertButton')
alert_button.click()

alert = browser.switch_to.alert
alert_text = alert.text
sleep(2)
alert.accept()

print('Содержимое сообщения: ', alert_text)
