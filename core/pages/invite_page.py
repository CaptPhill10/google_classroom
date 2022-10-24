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

    def invite_people(self, teacher_login, student_login):
        self.wait_for_element_clickable(
            element=self.people_button,
            wait_time=30
        )
        self.people_button.click()
        if not self.invite_teacher_button.visible:
            self.driver.refresh()
            self.wait_for_element_clickable(
                element=self.people_button,
                wait_time=30
            )
            self.people_button.click()

        self.invite_teacher_button.click()
        self.wait_for_element_clickable(
            element=self.dialog_people_email,
            wait_time=30
        )
        self.dialog_people_email.input_text(teacher_login)

        self.wait_for_element_clickable(
            element=self.dialog_select_first_person,
            wait_time=30
        )
        self.dialog_select_first_person.click()
        attribute_value = \
            self.dialog_invite_button.get_attribute("tabindex")
        if attribute_value == "0":
            self.dialog_invite_button.click()
        else:
            while attribute_value != "0":
                print(attribute_value)
                attribute_value = \
                    self.dialog_invite_button.get_attribute("tabindex")
                print(attribute_value)
                if attribute_value == "0":
                    self.dialog_invite_button.click()

        self.wait_for_element(element=self.teacher_invited)

        self.invite_student_button.click()
        self.wait_for_element_clickable(
            element=self.dialog_people_email,
            wait_time=30
        )
        self.dialog_people_email.input_text(
            student_login
        )
        self.wait_for_element_clickable(
            element=self.dialog_select_first_person,
            wait_time=30
        )
        self.dialog_select_first_person.click()
        attribute_value = \
            self.dialog_invite_button.get_attribute("tabindex")
        if attribute_value == "0":
            self.dialog_invite_button.click()
        else:
            while attribute_value != "0":
                print(attribute_value)
                attribute_value = \
                    self.dialog_invite_button.get_attribute("tabindex")
                print(attribute_value)
                if attribute_value == "0":
                    self.dialog_invite_button.click()

    @property
    def dialog_people_email(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DIALOG_PEOPLE_EMAIL
        )

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
    def invite_student_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.INVITE_STUDENT_BUTTON
        )

    @property
    def invite_teacher_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.INVITE_TEACHER_BUTTON
        )

    @property
    def student_name(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.STUDENT_NAME
        )

    @property
    def teacher_invited(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.TEACHER_INVITED
        )

    @property
    def teacher_name(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.TEACHER_NAME
        )
