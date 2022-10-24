from selenium.webdriver.common.by import By

from core.locators.base_locators import BaseLocators


class LoginLocators(BaseLocators):
    def __init__(self, test_config):
        super().__init__(test_config)

        self.test_config = test_config

        self.CREATE_ACCOUNT_BUTTON = (
            By.XPATH,
            '//div[@class="XOrBDc"]//span[@class="VfPpkd-vQzf8d"]'
        )

        self.ENGLISH_LANGUAGE = (
            By.XPATH,
            '//*[@id="lang-chooser"]/div[1]/div[2]/ul[1]/li[11]'
        )

        self.EMAIL_FIELD = (By.XPATH, '//*[@id="identifierId"]')

        self.EMAIL_LINK = (By.XPATH, '//div[@class="KTeGk"]')

        self.EMPTY_LOGIN_FIELD = (
            By.XPATH,
            '//div[contains (@class, "QBQrY zKHdkd")]'
            '//div[@class="AxOyFc snByac"]'
        )

        self.EMPTY_PASSWORD_FIELD = (
            By.XPATH,
            '//div[@id="password"]//div[@class="AxOyFc snByac"]'
        )

        self.FORGOT_EMAIL_BUTTON = (By.XPATH, '//div[@class="PrDSKc"]/button')

        self.FORGOT_PASSWORD_BUTTON = (
            By.XPATH,
            '//div[@class="XOrBDc"]//button/span'
        )

        self.LANGUAGE_SELECTOR = (By.XPATH, '//*[@id="lang-chooser"]')

        self.LOGIN_ERROR_MESSAGE = (By.XPATH, '//div[@class="o6cuMc"]')

        self.LOGIN_NEXT_BUTTON = (By.XPATH, '//span[text()="Next"]')

        self.PASSWORD_FIELD = (By.XPATH, '//div[@id="password"]//input')

        self.PASSWORD_ERROR_MESSAGE = (
            By.XPATH,
            '//div[@class="OyEIQ uSvLId"]//span'
        )

        self.SHOW_PASSWORD_CHECKBOX = (
            By.XPATH,
            '//div[@class="d3GVvd jGAaxb"]'
        )
