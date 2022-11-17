from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(c):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    c = math.log(abs(12*math.sin(int(x))))
    y = calc(c)

    browser.execute_script("window.scrollBy(0, 150);")

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    robot1 = browser.find_element(By.ID, "robotCheckbox")
    robot1.click()
    robot2 = browser.find_element(By.ID, "robotsRule")
    robot2.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()