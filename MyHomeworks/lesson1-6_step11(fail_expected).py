from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    input1 = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    input3.send_keys("Smolensk")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(3)
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(7)
    browser.quit()