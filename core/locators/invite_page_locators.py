from core.locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By


class InvitePageLocators(BaseLocators):
    def __init__(self, test_config):
        super().__init__(test_config)

        self.test_config = test_config

        self.DIALOG_INVITE_BUTTON = (
            By.XPATH,
            '//div[@role="dialog"]//div[@role="button" and @data-id="EBS5u"]'
        )

        self.DIALOG_STUDENT_EMAIL = (
            By.XPATH,
            '//div[@role="dialog"]//input[@role="combobox"]'
        )

        self.DIALOG_SELECT_FIRST_PERSON = (
            By.XPATH,
            '//div[@role="dialog"]//ul[@role="listbox"]/div[1]'
        )

        self.INVITE_STUDENT_BUTTON = (
            By.XPATH,
            '//button[@aria-label="Invite students"]'
        )

        self.STUDENT_NAME = (
            By.XPATH,
            '(//span[@class="g2DEGd KwqU3e QRiHXd"]/span)[1]'
        )
