from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage
import time


class MainPage(BasePage):
    """Главная страница сайта demoblaze.com"""

    # Локаторы для навигации
    LOGIN_LINK = (By.ID, "login2")
    SIGNUP_LINK = (By.ID, "signin2")
    LOGOUT_LINK = (By.ID, "logout2")
    USERNAME_DISPLAY = (By.ID, "nameofuser")

    # Локаторы для модального окна логина
    LOGIN_MODAL = (By.ID, "logInModal")
    LOGIN_USERNAME_INPUT = (By.ID, "loginusername")
    LOGIN_PASSWORD_INPUT = (By.ID, "loginpassword")
    LOGIN_BUTTON = (By.XPATH, "//button[@onclick='logIn()']")
    LOGIN_CLOSE_BUTTON = (By.XPATH, "//div[@id='logInModal']//button[@class='close']")

    # Локаторы для модального окна регистрации
    SIGNUP_MODAL = (By.ID, "signInModal")
    SIGNUP_USERNAME_INPUT = (By.ID, "sign-username")
    SIGNUP_PASSWORD_INPUT = (By.ID, "sign-password")
    SIGNUP_BUTTON = (By.XPATH, "//button[@onclick='register()']")
    SIGNUP_CLOSE_BUTTON = (By.XPATH, "//div[@id='signInModal']//button[@class='close']")

    # Локаторы для категорий
    CATEGORY_PHONES_LINK = (By.XPATH, "//a[@onclick=\"byCat('phone')\"]")
    CATEGORY_LAPTOPS_LINK = (By.XPATH, "//a[@onclick=\"byCat('notebook')\"]")
    CATEGORY_MONITORS_LINK = (By.XPATH, "//a[@onclick=\"byCat('monitor')\"]")

    # Локаторы для товаров
    PRODUCT_CARDS = (By.XPATH, "//div[@id='tbodyid']/div")
    PRODUCT_TITLES = (By.XPATH, "//div[@id='tbodyid']//h4/a")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.demoblaze.com/"

    @allure.step("Открыть главную страницу")
    def open(self):
        """Открыть главную страницу"""
        self.open_url(self.url)

    # ========== МЕТОДЫ ДЛЯ ЛОГИНА ==========

    @allure.step("Открыть модальное окно логина")
    def open_login_modal(self):
        """Кликнуть на ссылку Log in"""
        self.click_element(self.LOGIN_LINK)
        time.sleep(1)  # Даем время модальному окну открыться

    @allure.step("Ввести данные для логина: username={username}")
    def enter_login_credentials(self, username, password):
        """Ввести username и password в форму логина"""
        self.input_text(self.LOGIN_USERNAME_INPUT, username)
        self.input_text(self.LOGIN_PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку Log in")
    def click_login_button(self):
        """Нажать кнопку Log in в модальном окне"""
        self.click_element(self.LOGIN_BUTTON)
        time.sleep(1)  # Даем время на обработку

    @allure.step("Выполнить логин: username={username}")
    def login(self, username, password):
        """Полный процесс логина"""
        self.open_login_modal()
        self.enter_login_credentials(username, password)
        self.click_login_button()

    @allure.step("Проверить, что пользователь залогинен")
    def is_user_logged_in(self):
        """Проверить, виден ли элемент с именем пользователя"""
        return self.is_element_visible(self.USERNAME_DISPLAY, timeout=5)

    @allure.step("Получить имя залогиненного пользователя")
    def get_logged_in_username(self):
        """Получить отображаемое имя пользователя"""
        text = self.get_text(self.USERNAME_DISPLAY)
        # Текст в формате "Welcome username"
        return text.replace("Welcome ", "").strip()

    @allure.step("Выполнить logout")
    def logout(self):
        """Выйти из системы"""
        self.click_element(self.LOGOUT_LINK)
        time.sleep(1)

    # ========== МЕТОДЫ ДЛЯ РЕГИСТРАЦИИ ==========

    @allure.step("Открыть модальное окно регистрации")
    def open_signup_modal(self):
        """Кликнуть на ссылку Sign up"""
        self.click_element(self.SIGNUP_LINK)
        time.sleep(1)  # Даем время модальному окну открыться

    @allure.step("Ввести данные для регистрации: username={username}")
    def enter_signup_credentials(self, username, password):
        """Ввести username и password в форму регистрации"""
        self.input_text(self.SIGNUP_USERNAME_INPUT, username)
        self.input_text(self.SIGNUP_PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку Sign up")
    def click_signup_button(self):
        """Нажать кнопку Sign up в модальном окне"""
        self.click_element(self.SIGNUP_BUTTON)
        time.sleep(1)  # Даем время на обработку

    @allure.step("Выполнить регистрацию: username={username}")
    def signup(self, username, password):
        """Полный процесс регистрации"""
        self.open_signup_modal()
        self.enter_signup_credentials(username, password)
        self.click_signup_button()

    @allure.step("Ждать закрытия модального окна регистрации")
    def wait_for_signup_modal_to_close(self):
        """Ждать, пока модальное окно регистрации закроется"""
        self.wait_for_element_to_disappear(self.SIGNUP_MODAL, timeout=10)

    # ========== МЕТОДЫ ДЛЯ КАТЕГОРИЙ ==========

    @allure.step("Кликнуть по категории Phones")
    def click_phones_category(self):
        """Выбрать категорию Phones"""
        self.click_element(self.CATEGORY_PHONES_LINK)
        time.sleep(2)  # Даем время на загрузку товаров

    @allure.step("Кликнуть по категории Laptops")
    def click_laptops_category(self):
        """Выбрать категорию Laptops"""
        self.click_element(self.CATEGORY_LAPTOPS_LINK)
        time.sleep(2)  # Даем время на загрузку товаров

    @allure.step("Кликнуть по категории Monitors")
    def click_monitors_category(self):
        """Выбрать категорию Monitors"""
        self.click_element(self.CATEGORY_MONITORS_LINK)
        time.sleep(2)  # Даем время на загрузку товаров

    @allure.step("Получить количество отображаемых товаров")
    def get_product_count(self):
        """Получить количество карточек товаров на странице"""
        products = self.driver.find_elements(*self.PRODUCT_CARDS)
        count = len(products)
        allure.attach(str(count), name="Количество товаров", attachment_type=allure.attachment_type.TEXT)
        return count

    @allure.step("Получить названия всех товаров")
    def get_product_titles(self):
        """Получить список названий всех отображаемых товаров"""
        time.sleep(1)  # Даем время на загрузку
        title_elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        titles = [element.text for element in title_elements]
        allure.attach("\n".join(titles), name="Названия товаров", attachment_type=allure.attachment_type.TEXT)
        return titles

    @allure.step("Проверить, что все товары содержат ключевое слово: {keyword}")
    def check_products_contain_keyword(self, keyword):
        """Проверить, что названия товаров содержат определенное ключевое слово"""
        titles = self.get_product_titles()
        # Преобразуем ключевое слово и названия в нижний регистр для проверки
        keyword_lower = keyword.lower()
        matching_products = [title for title in titles if keyword_lower in title.lower()]

        result = {
            "total": len(titles),
            "matching": len(matching_products),
            "titles": titles,
            "matching_titles": matching_products
        }

        allure.attach(
            f"Всего товаров: {result['total']}\nСодержат '{keyword}': {result['matching']}",
            name="Результаты проверки",
            attachment_type=allure.attachment_type.TEXT
        )

        return result
