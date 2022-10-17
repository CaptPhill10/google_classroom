from core.locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By


class AccountLocators(BaseLocators):
    def __init__(self, test_config):
        super().__init__(test_config)

        self.test_config = test_config

        self.GOOGLE_APPS_BUTTON = (By.XPATH, '//a[@aria-label="Google apps"]')

        self.CLASSROOM_BUTTON = (By.XPATH, '//span[text()="Classroom"]')

        self.GMAIL_BUTTON = (By.XPATH, '//span[text()="Gmail"]')
