# Пример проекта для автоматизированного тестирования

Этот проект представляет собой каркас (boilerplate) для автоматизированного тестирования на Python. Он включает в себя примеры UI-тестов с использованием **Selenium** и **Playwright**, а также пример API-теста с использованием **httpx**.

## Для тестирования используются

- **UI-тесты** написаны на примере сайта [saucedemo.com](https://www.saucedemo.com)
- **API-тесты** используют публичный API [reqres.in/users](https://reqres.in/api/users)

## Структура проекта

```
automation-tests-example/
├── .github/workflows/ci.yml  # CI/CD пайплайн для GitHub Actions
├── config/settings.py        # Конфигурация проекта (URL, креды)
├── src/
│   ├── api_clients/          # Клиенты для взаимодействия с API
│   └── pages/                # Page Objects для UI тестов
├── tests/
│   ├── conftest.py           # Глобальные фикстуры pytest
│   ├── api/                  # API-тесты
│   └── ui/                   # UI-тесты
├── .env.example              # Пример файла с переменными окружения
├── .gitignore                # Исключения для Git
├── pytest.ini                # Конфигурация pytest
├── requirements.txt          # Зависимости проекта
└── README.md                 # Этот файл
```

## Установка

1.  **Клонируйте репозиторий:**
    ```bash
    git clone <URL репозитория>
    cd automation-tests-example
    ```

2.  **Создайте и активируйте виртуальное окружение:**
    ```bash
    pyenv install 3.11.8
    pyenv local 3.11.8

    # Or use your system's python3.11 if available:
    python3.11 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Установите браузеры для Playwright:**
    ```bash
    playwright install --with-deps
    ```

## Конфигурация

1.  Создайте файл `.env` в корне проекта, скопировав `.env.example`:
    ```bash
    cp .env.example .env
    ```
2.  При необходимости отредактируйте значения в `.env`. Текущие значения подходят для тестового сайта `saucedemo.com`.

## Запуск тестов

Для запуска всех тестов выполните команду:
```bash
pytest
```

Для запуска тестов с определенным маркером (например, только UI-тесты):
```bash
pytest -m ui
```

Доступные маркеры: `ui`, `api`, `smoke`, `regression`.

# Saucedemo credentials
BASE_URL="https://www.saucedemo.com"
USERNAME="standard_user"
PASSWORD="secret_sauce"