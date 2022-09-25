import sys
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.base_element import BaseElement
from core.locators.base_locators import BaseLocators


class BasePage:

    def __init__(self, driver, test_config):
        self.driver = driver
        self.test_config = test_config
        self.main_page = "https://accounts.google.com/"
        self.locators = BaseLocators(config=self.test_config)

    def open_main_page(self):
        self.driver.get(self.main_page)

    def find_element(self, locator: tuple, time=10):
        try:
            return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
            )

        except TimeoutException:
            print("Error: cannot find the element: ", sys.exc_info()[0])
            return None

    @staticmethod
    def wait_for_element(element, wait_time=30):
        i = 0
        while not element.visible and i < wait_time:
            print("Not visible")
            time.sleep(1)
            i += 1
        print("Visible")

    def elements_list(self, locator: str):
        try:
            elements = self.driver.find_elements(locator)
            return elements
        except TimeoutException:
            print("Error: cannot find the elements: ", sys.exc_info()[0])
            return None

    # @property
    # def main_menu_button(self):
    #     return BaseElement(driver=self.driver, locator=self.locators.MAIN_MENU_BUTTON)
    #
    # @property
    # def classes_button(self):
    #     return BaseElement(driver=self.driver, locator=self.locators.CLASSES_BUTTON)
