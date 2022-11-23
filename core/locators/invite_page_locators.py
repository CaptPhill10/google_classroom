from selenium.webdriver.common.by import By
from core.locators.base_locators import BaseLocators


class InvitePageLocators(BaseLocators):
    def __init__(self, test_config):
        super().__init__(test_config)

        self.test_config = test_config

        self.DIALOG_INVITE_BUTTON = (
            By.XPATH,
            '//div[@role="dialog"]//div[@role="button" and @data-id="EBS5u"]'
        )

        self.DIALOG_PEOPLE_EMAIL = (
            By.XPATH,
            '//div[@role="dialog"]//input[@role="combobox"]'
        )

        self.DIALOG_SELECT_FIRST_PERSON = (
            By.XPATH,
            '//div[@role="dialog"]//ul[@role="listbox"]/div[1]'
        )

        self.INVITE_STUDENT_BUTTON = (
            By.XPATH,
            '//button[@aria-label="Invite students"]'
        )

        self.INVITE_TEACHER_BUTTON = (
            By.XPATH,
            '//button[@data-tooltip-id="pK81de2"]'
        )

        self.STUDENT_NAME = (
            By.XPATH,
            '(//span[@class="g2DEGd KwqU3e QRiHXd"]/span)[1]'
        )

        self.TEACHER_INVITED = (
            By.XPATH,
            '//table[@class="XNIQbd Oo2pXc"]'
            '//span[@class="IMvYId pXwmie"]'
        )

        self.TEACHER_NAME = (
            By.XPATH,
            '(//table[@class="XNIQbd Oo2pXc"]'
            '//span[@class="sCv5Q asQXV"])[2]'
        )
