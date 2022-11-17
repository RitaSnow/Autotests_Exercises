from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element(By.XPATH, '//input[@placeholder="Enter first name"]')
    input1.send_keys("Nanana")
    input2 = browser.find_element(By.XPATH, '//input[@placeholder="Enter last name"]')
    input2.send_keys("Nananana")
    input3 = browser.find_element(By.XPATH, '//input[@placeholder="Enter email"]')
    input3.send_keys("Nananananana")

    current_dir = os.path.abspath(os.path.dirname('__file__'))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()