from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options, service=Service('C:/Selenium/chromedriver.exe'))
browser.get("https://demoqa.com/webtables")

search_key = '2000'

search_box = browser.find_element(By.ID, 'searchBox')
search_box.send_keys(search_key)

first_name_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]'
last_name_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[2]'
user_age_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[3]'
user_email_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[4]'
salary_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[5]'
department_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[6]'

assert search_key in browser.find_element(By.XPATH, first_name_xpath).text  or \
       search_key in browser.find_element(By.XPATH, last_name_xpath).text or \
       search_key in browser.find_element(By.XPATH, user_age_xpath).text or \
       search_key in browser.find_element(By.XPATH, user_email_xpath).text or \
       search_key in browser.find_element(By.XPATH, salary_xpath).text or \
       search_key in browser.find_element(By.XPATH, department_xpath).text, \
       'Нет найденных записей'
