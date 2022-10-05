from selenium.webdriver.common.by import By


class CoursePageLocators:
    def __init__(self, test_config):
        # super().__init__(test_config)
        #
        # self.test_config = test_config

        self.ALERTDIALOG = (By.XPATH, '//div[@role="alertdialog"]')

        self.ANNOUNCEMENT_POPUP = (By.XPATH, '//div[@id="inproduct-guide-modal"]')

        self.CLASSWORK_BUTTON = (
            By.XPATH,
            '//div[@class="R2tE8e VHRSDf"]//a[text()="Classwork"]'
        )

        self.CLOSE_BUTTON = (By.XPATH, '//div[@role="button" and contains (@class, "ARrCac DKmd5 ")]')

        self.COURSE_BUTTON = (By.XPATH, '//div[@class="R4EiSb"]')

        self.GOT_IT = (
            By.XPATH,
            '//div[@id="inproduct-guide-modal"]//button'
        )

        self.NEXT_BUTTON = (By.XPATH, '//div[@id="inproduct-guide-modal"]//button')

        self.PEOPLE_BUTTON = (By.XPATH, '//div[@class="R2tE8e VHRSDf"]//a[text()="People"]')

        self.SAVE_BUTTON = (
            By.XPATH,
            '//*[@id="yDmH0d"]/div[11]/div/div[2]/div[2]/div[3]//div/button'
        )

        self.SELECT_OPTION = (
            By.XPATH,
            '//*[@id="ow168"]/div[2]/div[2]/div[4]/div/div/button/span'
        )

        self.STREAM_OPTIONS = (
            By.XPATH,
            '//p[text()="Stream"]/..//div[@role="listbox"]'
        )

        self.STREAM_SETTINGS_BUTTON = (
            By.XPATH,
            '//span[text()="Stream settings"]'
        )
