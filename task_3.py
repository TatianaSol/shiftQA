from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import re
import random

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options, service=Service('C:/Selenium/chromedriver.exe'))
browser.get("https://demoqa.com/webtables")

department_list = ['Insurance', 'Compliance', 'Legal', 'Marketing']
first_name_list = ['Helen', 'Anton', 'Eugene', 'Sam', 'Ann']
last_name_list = ['Smith', 'Clark', 'Jones', 'Howard', 'Donald']

my_first_name = 'Tatiana'
my_last_name = 'Soloshenko'
my_user_age = 33
my_user_email = 'soloshka@yandex.ru'
my_salary = 3000
my_department = 'Insurance'

assert re.search(r'^[a-zA-Z]', my_first_name), 'Поле First Name должно содержать только латинские буквы'
assert re.search(r'^[a-zA-Z]', my_last_name), 'Поле Last Name должно содержать только латинские буквы'
assert my_user_age >= 18, 'Возраст должен быть больше 18'
assert 2000 <= my_salary <= 20000, 'Зарплата должна быть от 2.000 до 20.000'
assert my_department in department_list, 'Такого департамента не существует'

add_button = browser.find_element(By.ID, 'addNewRecordButton')
add_button.click()

form_first_name = browser.find_element(By.ID, 'firstName')
form_first_name.send_keys(my_first_name)
form_last_name = browser.find_element(By.ID, 'lastName')
form_last_name.send_keys(my_last_name)
form_user_email = browser.find_element(By.ID, 'userEmail')
form_user_email.send_keys(my_user_email)
form_user_age = browser.find_element(By.ID, 'age')
form_user_age.send_keys(my_user_age)
form_salary = browser.find_element(By.ID, 'salary')
form_salary.send_keys(my_salary)
form_department = browser.find_element(By.ID, 'department')
form_department.send_keys(my_department)
submit_button = browser.find_element(By.ID, 'submit')
submit_button.click()

first_name_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[4]/div/div[1]'
last_name_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[4]/div/div[2]'
user_age_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[4]/div/div[3]'
user_email_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[4]/div/div[4]'
salary_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[4]/div/div[5]'
department_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[4]/div/div[6]'

assert my_first_name == str(browser.find_element(By.XPATH, first_name_xpath).text) and \
        my_last_name == str(browser.find_element(By.XPATH, last_name_xpath).text) and \
        my_user_age == int(browser.find_element(By.XPATH, user_age_xpath).text) and \
        my_user_email == str(browser.find_element(By.XPATH, user_email_xpath).text) and \
        my_salary == int(browser.find_element(By.XPATH, salary_xpath).text) and \
        my_department == str(browser.find_element(By.XPATH, department_xpath).text), \
        'Ваша запись не добавлена'

select_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/span[2]/select'
select = Select(browser.find_element(By.XPATH, select_xpath))
select.select_by_value('5')

total_pages_1 = browser.find_element(By.CLASS_NAME, '-totalPages').text

for i in range(10):

    add_button = browser.find_element(By.ID, 'addNewRecordButton')
    add_button.click()

    first_name = random.choice(first_name_list)
    last_name = random.choice(last_name_list)
    department = random.choice(department_list)
    user_age = random.randint(18, 99)
    salary = random.randint(2000, 20000)
    user_email = first_name + '.' + last_name + '@mail.com'

    form_first_name = browser.find_element(By.ID, 'firstName')
    form_first_name.send_keys(first_name)
    form_last_name = browser.find_element(By.ID, 'lastName')
    form_last_name.send_keys(last_name)
    form_user_email = browser.find_element(By.ID, 'userEmail')
    form_user_email.send_keys(user_email)
    form_user_age = browser.find_element(By.ID, 'age')
    form_user_age.send_keys(user_age)
    form_salary = browser.find_element(By.ID, 'salary')
    form_salary.send_keys(salary)
    form_department = browser.find_element(By.ID, 'department')
    form_department.send_keys(department)
    submit_button = browser.find_element(By.ID, 'submit')
    submit_button.click()

total_pages_2 = browser.find_element(By.CLASS_NAME, '-totalPages').text

assert total_pages_1 != total_pages_2, 'Количество страниц не изменилось'

current_page_1_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/span[1]/div/input'
current_page_1 = browser.find_element(By.XPATH, current_page_1_xpath).get_attribute("value")

next_button_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[3]/button'
next_button = browser.find_element(By.XPATH, next_button_xpath)
next_button.click()

current_page_2_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/span[1]/div/input'
current_page_2 = browser.find_element(By.XPATH, current_page_2_xpath).get_attribute("value")

assert current_page_1 != current_page_2, 'Переход на следующую страницу не произошел'
