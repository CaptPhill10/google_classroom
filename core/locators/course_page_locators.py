from selenium.webdriver.common.by import By
from core.locators.base_locators import BaseLocators


class CoursePageLocators(BaseLocators):
    def __init__(self, test_config):
        super().__init__(test_config)

        self.test_config = test_config

        self.SAVE_BUTTON = (
            By.XPATH,
            '//div[@class="jzUkrb"]'
        )

        self.SAVED_MESSAGE = (
            By.XPATH,
            '//div[@class="RmhvCc Z3WPhc"]//span[contains (text(), "saved")]'
        )

        self.SELECT_STREAM_OPTION = (
            By.XPATH,
            '//div[contains (@class, "NFY6c")]//ul[@role="listbox"]/li[2]'
        )

        self.STREAM_OPTIONS = (
            By.XPATH,
            '//p[text()="Stream"]/..//div[@role="combobox"]'
        )

        self.STREAM_SETTINGS_BUTTON = (
            By.XPATH,
            '//span[text()="Stream settings"]'
        )
