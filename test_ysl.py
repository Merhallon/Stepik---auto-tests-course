import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

link = "https://www.gosuslugi.ru/new"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMail():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.implicitly_wait(20)
        button2 = browser.find_element_by_css_selector(".main-app-logo")
        button2.click()
        input1 = browser.find_element_by_xpath("//*[@id='_epgu_el2']/div/input")  # находим поисковую строку
        input1.send_keys("загран")

        browser.find_element_by_xpath("//*[text()='загранпаспорт нового поколения 18 лет']").click()

        button = browser.find_element_by_xpath("//*[text()=' гражданином Российской Федерации достигшим ']")
        ActionChains(browser).move_to_element(button).perform()  # скролим до  нужного элемента
        button.click()

        button2 = browser.find_element_by_css_selector(".btn-sec.larr_svg")  # кнопка вернуться
        button2.click()
        button3 = browser.find_element_by_css_selector(".btn-sec.small.larr_svg")  # кнопка вернутся
        button3.click()
        button4 = browser.find_element_by_css_selector(".btn-sec.small.larr")  # кнопка вернуться в каталог
        button4.click()

        massage = browser.find_element_by_css_selector(".h1.offset-top-none")
        assert massage.text in "Каталог госуслуг", "Значения разные"  # проверка отображения каталог госуслуг


#pytest -s -v test_ysl.py
