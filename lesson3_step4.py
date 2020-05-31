import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()

    browser.get(link)

    first_button = browser.find_element_by_css_selector("button.btn")
    first_button.click()

    confirm = browser.switch_to_alert()
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(10)

    answ = browser.switch_to_alert().text
    print(answ)

finally:

    browser.quit()