from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button2 = browser.find_element_by_id("book")
button2.click()

x2_element = browser.find_element_by_id("input_value")
x2 = x2_element.text
y = calc(x2)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

button1 = browser.find_element_by_id("solve")
button1.click()

time.sleep(10)
browser.quit()



