from selenium.webdriver.common.by import By


class BaseLocators:
    def __init__(self, config):
        self.config = config

        self.CLASSES_BUTTON = (By.XPATH, '//a//div[text()="Classes"]')

        self.CLASSWORK_BUTTON = (
            By.XPATH,
            '//div[@class="R2tE8e VHRSDf"]//a[@guidedhelpid="classworkTab"]'
        )

        self.GOT_IT_BUTTON = (By.XPATH, '//button[text()=" Got it "]')

        self.GUIDE_DIALOG = (By.XPATH, '//div[@id="inproduct-guide-modal"]')

        self.GUIDE_DIALOG_EXIT_BUTTON = (
            By.XPATH,
            '//button[@data-iph-nextstep="__dismiss__"]'
        )

        self.MAIN_MENU_BUTTON = (
            By.XPATH,
            '//button[@data-tooltip-id="tt-i1"]'
        )

        self.NEXT_BUTTON = (By.XPATH, '//button[text()=" Next "]')

        self.PEOPLE_BUTTON = (
            By.XPATH,
            '//div[@class="R2tE8e VHRSDf"]//a[@guidedhelpid="studentTab"]'
        )
