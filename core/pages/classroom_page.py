import time

import allure

from core.base_element import BaseElement
from core.locators.classroom_page_locators import ClassroomLocators
from core.pages.base_page import BasePage


class ClassroomPage(BasePage):
    def __init__(self, driver, test_config, text_data):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.text_data = text_data
        self.locators = ClassroomLocators(test_config=self.test_config)
        self.classroom_step()

    @allure.step("Classroom Page")
    def classroom_step(self):
        pass

    def archive_course(self):
        self.course_details_button.click()
        self.archive_course_button.click()
        self.dialog_archive_button.click()
        time.sleep(2)

    def create_course(self, classname):
        self.wait_for_element_clickable(
            element=self.create_join_button,
            wait_time=30
        )
        self.create_join_button.click()
        if not self.create_join_button.visible:
            self.driver.refresh()
            self.wait_for_element_clickable(
                element=self.create_join_button
            )
            self.create_join_button.click()
        self.create_class_button.click()
        if self.agree_checkbox.visible:
            self.agree_checkbox.click()
            attribute_value = \
                self.continue_button.get_attribute("tabindex")
            if attribute_value == "0":
                self.continue_button_2.click()
            else:
                while attribute_value != "0":
                    print(attribute_value)
                    attribute_value = \
                        self.continue_button.get_attribute("tabindex")
                    print(attribute_value)
                    if attribute_value == "0":
                        self.continue_button_2.click()

        self.enter_class_name(classname)
        self.enter_section(self.text_data.SECTION)
        self.enter_subject(self.text_data.SUBJECT)
        self.enter_room(self.text_data.ROOM)
        attribute_value = self.create_button.get_attribute("tabindex")
        if attribute_value == "0":
            self.create_button.click()
        else:
            while attribute_value != "0":
                print(attribute_value)
                attribute_value = \
                    self.create_button.get_attribute("tabindex")
                print(attribute_value)
                if attribute_value == "0":
                    self.create_button.click()

    def enter_class_name(self, classname):
        self.class_name_field.input_text(classname)

    def enter_section(self, section):
        self.section_field.input_text(section)

    def enter_subject(self, subject):
        self.subject_field.input_text(subject)

    def enter_room(self, room):
        self.room_field.input_text(room)

    @property
    def accept_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ACCEPT_BUTTON
        )

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
    def assignment_course_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ASSIGNMENT_COURSE_BUTTON
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
    def dialog_header(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DIALOG_HEADER
        )

    @property
    def join_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.JOIN_BUTTON
        )

    @property
    def material_course_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.MATERIAL_COURSE_BUTTON
        )

    @property
    def question_course_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.QUESTION_COURSE_BUTTON
        )

    @property
    def quiz_course_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.QUIZ_COURSE_BUTTON
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

    @property
    def teacher_dialog_header(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.TEACHER_DIALOG_HEADER
        )

    # @property
    # def topic_course_button(self):
    #     return BaseElement(
    #         driver=self.driver,
    #         locator=self.locators.TOPIC_COURSE_BUTTON
    #     )
