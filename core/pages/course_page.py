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
    def alertdialog(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ALERTDIALOG
        )

    @property
    def announcement_popup(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ANNOUNCEMENT_POPUP
        )

    @property
    def next_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.NEXT_BUTTON
        )

    @property
    def save_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SAVE_BUTTON
        )

    @property
    def select_stream_option(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SELECT_STREAM_OPTION
        )

    @property
    def stream_options(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.STREAM_OPTIONS
        )

    @property
    def stream_settings_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.STREAM_SETTINGS_BUTTON
        )
