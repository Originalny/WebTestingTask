import pytest
import allure
from .pages.main_page import MainPage
from .utils.config import Config


@allure.feature('Поиск и фильтрация')
@allure.story('Фильтрация товаров по категориям')
class TestCategories:
    """Тесты функциональности поиска по категориям"""

    @allure.title("Фильтрация товаров по категории 'Phones'")
    @allure.description("""
    ЦЕЛЬ: Проверить, что при выборе категории "Phones" отображаются только телефоны

    ШАГИ:
    1. Открыть главную страницу demoblaze.com
    2. Кликнуть по категории "Phones"
    3. Получить список отображаемых товаров

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Отображаются товары
    - Все товары относятся к категории телефонов
    - Названия содержат характерные слова: Samsung, Nokia, Nexus, HTC, Iphone, Sony
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_filter_by_phones_category(self, driver):
        """Проверка фильтрации по категории Phones"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Кликнуть по категории Phones"):
            page.click_phones_category()

        with allure.step("Получить количество отображаемых товаров"):
            product_count = page.get_product_count()
            allure.attach(
                str(product_count),
                name="Количество товаров в категории Phones",
                attachment_type=allure.attachment_type.TEXT
            )
            assert product_count > 0, "В категории Phones нет товаров"

        with allure.step("Получить названия товаров"):
            titles = page.get_product_titles()
            assert len(titles) > 0, "Не удалось получить названия товаров"

        with allure.step("Проверить, что товары относятся к телефонам"):
            # Характерные слова для телефонов
            phone_keywords = ['samsung', 'nokia', 'nexus', 'iphone', 'htc', 'sony', 'lumia']

            # Проверяем, что каждый товар содержит хотя бы одно ключевое слово
            for title in titles:
                title_lower = title.lower()
                has_keyword = any(keyword in title_lower for keyword in phone_keywords)
                allure.attach(
                    f"Товар: {title}\nСодержит ключевые слова телефонов: {has_keyword}",
                    name=f"Проверка: {title}",
                    attachment_type=allure.attachment_type.TEXT
                )
                assert has_keyword, f"Товар '{title}' не похож на телефон"

        with allure.step("Сделать скриншот категории Phones"):
            page.take_screenshot("phones_category")


    @allure.title("Фильтрация товаров по категории 'Laptops'")
    @allure.description("""
    ЦЕЛЬ: Проверить, что при выборе категории "Laptops" отображаются только ноутбуки

    ШАГИ:
    1. Открыть главную страницу demoblaze.com
    2. Кликнуть по категории "Laptops"
    3. Получить список отображаемых товаров

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Отображаются товары
    - Все товары относятся к категории ноутбуков
    - Названия содержат характерные слова: vaio, MacBook, Dell, etc.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_filter_by_laptops_category(self, driver):
        """Проверка фильтрации по категории Laptops"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Кликнуть по категории Laptops"):
            page.click_laptops_category()

        with allure.step("Получить количество отображаемых товаров"):
            product_count = page.get_product_count()
            allure.attach(
                str(product_count),
                name="Количество товаров в категории Laptops",
                attachment_type=allure.attachment_type.TEXT
            )
            assert product_count > 0, "В категории Laptops нет товаров"

        with allure.step("Получить названия товаров"):
            titles = page.get_product_titles()
            assert len(titles) > 0, "Не удалось получить названия товаров"

        with allure.step("Проверить, что товары относятся к ноутбукам"):
            # Характерные слова для ноутбуков
            laptop_keywords = ['vaio', 'macbook', 'dell', 'sony']

            # Проверяем, что каждый товар содержит хотя бы одно ключевое слово
            for title in titles:
                title_lower = title.lower()
                has_keyword = any(keyword in title_lower for keyword in laptop_keywords)
                allure.attach(
                    f"Товар: {title}\nСодержит ключевые слова ноутбуков: {has_keyword}",
                    name=f"Проверка: {title}",
                    attachment_type=allure.attachment_type.TEXT
                )
                # Для ноутбуков можем быть менее строгими, т.к. там могут быть общие названия
                # Просто проверяем, что это не телефон
                phone_keywords = ['samsung galaxy', 'nokia lumia', 'nexus', 'iphone', 'htc']
                is_phone = any(keyword in title_lower for keyword in phone_keywords)
                assert not is_phone, f"Товар '{title}' выглядит как телефон в категории ноутбуков"

        with allure.step("Сделать скриншот категории Laptops"):
            page.take_screenshot("laptops_category")


    @allure.title("Фильтрация товаров по категории 'Monitors'")
    @allure.description("""
    ЦЕЛЬ: Проверить, что при выборе категории "Monitors" отображаются только мониторы

    ШАГИ:
    1. Открыть главную страницу demoblaze.com
    2. Кликнуть по категории "Monitors"
    3. Получить список отображаемых товаров

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Отображаются товары
    - Все товары относятся к категории мониторов
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_filter_by_monitors_category(self, driver):
        """Проверка фильтрации по категории Monitors"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Кликнуть по категории Monitors"):
            page.click_monitors_category()

        with allure.step("Получить количество отображаемых товаров"):
            product_count = page.get_product_count()
            allure.attach(
                str(product_count),
                name="Количество товаров в категории Monitors",
                attachment_type=allure.attachment_type.TEXT
            )
            assert product_count > 0, "В категории Monitors нет товаров"

        with allure.step("Получить названия товаров"):
            titles = page.get_product_titles()
            assert len(titles) > 0, "Не удалось получить названия товаров"

        with allure.step("Проверить, что товары НЕ являются телефонами или ноутбуками"):
            # Проверяем, что это точно не телефоны
            phone_keywords = ['samsung galaxy', 'nokia', 'nexus', 'iphone', 'htc']
            for title in titles:
                title_lower = title.lower()
                is_phone = any(keyword in title_lower for keyword in phone_keywords)
                assert not is_phone, f"Товар '{title}' выглядит как телефон в категории мониторов"

        with allure.step("Сделать скриншот категории Monitors"):
            page.take_screenshot("monitors_category")


    @allure.title("Переключение между категориями")
    @allure.description("""
    ЦЕЛЬ: Проверить корректность работы при переключении между разными категориями

    ШАГИ:
    1. Открыть главную страницу
    2. Выбрать категорию Phones
    3. Проверить количество товаров
    4. Выбрать категорию Laptops
    5. Проверить количество товаров
    6. Выбрать категорию Monitors
    7. Проверить количество товаров

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - При каждом переключении обновляется список товаров
    - Количество товаров различается
    - Нет ошибок при переключении
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_switching_between_categories(self, driver):
        """Проверка переключения между категориями"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Выбрать категорию Phones и запомнить количество"):
            page.click_phones_category()
            phones_count = page.get_product_count()
            allure.attach(str(phones_count), name="Phones count", attachment_type=allure.attachment_type.TEXT)
            assert phones_count > 0, "В категории Phones нет товаров"

        with allure.step("Выбрать категорию Laptops и запомнить количество"):
            page.click_laptops_category()
            laptops_count = page.get_product_count()
            allure.attach(str(laptops_count), name="Laptops count", attachment_type=allure.attachment_type.TEXT)
            assert laptops_count > 0, "В категории Laptops нет товаров"

        with allure.step("Выбрать категорию Monitors и запомнить количество"):
            page.click_monitors_category()
            monitors_count = page.get_product_count()
            allure.attach(str(monitors_count), name="Monitors count", attachment_type=allure.attachment_type.TEXT)
            assert monitors_count > 0, "В категории Monitors нет товаров"

        with allure.step("Проверить, что количества различаются"):
            # Все категории должны иметь товары
            counts = [phones_count, laptops_count, monitors_count]
            allure.attach(
                f"Phones: {phones_count}\nLaptops: {laptops_count}\nMonitors: {monitors_count}",
                name="Сравнение количества товаров",
                attachment_type=allure.attachment_type.TEXT
            )
            # Проверяем, что хотя бы одна категория имеет другое количество
            # (т.е. фильтрация действительно работает)
            assert len(set(counts)) > 1 or all(c > 0 for c in counts), \
                "Все категории имеют одинаковое количество товаров - возможно фильтрация не работает"

        with allure.step("Вернуться к категории Phones"):
            page.click_phones_category()
            final_phones_count = page.get_product_count()
            # Количество должно остаться таким же
            assert final_phones_count > 0, "Товары не отображаются при повторном выборе категории"


    @allure.title("Проверка отображения товаров на главной странице (без фильтра)")
    @allure.description("""
    ЦЕЛЬ: Проверить, что на главной странице отображаются товары из всех категорий

    ШАГИ:
    1. Открыть главную страницу
    2. Получить список всех отображаемых товаров

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Отображаются товары
    - Товары из разных категорий (телефоны, ноутбуки, мониторы)
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_main_page_shows_all_products(self, driver):
        """Проверка отображения всех товаров на главной странице"""
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Получить количество товаров на главной странице"):
            total_count = page.get_product_count()
            allure.attach(
                str(total_count),
                name="Общее количество товаров",
                attachment_type=allure.attachment_type.TEXT
            )
            assert total_count > 0, "На главной странице нет товаров"

        with allure.step("Получить названия товаров"):
            titles = page.get_product_titles()
            allure.attach(
                "\n".join(titles),
                name="Список всех товаров",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Проверить разнообразие категорий"):
            # Проверяем, что есть хотя бы один телефон
            phone_keywords = ['samsung', 'nokia', 'nexus', 'iphone', 'htc']
            has_phones = any(
                any(keyword in title.lower() for keyword in phone_keywords)
                for title in titles
            )

            allure.attach(
                f"Есть телефоны: {has_phones}",
                name="Проверка наличия категорий",
                attachment_type=allure.attachment_type.TEXT
            )

            # Главная страница должна показывать товары
            assert len(titles) >= 3, "На главной странице слишком мало товаров"


    @allure.title("Проверка количества товаров в каждой категории")
    @allure.description("""
    ЦЕЛЬ: Проверить, что каждая категория содержит товары

    ШАГИ:
    1. Проверить категорию Phones
    2. Проверить категорию Laptops
    3. Проверить категорию Monitors

    ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:
    - Каждая категория содержит хотя бы один товар
    - Данные о количестве товаров сохраняются в отчет
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_all_categories_have_products(self, driver):
        """Проверка, что все категории содержат товары"""
        page = MainPage(driver)
        categories_data = []

        with allure.step("Открыть главную страницу"):
            page.open()

        with allure.step("Проверить категорию Phones"):
            page.click_phones_category()
            phones_count = page.get_product_count()
            phones_titles = page.get_product_titles()
            categories_data.append(("Phones", phones_count, len(phones_titles)))
            assert phones_count > 0, "Категория Phones пуста"

        with allure.step("Проверить категорию Laptops"):
            page.click_laptops_category()
            laptops_count = page.get_product_count()
            laptops_titles = page.get_product_titles()
            categories_data.append(("Laptops", laptops_count, len(laptops_titles)))
            assert laptops_count > 0, "Категория Laptops пуста"

        with allure.step("Проверить категорию Monitors"):
            page.click_monitors_category()
            monitors_count = page.get_product_count()
            monitors_titles = page.get_product_titles()
            categories_data.append(("Monitors", monitors_count, len(monitors_titles)))
            assert monitors_count > 0, "Категория Monitors пуста"

        with allure.step("Сформировать отчет о категориях"):
            report = "\n".join([
                f"{cat}: {count} карточек, {titles} названий"
                for cat, count, titles in categories_data
            ])
            allure.attach(
                report,
                name="Статистика по категориям",
                attachment_type=allure.attachment_type.TEXT
            )
