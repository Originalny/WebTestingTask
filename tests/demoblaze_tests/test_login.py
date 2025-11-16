import pytest
import allure
from .pages.main_page import MainPage
from .utils.config import Config


@allure.feature('Аутентификация')
@allure.story('Вход в систему (Login)')
class TestLogin:
    """Тесты функциональности логина"""

    @allure.title("Успешный вход с корректными учетными данными")
    @allure.description("""
    ЦЕЛЬ: Проверить, что пользователь может успешно войти в систему с корректными данными

    ПРЕДУСЛОВИЯ:
    - Пользователь зарегистрирован в системе
    - Используются корректные username и password

    ШАГИ:
    1. Открыть главную страницу demoblaze.com
    2. Кликнуть на ссылку "Log in"
    3. Ввести корректный username
    4. Ввести корректный password
    5. Нажать кнопку "Log in"

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Модальное окно логина закрывается
    - Отображается имя пользователя в навигации
    - Появляется кнопка "Log out"
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_successful_login(self, driver):
        """Проверка успешного входа с корректными данными"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Выполнить логин с корректными данными"):
            # ВАЖНО: Перед запуском теста создайте пользователя с этими данными
            # или измените Config.VALID_USERNAME и Config.VALID_PASSWORD
            page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        with allure.step("Проверить, что пользователь успешно залогинен"):
            assert page.is_user_logged_in(), "Пользователь не залогинен - элемент с именем не отображается"

        with allure.step("Проверить отображаемое имя пользователя"):
            displayed_username = page.get_logged_in_username()
            allure.attach(
                f"Ожидаемый username: {Config.VALID_USERNAME}\nОтображаемый: {displayed_username}",
                name="Сравнение username",
                attachment_type=allure.attachment_type.TEXT
            )
            assert displayed_username == Config.VALID_USERNAME, \
                f"Отображается неверное имя пользователя: {displayed_username}"

        with allure.step("Сделать скриншот успешного входа"):
            page.take_screenshot("successful_login")


    @allure.title("Вход с некорректным логином")
    @allure.description("""
    ЦЕЛЬ: Проверить, что система корректно обрабатывает попытку входа с несуществующим username

    ШАГИ:
    1. Открыть главную страницу
    2. Открыть модальное окно логина
    3. Ввести несуществующий username
    4. Ввести любой password
    5. Нажать кнопку "Log in"

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Появляется alert с сообщением об ошибке "User does not exist."
    - Пользователь не залогинен
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_login_with_invalid_username(self, driver):
        """Проверка входа с несуществующим username"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Попытаться войти с некорректным username"):
            invalid_username = "nonexistent_user_12345"
            page.login(invalid_username, "anypassword")

        with allure.step("Проверить появление alert с ошибкой"):
            alert_text = page.get_alert_text_and_accept()
            allure.attach(alert_text, name="Текст ошибки", attachment_type=allure.attachment_type.TEXT)
            assert "User does not exist" in alert_text, \
                f"Ожидали сообщение 'User does not exist', получили: {alert_text}"

        with allure.step("Проверить, что пользователь не залогинен"):
            assert not page.is_user_logged_in(), \
                "Пользователь залогинен, хотя не должен был"


    @allure.title("Вход с некорректным паролем")
    @allure.description("""
    ЦЕЛЬ: Проверить, что система корректно обрабатывает попытку входа с неправильным паролем

    ШАГИ:
    1. Открыть главную страницу
    2. Открыть модальное окно логина
    3. Ввести корректный username
    4. Ввести неправильный password
    5. Нажать кнопку "Log in"

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Появляется alert с сообщением об ошибке "Wrong password."
    - Пользователь не залогинен
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_login_with_wrong_password(self, driver):
        """Проверка входа с неправильным паролем"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Попытаться войти с неправильным паролем"):
            page.login(Config.VALID_USERNAME, "wrong_password_123")

        with allure.step("Проверить появление alert с ошибкой"):
            alert_text = page.get_alert_text_and_accept()
            allure.attach(alert_text, name="Текст ошибки", attachment_type=allure.attachment_type.TEXT)
            assert "Wrong password" in alert_text, \
                f"Ожидали сообщение 'Wrong password', получили: {alert_text}"

        with allure.step("Проверить, что пользователь не залогинен"):
            assert not page.is_user_logged_in(), \
                "Пользователь залогинен, хотя не должен был"


    @allure.title("Вход с пустыми полями")
    @allure.description("""
    ЦЕЛЬ: Проверить обработку попытки входа с незаполненными полями

    ШАГИ:
    1. Открыть главную страницу
    2. Открыть модальное окно логина
    3. Оставить поля username и password пустыми
    4. Нажать кнопку "Log in"

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Появляется alert с сообщением об ошибке
    - Пользователь не залогинен
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_login_with_empty_fields(self, driver):
        """Проверка входа с пустыми полями"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Попытаться войти с пустыми полями"):
            page.login("", "")

        with allure.step("Проверить появление alert"):
            alert_text = page.get_alert_text_and_accept()
            allure.attach(alert_text, name="Текст ошибки", attachment_type=allure.attachment_type.TEXT)
            # Система может показывать разные сообщения для пустых полей
            assert alert_text != "", "Alert должен содержать сообщение об ошибке"

        with allure.step("Проверить, что пользователь не залогинен"):
            assert not page.is_user_logged_in(), \
                "Пользователь залогинен, хотя не должен был"

        with allure.step("Сделать скриншот"):
            page.take_screenshot("login_empty_fields")


    @allure.title("Проверка Logout")
    @allure.description("""
    ЦЕЛЬ: Проверить, что пользователь может успешно выйти из системы

    ШАГИ:
    1. Войти в систему
    2. Нажать кнопку "Log out"

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Имя пользователя исчезает из навигации
    - Появляется кнопка "Log in"
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_logout(self, driver):
        """Проверка выхода из системы"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу и войти в систему"):
            page.open()
            page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)

        with allure.step("Проверить, что пользователь залогинен"):
            assert page.is_user_logged_in(), "Пользователь должен быть залогинен"

        with allure.step("Выполнить logout"):
            page.logout()

        with allure.step("Проверить, что пользователь разлогинен"):
            is_logged_in = page.is_user_logged_in()
            assert not is_logged_in, "Пользователь все еще залогинен после logout"

        with allure.step("Сделать скриншот"):
            page.take_screenshot("after_logout")
