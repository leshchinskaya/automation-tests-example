from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from playwright.sync_api import Page

from config.settings import settings
from src.pages.base_page import SeleniumBasePage, PlaywrightBasePage


class SeleniumLoginPage(SeleniumBasePage):
    _username_input = (By.ID, "user-name")
    _password_input = (By.ID, "password")
    _login_button = (By.ID, "login-button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open(settings.base_url)
        return self

    def login(self, username, password):
        self.driver.find_element(*self._username_input).send_keys(username)
        self.driver.find_element(*self._password_input).send_keys(password)
        self.driver.find_element(*self._login_button).click()


class PlaywrightLoginPage(PlaywrightBasePage):
    _username_input = "#user-name"
    _password_input = "#password"
    _login_button = "#login-button"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        super().open(settings.base_url)
        return self

    def login(self, username, password):
        self.page.locator(self._username_input).fill(username)
        self.page.locator(self._password_input).fill(password)
        self.page.locator(self._login_button).click() 