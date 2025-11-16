### Требования

```pip install --force-reinstall -v "selenium==4.38.0"
pip install --force-reinstall -v "pytest==9.0.1"
pip install --force-reinstall -v "pytest-html==4.1.1"
pip install --force-reinstall -v "webdriver-manager==4.0.2"
pip install --force-reinstall -v "allure-pytest==2.15.0"```

## Запуск тестов

### Активировать виртуальное окружение

```bash
source venv/bin/activate
```

### Запустить все тесты demoblaze

```bash
pytest tests/demoblaze_tests/ -v
```

### Запустить конкретную группу тестов

```bash
# Только тесты логина
pytest tests/demoblaze_tests/test_login.py -v

# Только тесты регистрации
pytest tests/demoblaze_tests/test_signup.py -v

# Только тесты категорий
pytest tests/demoblaze_tests/test_categories.py -v
```
## Просмотр отчетов

### HTML отчет

После запуска тестов откройте:
```
reports/report.html
```

### Allure отчет

```bash
# Открыть интерактивный отчет Allure
allure serve reports/allure-results
```

## Примеры команд

```bash
# Запустить все тесты с подробным выводом
pytest tests/demoblaze_tests/ -v

# Запустить с остановкой на первой ошибке
pytest tests/demoblaze_tests/ -x

# Запустить конкретный тест
pytest tests/demoblaze_tests/test_login.py::TestLogin::test_successful_login -v
