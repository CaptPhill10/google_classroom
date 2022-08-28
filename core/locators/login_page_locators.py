# import core.locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By


class LoginLocators:
    def __init__(self, test_config):
        # super().__init__(test_config)
        #
        # self.test_config = test_config

        self.LANGUAGE_SELECTOR = (By.XPATH, '//*[@id="lang-chooser"]')

        self.ENGLISH_LANGUAGE = (By.XPATH, '//*[@id="lang-chooser"]/div[2]/div[10]')

        self.EMAIL_FIELD = (By.XPATH, '//*[@id="identifierId"]')

        self.PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')

        self.NEXT_BUTTON = (By.XPATH, '//span[text()="Next"]')
