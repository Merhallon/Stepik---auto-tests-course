from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element_by_id("num1")
    x1 = x1_element.text
    x2_element = browser.find_element_by_id("num2")
    x2 = x2_element.text
    y = str(int(x1)+int(x2))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
