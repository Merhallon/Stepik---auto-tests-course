from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element_by_id("input_value")
    x1 = x1_element.text
    y = calc(x1)

    browser.execute_script("window.scrollBy(0, 100);")

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option = browser.find_element_by_id("robotCheckbox")
    option.click()

    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    button = browser.find_element_by_tag_name("button")
    button.click()
    # Отправляем заполненную форму


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
