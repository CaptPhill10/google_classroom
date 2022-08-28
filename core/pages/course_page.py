import allure

from core.base_element import BaseElement
from core.locators.course_page_locators import CoursePageLocators
from core.pages.base_page import BasePage


class CoursePage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = CoursePageLocators(test_config=self.test_config)
        self.course_step()

    @allure.step("Course step")
    def course_step(self):
        pass

    @property
    def classwork_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.CLASSWORK_BUTTON)

    @property
    def got_it_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.GOT_IT)

    @property
    def stream_settings_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.STREAM_SETTINGS_BUTTON)

    @property
    def stream_options(self):
        return BaseElement(driver=self.driver, locator=self.locators.STREAM_OPTIONS)

    @property
    def select_option(self):
        return BaseElement(driver=self.driver, locator=self.locators.SELECT_OPTION)

    @property
    def save_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.SAVE_BUTTON)
