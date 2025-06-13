from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from playwright.sync_api import Page, expect

from src.pages.base_page import SeleniumBasePage, PlaywrightBasePage


class SeleniumInventoryPage(SeleniumBasePage):
    _inventory_list_selector = (By.ID, "inventory_container")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def should_be_inventory_list(self):
        assert self.driver.find_element(*self._inventory_list_selector).is_displayed()
        return self


class PlaywrightInventoryPage(PlaywrightBasePage):
    _inventory_list_selector = "#inventory_container"

    def __init__(self, page: Page):
        super().__init__(page)

    def should_be_inventory_list(self):
        inventory_list = self.page.locator(self._inventory_list_selector).first
        expect(inventory_list).to_be_visible()
        return self 