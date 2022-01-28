from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options, service=Service('C:/Selenium/chromedriver.exe'))
browser.get("https://demoqa.com/webtables")


def add_user():
    department_list = ['Insurance', 'Compliance', 'Legal', 'Marketing']

    my_first_name = input('Введите имя из латинских букв: ')
    if re.search(r'^[a-zA-Z]', my_first_name):
        pass
    else:
        print("Поле First Name должно содержать только латинские буквы")
        my_first_name = input('Введите имя из латинских букв: ')

    my_last_name = input('Введите фамилию из латинских букв: ')
    if re.search(r'^[a-zA-Z]', my_last_name):
        pass
    else:
        print("Поле Last Name должно содержать только латинские буквы")
        my_last_name = input('Введите фамилию из латинских букв: ')

    my_user_age = int(input('Введите возраст: '))
    if my_user_age >= 18:
        pass
    else:
        print("Возраст должен быть больше 18")
        my_user_age = int(input('Введите возраст: '))

    my_user_email = input('Введите электронную почту: ')

    my_salary = int(input('Введите размер заработной платы: '))
    if 2000 <= my_salary <= 20000:
        pass
    else:
        print("Зарплата должна быть от 2.000 до 20.000")
        my_salary = int(input('Введите размер заработной платы: '))

    my_department = input('Введите название отдела: Insurance, Compliance, Legal, Marketing: ')
    if my_department in department_list:
        pass
    else:
        print("Такого департамента не существует")
        my_department = input('Введите название отдела: Insurance, Compliance, Legal, Marketing: ')

    add_button = browser.find_element(By.ID, 'addNewRecordButton')
    add_button.click()
    registration_form = browser.find_element(By.CLASS_NAME, 'modal-content')
    registration_form.click()

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

    first_name_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/div[1]/div[2]/div[4]'

    assert my_first_name in browser.find_element(By.XPATH, first_name_xpath).text, 'Ваша запись не добавлена'


add_user()
