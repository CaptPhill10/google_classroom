from core.locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By


class ArchivePageLocators(BaseLocators):
    def __init__(self, test_config):
        super().__init__(test_config)

        self.test_config = test_config

        self.ARCHIVE_PAGE_BUTTON = (
            By.XPATH,
            '//div[text()="Archived classes"]'
        )

        self.CLASSROOM_MENU = (By.XPATH, '//button[@data-tooltip-id="tt-i1"]')

        self.COURSE_DETAILS_BUTTON = (
            By.XPATH,
            '//ol//div[1]/div[4]/h2//button'
        )

        self.COURSE_TILE = (By.XPATH, '//h2[@class="prWPdf"]')

        self.DELETE_BUTTON = (By.XPATH, '//span[text()="Delete"]')

        self.DIALOG_DELETE_BUTTON = (
            By.XPATH,
            '//div[3]/div[2]//span[text()="Delete"]'
        )
