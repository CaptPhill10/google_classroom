import allure
import time
from datetime import datetime, timedelta
from core.base_element import BaseElement
from core.locators.classwork_page_locators import ClassworkPageLocators
from core.pages.base_page import BasePage


class ClassworkPage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = ClassworkPageLocators(test_config=self.test_config)
        self.classwork_step()

    @allure.step("Classwork step")
    def classwork_step(self):
        pass

    @property
    def add_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ADD_BUTTON
        )

    @property
    def add_link_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ADD_LINK_BUTTON
        )

    @property
    def add_video_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ADD_VIDEO_BUTTON
        )

    @property
    def alertdialog_hand_in_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ALERTDIALOG_HAND_IN_BUTTON
        )

    @property
    def alertdialog_input(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ALERTDIALOG_INPUT
        )

    @property
    def alertdialog_mark_as_done(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ALERTDIALOG_MARK_AS_DONE
        )

    @property
    def alertdialog_rename_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ALERTDIALOG_RENAME_BUTTON
        )

    @property
    def answer_input(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ANSWER_INPUT
        )

    @property
    def assigned_task(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ASSIGNED_TASK
        )

    @property
    def assigned_task_view_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ASSIGNED_TASK_VIEW_BUTTON
        )

    @property
    def assigned_work(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ASSIGNED_WORK
        )

    @property
    def assignment_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ASSIGNMENT_BUTTON
        )

    @property
    def assignment_name(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ASSIGNMENT_NAME
        )

    @property
    def assignment_settings_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ASSIGNMENT_SETTINGS_BUTTON
        )

    @property
    def attach_link_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ATTACH_LINK_BUTTON
        )

    @property
    def attach_video_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ATTACH_VIDEO_BUTTON
        )

    @property
    def attachment_link(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ATTACHMENT_LINK
        )

    @property
    def changed_assignment_name(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CHANGED_ASSIGNMENT_NAME
        )

    @property
    def changed_other_name(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CHANGED_OTHER_NAME
        )

    @property
    def course_title(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.COURSE_TITLE
        )

    @property
    def create_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CREATE_BUTTON
        )

    @property
    def create_quiz_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CREATE_QUIZ_BUTTON
        )

    @property
    def date_picker_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DATE_PICKER_BUTTON
        )

    @property
    def due_date_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DUE_DATE_BUTTON
        )

    @property
    def due_date_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DUE_DATE_FIELD
        )

    @property
    def edit_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.EDIT_BUTTON
        )

    @property
    def forms_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.FORMS_BUTTON
        )

    @property
    def google_quiz(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.GOOGLE_QUIZ
        )

    @property
    def hand_in_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.HAND_IN_BUTTON
        )

    @property
    def mark_as_done(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.MARK_AS_DONE
        )

    @property
    def material_attachment(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.MATERIAL_ATTACHMENT
        )

    @property
    def material_attachment_link(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.MATERIAL_ATTACHMENT_LINK
        )

    @property
    def material_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.MATERIAL_BUTTON
        )

    @property
    def material_title(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.MATERIAL_TITLE
        )

    @property
    def material_page_title(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.MATERIAL_PAGE_TITLE
        )

    @property
    def material_settings_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.MATERIAL_SETTINGS_BUTTON
        )

    @property
    def open_quiz(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.OPEN_QUIZ
        )

    @property
    def other_name(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.OTHER_NAME
        )

    @property
    def post_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.POST_BUTTON
        )

    @property
    def question_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.QUESTION_BUTTON
        )

    @property
    def question_title(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.QUESTION_TITLE
        )

    @property
    def question_settings_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.QUESTION_SETTINGS_BUTTON
        )

    @property
    def question_status(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.QUESTION_STATUS
        )

    @property
    def quiz_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.QUIZ_BUTTON
        )

    @property
    def quiz_name(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.QUIZ_NAME
        )

    @property
    def remove_attachment(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.REMOVE_ATTACHMENT
        )

    @property
    def rename_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.RENAME_BUTTON
        )

    @property
    def save_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SAVE_BUTTON
        )

    @property
    def search_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SEARCH_BUTTON
        )

    @property
    def search_video_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SEARCH_VIDEO_FIELD
        )

    @property
    def task_title(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.TASK_TITLE
        )

    @property
    def topic_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.TOPIC_BUTTON
        )

    @property
    def topic_name(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.TOPIC_NAME
        )

    @property
    def topic_name_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.TOPIC_NAME_FIELD
        )

    @property
    def topic_settings_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.TOPIC_SETTINGS_BUTTON
        )

    @property
    def unsubmit_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.UNSUBMIT_BUTTON
        )

    @property
    def your_work_label(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.YOUR_WORK_LABEL
        )

    def step_date(self):
        sub_date = datetime.now() + timedelta(days=7)
        time.sleep(3)
        self.due_date_field.input_text_2(sub_date.strftime("%b %d, %Y"))
