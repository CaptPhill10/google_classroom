# import core.locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By


class ClassroomLocators:
    def __init__(self, test_config):
        # super().__init__(test_config)
        #
        # self.test_config = test_config

        self.ARCHIVE_COURSE_BUTTON = (By.XPATH, '//li/span[text()="Archive"]')

        self.CLASSES_BUTTON = (By.XPATH, '//a//div[text()="Classes"]')

        self.CLASSROOM_HEADER = (By.XPATH, '//span[@class="IqJTee" and text()="Classroom"]')

        self.COURSE_DETAILS_BUTTON = (By.XPATH, '//div[3]/h2/div/div/div[1]/button')

        self.CREATE_COURSE_BUTTON = (By.XPATH, '//div[@role="button"]//span[text()="Create class"]')

        self.DIALOG_ARCHIVE_BUTTON = (By.XPATH, '//div[@class="OE6hId J9fJmf"]//span[text()="Archive"]')

        self.DIALOG_WINDOW = (By.XPATH, '//div[@role="dialog"]')

        self.AGREE_CHECKBOX = (By.ID, 'c3')

        self.CONTINUE_BUTTON = (By.XPATH, '//div[@class="jzUkrb"]//div[@data-id="EBS5u"]')

        self.CONTINUE_BUTTON_2 = (By.XPATH, '//*[@id="yDmH0d"]/div[8]/div/div[2]/div[3]/div[2]/span/span')

        self.CLASS_NAME_FIELD = (By.XPATH, '//*[@id="c7"]')

        self.CREATE_BUTTON = (By.XPATH, '//*[@id="yDmH0d"]/div[8]/div/div[2]/div[3]/div[2]/span/span')

        self.DIALOG_CONTINUE_BUTTON = (By.XPATH, '//span[text()="Continue"]')

        self.MAIN_MENU_BUTTON = (By.XPATH, '//button[@data-tooltip-id="tt-i1"]')

        self.ROOM_FIELD = (By.XPATH, '//*[@id="c14"]')

        self.SECTION_FIELD = (By.XPATH, '//*[@id="c8"]')

        self.SUBJECT_FIELD = (By.XPATH, '//*[@id="c12"]')
