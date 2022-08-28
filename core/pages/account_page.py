import time

import allure

from core.base_element import BaseElement
from core.locators.account_page_locators import AccountLocators
from core.pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class AccountPage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = AccountLocators(test_config=self.test_config)
        self.account_step()

    @allure.step("Account Page")
    def account_step(self):
        pass

    def open_classroom(self):
        self.google_apps_button.click()
        self.driver.switch_to.frame("app")
        self.classroom_button.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    @property
    def google_apps_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.GOOGLE_APPS_BUTTON)

    @property
    def ul(self):
        return BaseElement(driver=self.driver, locator=self.locators.UNORDERED_LIST)

    @property
    def classroom_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.CLASSROOM_BUTTON)
