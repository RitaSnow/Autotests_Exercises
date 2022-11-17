from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(int(a)+int(b))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    a_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    a = a_element.text
    b_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    b = b_element.text
    x = int(a)+int(b)
    y = calc(x)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()