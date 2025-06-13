from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver
from playwright.sync_api import Page


class BasePage(ABC):
    def __init__(self, driver_or_page):
        self.driver = driver_or_page

    @abstractmethod
    def open(self, url: str):
        raise NotImplementedError


class SeleniumBasePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver: WebDriver = driver

    def open(self, url: str):
        self.driver.get(url)


class PlaywrightBasePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page: Page = page

    def open(self, url: str):
        self.page.goto(url) 