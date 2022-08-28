from selenium.webdriver.common.by import By


class AccountLocators:
    def __init__(self, test_config):
        # super().__init__(test_config)
        #
        # self.test_config = test_config

        self.GOOGLE_APPS_BUTTON = (By.XPATH, '//a[@aria-label="Google apps"]')

        self.UNORDERED_LIST = (By.XPATH, '//ul[@jsname="k77Iif"]')

        self.CLASSROOM_BUTTON = (By.XPATH, '//span[text()="Classroom"]')
