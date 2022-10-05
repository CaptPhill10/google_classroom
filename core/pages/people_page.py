import allure

from core.base_element import BaseElement
from core.locators.people_page_locators import PeoplePageLocators
from core.pages.base_page import BasePage


class PeoplePage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = PeoplePageLocators(test_config=self.test_config)
        self.people_page_step()

    def people_page_step(self):
        pass

    @property
    def invite_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.INVITE_BUTTON)

    @property
    def invite_student_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.INVITE_STUDENT_BUTTON)

    @property
    def invite_teacher_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.INVITE_TEACHER_BUTTON)

    @property
    def people_email(self):
        return BaseElement(driver=self.driver, locator=self.locators.PEOPLE_EMAIL)

    @property
    def people_email_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.PEOPLE_EMAIL_FIELD)

    @property
    def people_option(self):
        return BaseElement(driver=self.driver, locator=self.locators.PEOPLE_OPTION)

    @property
    def student_name(self):
        return BaseElement(driver=self.driver, locator=self.locators.STUDENT_NAME)

    @property
    def teacher_name(self):
        return BaseElement(driver=self.driver, locator=self.locators.TEACHER_NAME)
