import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from config.settings import settings
from src.pages.login_page import SeleniumLoginPage
from src.pages.inventory_page import SeleniumInventoryPage


@pytest.mark.ui
@pytest.mark.smoke
def test_user_can_login_with_selenium(driver: WebDriver):
    # Arrange
    login_page = SeleniumLoginPage(driver)
    inventory_page = SeleniumInventoryPage(driver)

    # Act
    login_page.open()
    login_page.login(settings.username, settings.password)

    # Assert
    inventory_page.should_be_inventory_list() 