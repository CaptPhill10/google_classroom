import allure
from core.base_element import BaseElement
from core.locators.googleform_page_locators import GoogleformPageLocators
from core.pages.base_page import BasePage


class GoogleformPage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = GoogleformPageLocators(test_config=self.test_config)
        self.googleform_step()

    @allure.step("Googleform step")
    def googleform_step(self):
        pass

    @property
    def add_answer_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ADD_ANSWER_FIELD
        )

    @property
    def add_question_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ADD_QUESTION_BUTTON
        )

    @property
    def answer_key(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ANSWER_KEY
        )

    @property
    def answer_submitted_time(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ANSWER_SUBMITTED_TIME
        )

    @property
    def configure_option(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CONFIGURE_OPTION
        )

    @property
    def done_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DONE_BUTTON
        )

    @property
    def edit_form_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.EDIT_FORM_BUTTON
        )

    @property
    def first_answer_input(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.FIRST_ANSWER_INPUT
        )

    @property
    def first_answer_text(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.FIRST_ANSWER_TEXT
        )

    @property
    def first_question_title(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.FIRST_QUESTION_TITLE
        )

    @property
    def individual_tab(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.INDIVIDUAL_TAB
        )

    @property
    def input_answer(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.INPUT_ANSWER
        )

    @property
    def mark_as_incorrect_checkbox(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.MARK_AS_INCORRECT_CHECKBOX
        )

    @property
    def question_name(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.QUESTION_NAME
        )

    @property
    def quiz_title(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.QUIZ_TITLE
        )

    @property
    def required_radio(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.REQUIRED_RADIO
        )

    @property
    def responses_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.RESPONSES_BUTTON
        )

    @property
    def second_answer_input(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SECOND_ANSWER_INPUT
        )

    @property
    def second_answer_text(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SECOND_ANSWER_TEXT
        )

    @property
    def second_answer_key(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SECOND_ANSWER_KEY
        )

    @property
    def second_configure_option(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SECOND_CONFIGURE_OPTION
        )

    @property
    def second_question_name(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SECOND_QUESTION_NAME
        )

    @property
    def second_question_title(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SECOND_QUESTION_TITLE
        )

    @property
    def second_required_radio(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SECOND_REQUIRED_RADIO
        )

    @property
    def second_select_option(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SECOND_SELECT_OPTION
        )

    @property
    def select_option(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SELECT_OPTION
        )

    @property
    def submit_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SUBMIT_BUTTON
        )
