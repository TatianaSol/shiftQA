from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options, service=Service('C:/Selenium/chromedriver.exe'))
browser.get("https://demoqa.com/webtables")

delete_button = browser.find_element(By.ID, 'delete-record-3')
delete_button.click()

first_name_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div/div[1]'
last_name_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div/div[2]'
user_age_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div/div[3]'
user_email_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div/div[4]'
salary_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div/div[5]'
department_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[3]/div/div[6]'

assert browser.find_element(By.XPATH, first_name_xpath).text == ' ' and \
       browser.find_element(By.XPATH, last_name_xpath).text == ' ' and \
       browser.find_element(By.XPATH, user_age_xpath).text == ' ' and \
       browser.find_element(By.XPATH, user_email_xpath).text == ' ' and \
       browser.find_element(By.XPATH, salary_xpath).text == ' ' and \
       browser.find_element(By.XPATH, department_xpath).text == ' ', \
       'Ваша запись не удалена'
