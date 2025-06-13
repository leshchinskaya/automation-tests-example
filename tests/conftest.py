import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для инициализации и закрытия WebDriver для Selenium.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# Для Playwright фикстура 'page' предоставляется плагином pytest-playwright автоматически.
# Нет необходимости определять ее здесь. 