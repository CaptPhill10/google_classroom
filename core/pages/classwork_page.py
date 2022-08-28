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
    def add_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.ADD_BUTTON)

    @property
    def add_video_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.ADD_VIDEO_BUTTON)

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
    def assignment_title_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.ASSIGNMENT_TITLE_FIELD)

    @property
    def attach_video_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.ATTACH_VIDEO_BUTTON)

    @property
    def close_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.CLOSE_BUTTON)

    @property
    def create_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.CREATE_BUTTON)

    @property
    def due_date(self):
        return BaseElement(driver=self.driver, locator=self.locators.DUE_DATE)

    @property
    def due_date_field(self):
        return BaseElement(driver=self.driver, locator=self.locators.DUE_DATE_FIELD)

    @property
    def got_it_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.GOT_IT_BUTTON)

    @property
    def quiz_assignment(self):
        return BaseElement(driver=self.driver, locator=self.locators.QUIZ_ASSIGNMENT)

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
    def select_date(self):
        return BaseElement(driver=self.driver, locator=self.locators.SELECT_DATE)

    @property
    def select_topic(self):
        return BaseElement(driver=self.driver, locator=self.locators.SELECT_TOPIC)

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
