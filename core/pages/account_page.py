import allure

from core.base_element import BaseElement
from core.locators.account_page_locators import AccountLocators
from core.pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = AccountLocators(test_config=self.test_config)
        self.account_step()

    @allure.step("Account Page")
    def account_step(self):
        pass

    def open_classroom(self):
        self.wait_for_element_clickable(
            element=self.google_apps_button,
            wait_time=30
        )
        self.google_apps_button.click()
        self.driver.switch_to.frame("app")
        self.classroom_button.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def open_gmail(self):
        self.wait_for_element_clickable(
            element=self.google_apps_button,
            wait_time=30
        )
        self.google_apps_button.click()
        if not self.apps_iframe.visible:
            self.google_apps_button.click()
        self.driver.switch_to.frame("app")
        self.gmail_button.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    @property
    def apps_iframe(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.APPS_IFRAME
        )

    @property
    def classroom_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CLASSROOM_BUTTON
        )

    @property
    def gmail_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.GMAIL_BUTTON
        )

    @property
    def google_apps_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.GOOGLE_APPS_BUTTON
        )
