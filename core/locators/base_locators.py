from selenium.webdriver.common.by import By


class BaseLocators:
    def __init__(self, config):
        self.config = config

        self.MAIN_MENU_BUTTON = (By.XPATH, '//button[@data-tooltip-id="tt-i1"]')

        self.CLASSES_BUTTON = (By.XPATH, '//a//div[text()="Classes"]')
