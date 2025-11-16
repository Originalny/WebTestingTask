import random
import string
from datetime import datetime


class Config:
    """Настройки и константы для тестов"""

    # URL сайта
    BASE_URL = "https://www.demoblaze.com/"

    # Тестовые данные для успешного логина
    # Примечание: эти данные нужно создать вручную на сайте
    VALID_USERNAME = "user1231231"
    VALID_PASSWORD = "user1231231"

    # Занятый пользователь (существует в системе)
    EXISTING_USERNAME = "user123"

    # Тестовый пользователь для регистрации
    TEST_SIGNUP_USERNAME = "user"
    TEST_SIGNUP_PASSWORD = "user"

    # Категории товаров
    CATEGORY_PHONES = "Phones"
    CATEGORY_LAPTOPS = "Laptops"
    CATEGORY_MONITORS = "Monitors"

    @staticmethod
    def generate_random_username(prefix="user"):
        """Генерация случайного имени пользователя"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        return f"{prefix}_{timestamp}_{random_str}"

    @staticmethod
    def generate_random_password(length=10):
        """Генерация случайного пароля"""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))
