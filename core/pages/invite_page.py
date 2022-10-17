import allure

from core.base_element import BaseElement
from core.locators.invite_page_locators import InvitePageLocators
from core.pages.base_page import BasePage


class InvitePage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = InvitePageLocators(test_config=self.test_config)
        self.invite_step()

    @allure.step("Invite step")
    def invite_step(self):
        pass

    @property
    def dialog_invite_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DIALOG_INVITE_BUTTON
        )

    @property
    def dialog_select_first_person(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DIALOG_SELECT_FIRST_PERSON
        )

    @property
    def dialog_student_email(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DIALOG_STUDENT_EMAIL
        )

    @property
    def invite_student_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.INVITE_STUDENT_BUTTON
        )

    @property
    def student_name(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.STUDENT_NAME
        )
