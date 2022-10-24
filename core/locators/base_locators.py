from selenium.webdriver.common.by import By


class BaseLocators:
    def __init__(self, test_config):
        self.test_config = test_config

        self.ALERTDIALOG = (By.XPATH, '//div[@role="alertdialog"]')

        self.ANNOUNCEMENT_POPUP = (By.ID, 'inproduct-guide-modal')

        self.CLASSES_BUTTON = (By.XPATH, '//a//div[text()="Classes"]')

        self.CLASSWORK_BUTTON = (
            By.XPATH,
            '//div[@class="R2tE8e VHRSDf"]//a[@guidedhelpid="classworkTab"]'
        )

        self.CLOSE_BUTTON = (
            By.XPATH,
            '//div[@role="button"]//span[text()="Close"]'
        )

        self.CUSTOMIZE_RIBBON_BUTTON = (
            By.XPATH,
            '//div[@role="button" and contains (@class, "uArJ5e cd29Sd")]'
        )

        self.DIALOG_CONTINUE_BUTTON = (By.XPATH, '//span[text()="Continue"]')

        self.DIALOG_WINDOW = (By.XPATH, '//div[@role="dialog"]')

        self.GOT_IT_BUTTON = (
            By.XPATH,
            '//button[@data-iph-nextstep="__dismiss__"]'
        )

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
