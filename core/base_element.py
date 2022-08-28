import sys

from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    NoSuchElementException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

        self.web_element = None
        self.find()

    def find(self):
        try:
            web_element = WebDriverWait(
                self.driver,
                10,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                ),
            ).until(EC.presence_of_element_located(locator=self.locator))
            self.web_element = web_element
            return None
        except TimeoutException:
            print(f"\nERROR: cannot find the element using a "
                  f"locator {self.locator}. ")
            return None

    def click(self, wait_time=10):
        if self.web_element is not None:
            try:
                web_element = WebDriverWait(self.driver, wait_time).until(
                    EC.element_to_be_clickable(self.locator)
                )
                web_element.click()
                return None
            except StaleElementReferenceException:
                self.driver.refresh()
                web_element = WebDriverWait(self.driver, wait_time).until(
                    EC.element_to_be_clickable(self.locator)
                )
                web_element.click()
                return None
            except TimeoutException:
                web_element.click()
                print(
                    f"\nERROR: cannot find the element using a "
                    f"locator {self.locator}. "
                )
                return None
        else:
            return None

    def has_text(self, value, wait_time=10):
        if self.web_element is not None:
            try:
                WebDriverWait(self.driver, wait_time).until(
                    EC.text_to_be_present_in_element(locator=self.locator, text_=value)
                )
                return True
            except TimeoutException:
                print(
                    f"\nFailed: the text {value} isn't present in the element using the locator {self.locator}.\n",
                    sys.exc_info()[:2],
                )
                return False
        else:
            return None

    def input_text(self, text):
        if self.web_element is not None:
            web_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(mark=self.locator)
            )
            web_element.clear()
            web_element.send_keys(text)
        else:
            return None

    # def set_value(self, text):
    #     web_element = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(mark=self.locator)
    #     )
    #     web_element.clear()
    #     web_element.set_value(text)

    @property
    def get_attribute(self):
        if self.web_element is not None:
            try:
                attribute = self.web_element.get_attribute
                return attribute
            except AttributeError:
                print(
                    "\nERROR: the element doesn't have attribute text.\n",
                    sys.exc_info()[:2],
                )
                return None
        else:
            return None

    @property
    def text(self):
        if self.web_element is not None:
            try:
                text = self.web_element.text
                return text
            except AttributeError:
                print(
                    "\nERROR: the element doesn't have attribute text.\n",
                    sys.exc_info()[:2],
                )
                return None
        else:
            return None

    @property
    def visible(self, wait_time=10):
        if self.web_element is not None:
            try:
                WebDriverWait(self.driver, wait_time).until(
                    EC.visibility_of(self.web_element)
                )
                return True
            except TimeoutException:
                print(
                    f"Error: element with locator {self.locator} not visible after 10 seconds: ",
                    sys.exc_info()[0],
                )
                return False
            except Exception as e:
                print(f"An Exception occurred: {e}")
                return False
        else:
            return False
