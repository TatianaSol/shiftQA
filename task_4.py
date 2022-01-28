from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Номер записи, которую будем изменять
edit_id = 2

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options, service=Service('C:/Selenium/chromedriver.exe'))
browser.get("https://demoqa.com/webtables")

edit_button = browser.find_element(By.ID, 'edit-record-%s' % str(edit_id))
edit_button.click()

first_name = 'Tatiana'
last_name = 'Soloshenko'
user_age = 33
user_email = 'soloshka@yandex.ru'
salary = 2000
department = 'Quality Assurance'

form_first_name = browser.find_element(By.ID, 'firstName')
form_first_name.clear()
form_first_name.send_keys(first_name)
form_last_name = browser.find_element(By.ID, 'lastName')
form_last_name.clear()
form_last_name.send_keys(last_name)
form_user_email = browser.find_element(By.ID, 'userEmail')
form_user_email.clear()
form_user_email.send_keys(user_email)
form_user_age = browser.find_element(By.ID, 'age')
form_user_age.clear()
form_user_age.send_keys(user_age)
form_salary = browser.find_element(By.ID, 'salary')
form_salary.clear()
form_salary.send_keys(salary)
form_department = browser.find_element(By.ID, 'department')
form_department.clear()
form_department.send_keys(department)

submit_button = browser.find_element(By.ID, 'submit')
submit_button.click()

first_name_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[%s]/div/div[1]' % str(edit_id)
last_name_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[%s]/div/div[2]' % str(edit_id)
user_age_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[%s]/div/div[3]' % str(edit_id)
user_email_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[%s]/div/div[4]' % str(edit_id)
salary_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[%s]/div/div[5]' % str(edit_id)
department_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[%s]/div/div[6]' % str(edit_id)

assert first_name == str(browser.find_element(By.XPATH, first_name_xpath).text) and \
        last_name == str(browser.find_element(By.XPATH, last_name_xpath).text) and \
        user_age == int(browser.find_element(By.XPATH, user_age_xpath).text) and \
        user_email == str(browser.find_element(By.XPATH, user_email_xpath).text) and \
        salary == int(browser.find_element(By.XPATH, salary_xpath).text) and \
        department == str(browser.find_element(By.XPATH, department_xpath).text), \
        'Ваша запись не изменена'
