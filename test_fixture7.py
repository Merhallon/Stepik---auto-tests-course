import pytest
import time
import math

from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["236895/step/1", "236896/step/1",
                                  "236897/step/1", "236898/step/1",
                                  "236899/step/1", "236903/step/1",
                                  "236904/step/1", "236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    link = f"https://stepik.org/lesson/{link}"
    browser.get(link)
    browser.implicitly_wait(5)
    a = browser.find_element_by_xpath("//textarea[@placeholder='Напишите ваш ответ здесь...']")
    answer = math.log(int(time.time()))
    a.send_keys(str(answer))
    browser.find_element_by_xpath("//button[@class='submit-submission']").click()
    massage = browser.find_element_by_xpath("//pre[@class='smart-hints__hint']")
    assert massage.text in "Correct!", "Значения разные"

    time.sleep(2)


