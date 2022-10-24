import allure

from selenium.webdriver.common.by import By

from core.base_element import BaseElement
from core.locators.gmail_page_locators import GmailPageLocators
from core.pages.base_page import BasePage


class GmailPage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = GmailPageLocators(test_config=self.test_config)
        self.gmail_step()

    @allure.step("Gmail step")
    def gmail_step(self):
        pass

    @property
    def class_invitation_mail(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.CLASS_INVITATION_MAIL
        )

    @property
    def delete_invitation_mail(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.DELETE_INVITATION_MAIL
        )

    @property
    def join_to_class(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.JOIN_TO_CLASS
        )

    @property
    def more_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.MORE_BUTTON
        )

    @property
    def search_box(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SEARCH_BOX
        )

    @property
    def search_term(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SEARCH_TERM
        )

    @property
    def show_content_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.SHOW_CONTENT_BUTTON
        )

    def show_content(self):
        elements_list = self.driver.find_elements(
            by=By.XPATH,
            value='//div[@aria-label="Show trimmed content"]'
        )
        print(f"Content buttons: {len(elements_list)}")
        # self.wait_for_element_clickable(
        #     element=self.show_content_button,
        #     wait_time=30
        # )
        show_content = (
            By.XPATH,
            f'(//div[@aria-label="Show trimmed content"])[{len(elements_list)}]'
        )
        BaseElement(driver=self.driver, locator=show_content).click()

    def join_class(self):
        elements_list = self.driver.find_elements(
            by=By.XPATH,
            value='//table[@role="presentation"]//a[text()="Join"]'
        )
        print(f"Join buttons: {len(elements_list)}")
        join_class_button = (
            By.XPATH,
            f'(//table[@role="presentation"]'
            f'//a[text()="Join"])[{len(elements_list)}]'
        )
        BaseElement(driver=self.driver, locator=join_class_button).click()
