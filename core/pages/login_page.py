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
        self.email_field.input_text(email)
        self.next_button.click()
        self.wait_for_element_clickable(element=self.password_field)
        self.password_field.input_text(password)
        self.next_button.click()

    @property
    def create_account_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CREATE_ACCOUNT_BUTTON
        )

    @property
    def email_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.EMAIL_FIELD
        )

    @property
    def email_link(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.EMAIL_LINK
        )

    @property
    def empty_login_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.EMPTY_LOGIN_FIELD
        )

    @property
    def empty_password_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.EMPTY_PASSWORD_FIELD
        )

    @property
    def forgot_email_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.FORGOT_EMAIL_BUTTON
        )

    @property
    def forgot_password_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.FORGOT_PASSWORD_BUTTON
        )

    @property
    def language_selector(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.LANGUAGE_SELECTOR
        )

    @property
    def login_error_message(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.LOGIN_ERROR_MESSAGE
        )

    @property
    def next_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.NEXT_BUTTON
        )

    @property
    def password_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.PASSWORD_FIELD
        )

    @property
    def password_error_message(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.PASSWORD_ERROR_MESSAGE
        )

    @property
    def select_english(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ENGLISH_LANGUAGE
        )

    @property
    def show_password_checkbox(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SHOW_PASSWORD_CHECKBOX
        )
