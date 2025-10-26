import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()  # подключение к браузеру Хром
    driver.implicitly_wait(10)
    yield driver  # Все что будет после yield будет выполняться после тестов
    driver.close()  # закрытие браузера
