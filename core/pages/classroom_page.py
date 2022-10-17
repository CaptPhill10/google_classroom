import time

import allure

from core.base_element import BaseElement
from core.locators.classroom_page_locators import ClassroomLocators
from core.pages.base_page import BasePage


class ClassroomPage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = ClassroomLocators(test_config=self.test_config)
        self.classroom_step()

    @allure.step("Classroom Page")
    def classroom_step(self):
        pass

    def archive_course(self):
        self.main_menu_button.click()
        self.classes_button.click()
        self.course_details_button.click()
        self.archive_course_button.click()
        self.dialog_archive_button.click()
        time.sleep(2)

    def enter_class_name(self, classname):
        self.class_name_field.input_text(classname)

    def enter_section(self, section):
        self.section_field.input_text(section)

    def enter_subject(self, subject):
        self.subject_field.input_text(subject)

    def enter_room(self, room):
        self.room_field.input_text(room)

    @property
    def agree_checkbox(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.AGREE_CHECKBOX
        )

    @property
    def archive_course_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ARCHIVE_COURSE_BUTTON
        )

    @property
    def archive_page_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ARCHIVE_PAGE_BUTTON
        )

    @property
    def class_name_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CLASS_NAME_FIELD
        )

    @property
    def classroom_page_header(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CLASSROOM_PAGE_HEADER
        )

    @property
    def continue_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CONTINUE_BUTTON
        )

    @property
    def continue_button_2(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CONTINUE_BUTTON_2
        )

    @property
    def course_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.COURSE_BUTTON
        )

    @property
    def course_details_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.COURSE_DETAILS_BUTTON
        )

    @property
    def create_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CREATE_BUTTON
        )

    @property
    def create_class_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CREATE_CLASS_BUTTON
        )

    @property
    def create_join_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CREATE_JOIN_BUTTON
        )

    @property
    def dialog_archive_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DIALOG_ARCHIVE_BUTTON
        )

    @property
    def dialog_continue_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DIALOG_CONTINUE_BUTTON
        )

    @property
    def dialog_header(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DIALOG_HEADER
        )

    @property
    def dialog_window(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DIALOG_WINDOW
        )

    @property
    def join_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.JOIN_BUTTON
        )

    @property
    def room_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ROOM_FIELD
        )

    @property
    def section_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SECTION_FIELD
        )

    @property
    def subject_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SUBJECT_FIELD
        )
