from selenium.webdriver.common.by import By


class CoursePageLocators:
    def __init__(self, test_config):
        # super().__init__(test_config)
        #
        # self.test_config = test_config

        self.STREAM_SETTINGS_BUTTON = (
            By.XPATH,
            '//span[text()="Stream settings"]'
        )

        self.STREAM_OPTIONS = (
            By.XPATH,
            '//p[text()="Stream"]/..//div[@role="listbox"]'
        )

        self.SELECT_OPTION = (
            By.XPATH,
            '//*[@id="ow168"]/div[2]/div[2]/div[4]/div/div/button/span'
        )

        self.SAVE_BUTTON = (
            By.XPATH,
            '//*[@id="yDmH0d"]/div[11]/div/div[2]/div[2]/div[3]//div/button'
        )

        self.GOT_IT = (
            By.XPATH,
            '//div[@id="inproduct-guide-modal"]//button'
        )

        self.CLASSWORK_BUTTON = (
            By.XPATH,
            '//div[@class="R2tE8e VHRSDf"]//a[text()="Classwork"]'
        )
