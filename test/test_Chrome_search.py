import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

url1 = "https://www.google.com/"
url2 = "https://github.com/"

def test_chrome_open(browser):
    browser.get(url1)  # открыть страницу
    assert browser.current_url == url1  # проверка открыт поиск


def test_chrome_search_input(browser):
    input = browser.find_element(By.ID, "APjFqb")  # поиск инпута
    input.click()  # установка фокуса
    input.send_keys("вконтакте")  # ввод текста в поиск
    assert (
        input.get_attribute("value") == "вконтакте"
    )  # проверка, что текст присутствует в поле
    input.send_keys(Keys.ENTER)  # нажатие enter
    time.sleep(15)
    assert (
        "%D0%B2%D0%BA%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%B5" in browser.current_url
    )  # проверка что браузерной строке есть вконтакте


def test_open_github(browser):
    browser.get(url2)
    assert browser.current_url == url2