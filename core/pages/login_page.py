import time

import allure

from core.base_element import BaseElement
from core.locators.login_page_locators import LoginLocators
from core.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = LoginLocators(test_config=self.test_config)
        self.login_step()

    @allure.step("Login Page")
    def login_step(self):
        pass

    def do_login(self, email, password):
        self.language_selector.click()
        self.select_english.click()
        time.sleep(1)
        self.email_field.input_text(email)
        self.next_button.click()
        time.sleep(1)
        self.password_field.input_text(password)
        self.next_button.click()

    @property
    def language_selector(self):
        return BaseElement(driver=self.driver, locator=self.locators.LANGUAGE_SELECTOR)

    @property
    def select_english(self):
        return BaseElement(driver=self.driver, locator=self.locators.ENGLISH_LANGUAGE)

    @property
    def email_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.EMAIL_FIELD)

    @property
    def password_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.PASSWORD_FIELD)

    @property
    def next_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.NEXT_BUTTON)
