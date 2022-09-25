import allure

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
    def add_answer_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.ADD_ANSWER_FIELD)

    @property
    def add_answer_option(self):
        return BaseElement(driver=self.driver, locator=self.locators.ADD_ANSWER_OPTION)

    @property
    def add_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.ADD_BUTTON)

    @property
    def add_question_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.ADD_QUESTION_BUTTON)

    @property
    def add_video_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.ADD_VIDEO_BUTTON)

    @property
    def alterdialog(self):
        return BaseElement(driver=self.driver, locator=self.locators.ALTERDIALOG)

    @property
    def answer_key(self):
        return BaseElement(driver=self.driver, locator=self.locators.ANSWER_KEY)

    @property
    def answer_option_1(self):
        return BaseElement(driver=self.driver, locator=self.locators.ANSWER_OPTION_1)

    @property
    def answer_option_2(self):
        return BaseElement(driver=self.driver, locator=self.locators.ANSWER_OPTION_2)

    @property
    def ask_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.ASK_BUTTON)

    @property
    def assign_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.ASSIGN_BUTTON)

    @property
    def assignment_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.ASSIGNMENT_BUTTON)

    @property
    def assignment_instructions(self):
        return BaseElement(driver=self.driver, locator=self.locators.ASSIGNMENT_INSTRUCTIONS)

    @property
    def attach_video_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.ATTACH_VIDEO_BUTTON)

    @property
    def close_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.CLOSE_BUTTON)

    @property
    def configure_option(self):
        return BaseElement(driver=self.driver, locator=self.locators.CONFIGURE_OPTION)

    @property
    def create_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.CREATE_BUTTON)

    @property
    def description(self):
        return BaseElement(driver=self.driver, locator=self.locators.DESCRIPTION)

    @property
    def description_text_input(self):
        return BaseElement(driver=self.driver, locator=self.locators.DESCRIPTION_TEXT_INPUT)

    @property
    def done_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.DONE_BUTTON)

    @property
    def due_date(self):
        return BaseElement(driver=self.driver, locator=self.locators.DUE_DATE)

    @property
    def due_date_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.DUE_DATE_FIELD)

    @property
    def first_question_title(self):
        return BaseElement(driver=self.driver, locator=self.locators.FIRST_QUESTION_TITLE)

    @property
    def got_it_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.GOT_IT_BUTTON)

    @property
    def guide(self):
        return BaseElement(driver=self.driver, locator=self.locators.GUIDE)

    @property
    def input_answer(self):
        return BaseElement(driver=self.driver, locator=self.locators.INPUT_ANSWER)

    @property
    def listbox_option(self):
        return BaseElement(driver=self.driver, locator=self.locators.LISTBOX_OPTION)

    @property
    def mark_as_incorrect_checkbox(self):
        return BaseElement(driver=self.driver, locator=self.locators.MARK_AS_INCORRECT_CHECKBOX)

    @property
    def material_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.MATERIAL_BUTTON)

    @property
    def material_name(self):
        return BaseElement(driver=self.driver, locator=self.locators.MATERIAL_NAME)

    @property
    def material_topic_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.MATERIAL_TOPIC_FIELD)

    @property
    def no_thanks_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.NO_THANKS_BUTTON)

    @property
    def okay_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.OKAY_BUTTON)

    @property
    def open_quiz(self):
        return BaseElement(driver=self.driver, locator=self.locators.OPEN_QUIZ)

    @property
    def popup(self):
        return BaseElement(driver=self.driver, locator=self.locators.POPUP)

    @property
    def post_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.POST_BUTTON)

    @property
    def question_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.QUESTION_BUTTON)

    @property
    def question_listbox(self):
        return BaseElement(driver=self.driver, locator=self.locators.QUESTION_LISTBOX)

    @property
    def quiz_assignment(self):
        return BaseElement(driver=self.driver, locator=self.locators.QUIZ_ASSIGNMENT)

    @property
    def quiz_assignment_title(self):
        return BaseElement(driver=self.driver, locator=self.locators.QUIZ_ASSIGNMENT_TITLE)

    @property
    def quiz_title(self):
        return BaseElement(driver=self.driver, locator=self.locators.QUIZ_TITLE)

    @property
    def required_radio(self):
        return BaseElement(driver=self.driver, locator=self.locators.REQUIRED_RADIO)

    # @property
    # def next_month(self):
    #     return BaseElement(driver=self.driver, locator=self.locators.NEXT_MONTH)

    @property
    def search_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.SEARCH_BUTTON)

    @property
    def search_video_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.SEARCH_VIDEO_FIELD)

    @property
    def second_answer_key(self):
        return BaseElement(driver=self.driver, locator=self.locators.SECOND_ANSWER_KEY)

    @property
    def second_configure_option(self):
        return BaseElement(driver=self.driver, locator=self.locators.SECOND_CONFIGURE_OPTION)

    @property
    def second_question_title(self):
        return BaseElement(driver=self.driver, locator=self.locators.SECOND_QUESTION_TITLE)

    @property
    def second_required_radio(self):
        return BaseElement(driver=self.driver, locator=self.locators.SECOND_REQUIRED_RADIO)

    @property
    def second_select_option(self):
        return BaseElement(driver=self.driver, locator=self.locators.SECOND_SELECT_OPTION)

    @property
    def select_date(self):
        return BaseElement(driver=self.driver, locator=self.locators.SELECT_DATE)

    @property
    def select_option(self):
        return BaseElement(driver=self.driver, locator=self.locators.SELECT_OPTION)

    @property
    def select_topic(self):
        return BaseElement(driver=self.driver, locator=self.locators.SELECT_TOPIC)

    @property
    def title_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.TITLE_FIELD)

    @property
    def topic_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.TOPIC_BUTTON)

    @property
    def topic_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.TOPIC_FIELD)

    @property
    def topic_name(self):
        return BaseElement(driver=self.driver, locator=self.locators.TOPIC_NAME)

    @property
    def topic_name_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.TOPIC_NAME_FIELD)
