from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options, service=Service('C:/Selenium/chromedriver.exe'))
browser.get("https://demoqa.com/upload-download")

app_dir = os.path.dirname(__file__)
default_file_path = os.path.join(app_dir, "thisisyourfile.txt")
default_file_name = default_file_path.split('\\')[-1]
upload_file = browser.find_element(By.ID, 'uploadFile')
upload_file.send_keys(default_file_path)
result_file_path = browser.find_element(By.ID, 'uploadedFilePath')
uploaded_file_name = result_file_path.text.split('\\')[-1]

assert default_file_name == uploaded_file_name, 'Имена файлов не совпадают'
