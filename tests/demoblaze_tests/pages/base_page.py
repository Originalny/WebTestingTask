from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    """Базовый класс для всех Page Objects"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть URL: {url}")
    def open_url(self, url):
        """Открыть страницу по URL"""
        self.driver.get(url)

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator, timeout=10):
        """Найти элемент на странице"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Найти кликабельный элемент: {locator}")
    def find_clickable_element(self, locator, timeout=10):
        """Найти кликабельный элемент"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Кликнуть по элементу: {locator}")
    def click_element(self, locator, timeout=10):
        """Кликнуть по элементу"""
        element = self.find_clickable_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def input_text(self, locator, text, timeout=10):
        """Ввести текст в поле"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator, timeout=10):
        """Получить текст элемента"""
        element = self.find_element(locator, timeout)
        return element.text

    @allure.step("Проверить видимость элемента: {locator}")
    def is_element_visible(self, locator, timeout=10):
        """Проверить, виден ли элемент"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Ждать появления алерта")
    def wait_for_alert(self, timeout=10):
        """Ждать появления alert"""
        return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())

    @allure.step("Получить текст alert и принять его")
    def get_alert_text_and_accept(self):
        """Получить текст из alert и закрыть его"""
        alert = self.wait_for_alert()
        alert_text = alert.text
        allure.attach(alert_text, name="Текст alert", attachment_type=allure.attachment_type.TEXT)
        alert.accept()
        return alert_text

    @allure.step("Ждать исчезновения элемента: {locator}")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        """Ждать, пока элемент исчезнет"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Сделать скриншот")
    def take_screenshot(self, name="screenshot"):
        """Сделать скриншот текущей страницы"""
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
        return screenshot
