from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options, service=Service('C:/Selenium/chromedriver.exe'))
browser.get("https://demoqa.com/sortable")

action_chains = ActionChains(browser)

# Перетаскивание 6го элемента на 4ое место по номеру из XPATH (относительная величина)
element = browser.find_element(By.XPATH, '//*[@id="demo-tabpane-list"]/div/div[6]')
target = browser.find_element(By.XPATH, '//*[@id="demo-tabpane-list"]/div/div[4]')
action_chains.drag_and_drop(element, target).perform()


# Метод, который позволяет поменять местами два элемента
def swap_elements(number_one, number_two):
    if number_one < number_two:
        element_one = browser.find_element(By.XPATH, '//*[@id="demo-tabpane-list"]/div/div[%s]' % str(number_one))
        target_one = browser.find_element(By.XPATH, '//*[@id="demo-tabpane-list"]/div/div[%s]' % str(number_two))
        action_chains.drag_and_drop(element_one, target_one).perform()
        element_two = browser.find_element(By.XPATH, '//*[@id="demo-tabpane-list"]/div/div[%s]' % str(number_two - 1))
        target_two = browser.find_element(By.XPATH, '//*[@id="demo-tabpane-list"]/div/div[%s]' % str(number_one))
        action_chains.drag_and_drop(element_two, target_two).perform()
    elif number_one > number_two:
        element_one = browser.find_element(By.XPATH, '//*[@id="demo-tabpane-list"]/div/div[%s]' % str(number_one))
        target_one = browser.find_element(By.XPATH, '//*[@id="demo-tabpane-list"]/div/div[%s]' % str(number_two))
        action_chains.drag_and_drop(element_one, target_one).perform()
        element_two = browser.find_element(By.XPATH, '//*[@id="demo-tabpane-list"]/div/div[%s]' % str(number_two + 1))
        target_two = browser.find_element(By.XPATH, '//*[@id="demo-tabpane-list"]/div/div[%s]' % str(number_one))
        action_chains.drag_and_drop(element_two, target_two).perform()
    else:
        print("Выберите неравные значения")


swap_elements(4, 2)
