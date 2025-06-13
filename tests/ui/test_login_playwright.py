import pytest
from playwright.sync_api import Page

from config.settings import settings
from src.pages.login_page import PlaywrightLoginPage
from src.pages.inventory_page import PlaywrightInventoryPage


@pytest.mark.ui
@pytest.mark.smoke
def test_user_can_login_with_playwright(page: Page):
    # Arrange
    login_page = PlaywrightLoginPage(page)
    inventory_page = PlaywrightInventoryPage(page)

    # Act
    login_page.open()
    login_page.login(settings.username, settings.password)

    # Assert
    inventory_page.should_be_inventory_list() 