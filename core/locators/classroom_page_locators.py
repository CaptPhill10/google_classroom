from core.locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By


class ClassroomLocators(BaseLocators):
    def __init__(self, test_config):
        super().__init__(test_config)

        self.test_config = test_config

        self.AGREE_CHECKBOX = (By.ID, 'c3')

        self.ARCHIVE_COURSE_BUTTON = (By.XPATH, '//li/span[text()="Archive"]')

        self.ARCHIVE_PAGE_BUTTON = (
            By.XPATH,
            '//div[text()="Archived classes"]'
        )

        self.CLASS_NAME_FIELD = (By.XPATH, '//*[@id="c7"]')

        self.CLASSROOM_PAGE_HEADER = (
            By.XPATH,
            '//span[@class="IqJTee" and text()="Classroom"]'
        )

        self.CONTINUE_BUTTON = (
            By.XPATH,
            '//div[@role="alertdialog"]/div[3]/div[2]'
        )

        self.CONTINUE_BUTTON_2 = (
            By.XPATH,
            '//div[@role="alertdialog"]/div[3]/div[2]'
        )

        self.COURSE_BUTTON = (By.XPATH, '//div[@class="R4EiSb"]')

        self.COURSE_DETAILS_BUTTON = (
            By.XPATH,
            '//div[3]/h2/div/div/div[1]/button'
        )

        self.CREATE_BUTTON = (
            By.XPATH,
            '//div[@role="alertdialog"]/div[3]/div[2]'
        )

        self.CREATE_CLASS_BUTTON = (
            By.XPATH,
            '//li[@role="menuitem"]//span[text()="Create class"]'
        )

        self.CREATE_JOIN_BUTTON = (By.XPATH, '//button[@jsname="mSMdM"]')

        self.DIALOG_ARCHIVE_BUTTON = (
            By.XPATH,
            '//div[@class="OE6hId J9fJmf"]//span[text()="Archive"]'
        )

        self.DIALOG_CONTINUE_BUTTON = (By.XPATH, '//span[text()="Continue"]')

        self.DIALOG_HEADER = (By.XPATH, '//h1[contains (text(), "Join")]')

        self.DIALOG_WINDOW = (By.XPATH, '//div[@role="dialog"]')

        self.JOIN_BUTTON = (By.XPATH, '//form//button[text()="Join"]')

        self.ROOM_FIELD = (By.XPATH, '//*[@id="c14"]')

        self.SECTION_FIELD = (By.XPATH, '//*[@id="c9"]')

        self.SUBJECT_FIELD = (By.XPATH, '//*[@id="c12"]')
