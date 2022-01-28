from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options, service=Service('C:/Selenium/chromedriver.exe'))
browser.get("https://demoqa.com/dynamic-properties")

enable_after = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "enableAfter")))
enable_after.click()
visible_after = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "visibleAfter")))
visible_after.click()


# Фунция опрашивает систему в течение указанного времени, либо до тех пор, пока кнопка не нажата
def waiting_for_element(element_id, timeout):
    delay = 60 * timeout
    close_time = time.time() + delay
    while True:
        your_button = browser.find_element(By.ID, element_id)
        your_button.click()
        if your_button.is_enabled():
            break
        elif time.time() > close_time:
            break


# Время указывается в секундах
waiting_for_element('enableAfter', 15)
