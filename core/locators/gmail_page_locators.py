from selenium.webdriver.common.by import By
from core.locators.base_locators import BaseLocators


class GmailPageLocators(BaseLocators):
    def __init__(self, test_config):
        super().__init__(test_config)

        self.test_config = test_config

        self.CLASS_INVITATION_MAIL = (
            By.XPATH,
            '(//table[@id="gs_sbt50"]'
            '//div[contains (@title, "Class invitation:")])[1]'
        )

        self.DELETE_INVITATION_MAIL = (
            By.XPATH,
            '//div[@role="menu"]//div[@id=":6t"]'
        )

        self.JOIN_TO_CLASS = (
            By.XPATH,
            '//table[@role="presentation"]//a[text()="Join"]'
        )

        self.MORE_BUTTON = (By.XPATH, '//div[@aria-label="More"]')

        self.SEARCH_BOX = (By.XPATH, '//input[@name="q"]')

        self.SEARCH_TERM = (By.XPATH, '//div[@class="nH V8djrc byY"]')

        self.SHOW_CONTENT_BUTTON = (
            By.XPATH,
            '//div[@aria-label="Show trimmed content"]'
        )

        self.TEACHER_INVITATION_MAIL = (
            By.XPATH,
            '(//table[@id="gs_sbt50"]'
            '//div[contains (@title, "Invitation")])[1]'
        )
