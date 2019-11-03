from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os
try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[placeholder='Enter first name']")
    input1.send_keys("kdk")

    input1 = browser.find_element_by_css_selector("[placeholder='Enter last name']")
    input1.send_keys("g")

    input1 = browser.find_element_by_css_selector("[placeholder='Enter email']")
    input1.send_keys("kdk@mai.ru")

    input3 = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'h.txt')           # добавляем к этому пути имя файла
    input3.send_keys(file_path)

    button = browser.find_element_by_class_name("btn")
    button.click()
    # Отправляем заполненную форму


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
