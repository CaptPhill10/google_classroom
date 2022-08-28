import time

import allure

from core.base_element import BaseElement
from core.locators.archive_page_locators import ArchivePageLocators
from core.pages.base_page import BasePage


class ArchivePage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = ArchivePageLocators(test_config=self.test_config)
        self.archive_step()

    @allure.step("Classwork step")
    def archive_step(self):
        pass

    def delete_course(self):
        self.archive_page_button.click()
        self.course_details_button.click()
        self.delete_button.click()
        # breakpoint()
        self.dialog_delete_button.click()

    @property
    def classroom_menu(self):
        return BaseElement(driver=self.driver, locator=self.locators.CLASSROOM_MENU)

    @property
    def course_details_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.COURSE_DETAILS_BUTTON)

    @property
    def archive_page_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.ARCHIVE_PAGE_BUTTON)

    @property
    def dialog_delete_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.DIALOG_DELETE_BUTTON)

    @property
    def delete_button(self):
        return BaseElement(driver=self.driver, locator=self.locators.DELETE_BUTTON)
