from selenium import webdriver
import unittest
import time


class TestAbs(unittest.TestCase):

    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block > .form-group.first_class input:nth-child(2)")
        first_name.send_keys("Bla")
        last_name = browser.find_element_by_css_selector(".first_block > .form-group.second_class input:nth-child(2)")
        last_name.send_keys("Bla")
        email = browser.find_element_by_css_selector(".first_block > .form-group.third_class input:nth-child(2)")
        email.send_keys("bla@bla.bla")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,  "phrases do not match")

        browser.quit()

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block > .form-group.first_class input:nth-child(2)")
        first_name.send_keys("Bla")
        last_name = browser.find_element_by_css_selector(".first_block > .form-group.second_class input:nth-child(2)")
        last_name.send_keys("Bla")
        email = browser.find_element_by_css_selector(".first_block > .form-group.third_class input:nth-child(2)")
        email.send_keys("bla@bla.bla")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,  "phrases do not match")

        browser.quit()


if __name__ == "__main__":
    unittest.main()
