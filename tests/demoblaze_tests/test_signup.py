import pytest
import allure
from .pages.main_page import MainPage
from .utils.config import Config


@allure.feature('Аутентификация')
@allure.story('Регистрация (Sign up)')
class TestSignup:
    """Тесты функциональности регистрации"""

    @allure.title("Успешная регистрация новой учетной записи")
    @allure.description("""
    ЦЕЛЬ: Проверить, что новая учетная запись может быть успешно зарегистрирована

    ШАГИ:
    1. Открыть главную страницу demoblaze.com
    2. Кликнуть на ссылку "Sign up"
    3. Ввести уникальный username (генерируется автоматически)
    4. Ввести password
    5. Нажать кнопку "Sign up"

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Появляется alert с сообщением "Sign up successful."
    - Модальное окно регистрации закрывается
    - Пользователь может войти с этими данными
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_successful_signup(self, driver):
        """Проверка успешной регистрации новой учетной записи"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Подготовить учетные данные для регистрации"):
            new_username = Config.generate_random_username()
            new_password = Config.generate_random_password()
            allure.attach(
                f"Username: {new_username}\nPassword: {new_password}",
                name="Учетные данные для регистрации",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Выполнить регистрацию"):
            page.signup(new_username, new_password)

        with allure.step("Проверить успешное сообщение о регистрации"):
            alert_text = page.get_alert_text_and_accept()
            allure.attach(alert_text, name="Текст alert", attachment_type=allure.attachment_type.TEXT)
            assert "Sign up successful" in alert_text, \
                f"Ожидали 'Sign up successful', получили: {alert_text}"

        with allure.step("Проверить возможность входа с новыми данными"):
            page.login(new_username, new_password)
            assert page.is_user_logged_in(), \
                "Не удалось войти с только что зарегистрированными данными"

        with allure.step("Проверить отображаемое имя пользователя"):
            displayed_username = page.get_logged_in_username()
            assert displayed_username == new_username, \
                f"Отображается неверное имя: {displayed_username}"

        with allure.step("Сделать скриншот успешной регистрации"):
            page.take_screenshot("successful_signup")


    @allure.title("Повторная регистрация с существующим логином")
    @allure.description("""
    ЦЕЛЬ: Проверить, что повторная регистрация с уже существующим логином
          выдаёт соответствующее сообщение об ошибке

    ШАГИ:
    1. Открыть главную страницу
    2. Попытаться зарегистрировать пользователя с уже существующим username (user123)

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Появляется alert с сообщением "This user already exist."
    - Новая учетная запись не создается

    ПРИМЕЧАНИЕ: Использует существующего пользователя user123
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_signup_with_existing_username(self, driver):
        """Проверка регистрации с уже существующим логином"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Попытаться зарегистрировать пользователя с существующим username"):
            # Используем существующего пользователя user123
            username = Config.EXISTING_USERNAME
            password = "anypassword123"
            allure.attach(
                f"Username: {username}\nPassword: {password}",
                name="Данные для попытки регистрации",
                attachment_type=allure.attachment_type.TEXT
            )
            page.signup(username, password)

        with allure.step("Проверить сообщение об ошибке"):
            alert_text = page.get_alert_text_and_accept()
            allure.attach(alert_text, name="Текст ошибки", attachment_type=allure.attachment_type.TEXT)
            assert "This user already exist" in alert_text, \
                f"Ожидали 'This user already exist', получили: {alert_text}"

        with allure.step("Сделать скриншот"):
            page.take_screenshot("duplicate_username_error")


    @allure.title("Регистрация с пустыми полями")
    @allure.description("""
    ЦЕЛЬ: Проверить обработку попытки регистрации с незаполненными полями

    ШАГИ:
    1. Открыть главную страницу
    2. Открыть модальное окно регистрации
    3. Оставить поля username и password пустыми
    4. Нажать кнопку "Sign up"

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Появляется alert с сообщением об ошибке
    - Новая учетная запись не создается
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_signup_with_empty_fields(self, driver):
        """Проверка регистрации с пустыми полями"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Попытаться зарегистрироваться с пустыми полями"):
            page.signup("", "")

        with allure.step("Проверить появление alert с ошибкой"):
            alert_text = page.get_alert_text_and_accept()
            allure.attach(alert_text, name="Текст ошибки", attachment_type=allure.attachment_type.TEXT)
            # Система должна показать какую-то ошибку
            assert alert_text != "", "Alert должен содержать сообщение об ошибке"

        with allure.step("Сделать скриншот"):
            page.take_screenshot("signup_empty_fields")


    @allure.title("Регистрация только с username (пустой пароль)")
    @allure.description("""
    ЦЕЛЬ: Проверить обработку регистрации когда заполнен только username

    ШАГИ:
    1. Открыть главную страницу
    2. Открыть модальное окно регистрации
    3. Ввести username, оставить password пустым
    4. Нажать кнопку "Sign up"

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Появляется alert с сообщением об ошибке
    - Учетная запись не создается
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_signup_with_empty_password(self, driver):
        """Проверка регистрации с пустым паролем"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Попытаться зарегистрироваться с пустым паролем"):
            username = Config.generate_random_username()
            page.signup(username, "")

        with allure.step("Проверить появление alert с ошибкой"):
            alert_text = page.get_alert_text_and_accept()
            allure.attach(alert_text, name="Текст ошибки", attachment_type=allure.attachment_type.TEXT)
            assert alert_text != "", "Alert должен содержать сообщение об ошибке"


    @allure.title("Регистрация только с паролем (пустой username)")
    @allure.description("""
    ЦЕЛЬ: Проверить обработку регистрации когда заполнен только password

    ШАГИ:
    1. Открыть главную страницу
    2. Открыть модальное окно регистрации
    3. Оставить username пустым, ввести password
    4. Нажать кнопку "Sign up"

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Появляется alert с сообщением об ошибке
    - Учетная запись не создается
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_signup_with_empty_username(self, driver):
        """Проверка регистрации с пустым username"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Попытаться зарегистрироваться с пустым username"):
            password = Config.generate_random_password()
            page.signup("", password)

        with allure.step("Проверить появление alert с ошибкой"):
            alert_text = page.get_alert_text_and_accept()
            allure.attach(alert_text, name="Текст ошибки", attachment_type=allure.attachment_type.TEXT)
            assert alert_text != "", "Alert должен содержать сообщение об ошибке"

        with allure.step("Сделать скриншот"):
            page.take_screenshot("signup_empty_username")

