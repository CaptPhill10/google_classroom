import allure

from core.base_element import BaseElement
from core.locators.gmail_page_locators import GmailPageLocators
from core.pages.base_page import BasePage


class GmailPage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = GmailPageLocators(test_config=self.test_config)
        self.gmail_step()

    @allure.step("Gmail step")
    def gmail_step(self):
        pass

    @property
    def class_invitation_mail(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CLASS_INVITATION_MAIL
        )

    @property
    def delete_invitation_mail(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DELETE_INVITATION_MAIL
        )

    @property
    def join_to_class(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.JOIN_TO_CLASS
        )

    @property
    def more_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.MORE_BUTTON
        )

    @property
    def search_box(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SEARCH_BOX
        )

    @property
    def search_term(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SEARCH_TERM
        )

    @property
    def show_content_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SHOW_CONTENT_BUTTON
        )
