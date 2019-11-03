from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x2_element = browser.find_element_by_id("input_value")
    x2 = x2_element.text
    y = calc(x2)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()
    # Отправляем заполненную форму


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
