"""
Настройки для всех тестов
Здесь создается браузер Firefox для каждого теста
"""
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import os


@pytest.fixture(scope="function")
def driver():
    """
    Создает браузер Firefox для теста
    После теста автоматически закрывает браузер
    """
    # Настройки Firefox
    options = Options()

    # Путь к локальному geckodriver
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    geckodriver_path = os.path.join(project_root, "drivers", "geckodriver")

    # Создаем браузер с локальным geckodriver
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)

    # Ждем элементы максимум 10 секунд
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Передаем браузер в тест
    yield driver

    # Закрываем браузер после теста
    driver.quit()
