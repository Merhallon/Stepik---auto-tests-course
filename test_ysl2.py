import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMail():
    def test_second(self, browser):
        link = "https://www.gosuslugi.ru/situation/obtaining_drivers_license_first_time"
        browser.get(link)
        browser.implicitly_wait(20)

        button = browser.find_element_by_css_selector('[href="http://www.gibdd.ru/"]')
        ActionChains(browser).move_to_element(button).perform()
        button.click()
        time.sleep(10)

        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        button1 = browser.find_element_by_css_selector('[href="/banners/redirect?bid=4"]')
        ActionChains(browser).move_to_element(button1).perform()
        button1.click()
        time.sleep(10)

        new_window = browser.window_handles[2]
        browser.switch_to.window(new_window)
        input1 = browser.find_element_by_css_selector('#menu-1 > li:nth-child(1)')
        input1.click()
        browser.find_element_by_css_selector('[href="/mvd/documents"]').click()
        time.sleep(10)
        button1 = browser.find_element_by_css_selector('[ href="/mvd/documents/other-docs"]')
        ActionChains(browser).move_to_element(button1).perform()
        button1.click()
        time.sleep(10)
        browser.find_element_by_class_name('[href="https://media.mvd.ru/files/application/1493272"]').click()
        #browser.set_preference("pdfjs.disabled", True)


    # pytest -s -v test_2.py
