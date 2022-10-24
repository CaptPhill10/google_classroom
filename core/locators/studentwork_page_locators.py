from selenium.webdriver.common.by import By

from core.locators.base_locators import BaseLocators


class StudentworkPageLocators(BaseLocators):
    def __init__(self, test_config):
        super().__init__(test_config)

        self.test_config = test_config

        self.ADD_GRADE_BUTTON = (By.XPATH, '//div[@class="QRiHXd gRisWe"]')

        self.ALERTDIALOG_RETURN_BUTTON = (
            By.XPATH,
            '//div[@role="alertdialog"]'
            '//div[@class="OE6hId J9fJmf"]'
            '//div[@data-id="EBS5u"]'
        )

        self.ATTACHMENT_LINK = (
            By.XPATH,
            '//a[contains (@aria-label, "Attachment")]'
        )

        self.GRADE_POINTS = (
            By.XPATH,
            '//span[@class="Y5vSD vU2BTc CHXfbe RMcyD"]/span[@class="PazDv"]'
        )

        self.GRADED_LABEL = (
            By.XPATH,
            '//div[@class="IMvYId Y5vSD"]/span[contains (text(), "ed")]'
        )

        self.INPUT_GRADE_BOX = (
            By.XPATH,
            '//table[@role="grid"]//tbody//input[@class="whsOnd zHQkBf"]'
        )

        self.POST_COMMENT = (By.XPATH, '//div[@aria-label="Post"]')

        self.PRIVATE_COMMENT_FIELD = (By.XPATH, '//*[@id=":0.t"]')

        self.PUBLISHED_COMMENT = (
            By.XPATH,
            '//div[@class="VSWCL tLDEHd"]//span'
        )

        self.RETURN_BUTTON = (
            By.XPATH,
            '//div[@class="QRiHXd f5Kwpe"]'
            '//button[contains (@class, "bDxw8b")]'
        )

        self.STUDENT_ANSWER = (
            By.XPATH,
            '//div[@class="lziZub jZrWoe"]/span'
        )
