from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options, service=Service('C:/Selenium/chromedriver.exe'))
browser.get("https://demoqa.com/browser-windows")

main_window = browser.current_window_handle
main_window_title_1 = main_window.title
new_tab = browser.find_element(By.ID, 'tabButton')
new_tab.click()
browser.switch_to.window(browser.window_handles[1])
browser.close()
browser.switch_to.window(main_window)
main_window_title_2 = main_window.title

assert main_window_title_1 == main_window_title_2, 'Названия вкладок не совпадают'

print('Список доступных кнопок: ')
for button in browser.find_elements(By.ID, 'browserWindows'):
    if button.is_enabled() is True:
        print(button.text)
