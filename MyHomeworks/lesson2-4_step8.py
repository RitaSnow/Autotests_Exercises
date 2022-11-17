from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(c):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = WebDriverWait(browser, 1).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    c = math.log(abs(12 * math.sin(int(x))))
    y = calc(c)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(10)
    browser.quit()