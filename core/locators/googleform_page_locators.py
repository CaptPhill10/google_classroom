from selenium.webdriver.common.by import By

from core.locators.base_locators import BaseLocators


class GoogleformPageLocators(BaseLocators):
    def __init__(self, test_config):
        super().__init__(test_config)

        self.test_config = test_config

        self.ADD_ANSWER_FIELD = (By.XPATH, '//div[@class="XBufad "]//input')

        self.ADD_QUESTION_BUTTON = (
            By.XPATH,
            '//*[@id="SchemaEditor"]//div[@guidedhelpid="addQuestionGH"]'
        )

        self.ANSWER_KEY = (By.XPATH, '//span[text()="Answer key"]')

        self.ANSWER_SUBMITTED_TIME = (
            By.XPATH,
            '//div[@class="phD6Pe" and contains (text(), "Submitted")]'
        )

        self.CONFIGURE_OPTION = (
            By.XPATH,
            '//div[@role="listbox" and contains(@class, "llrsB")]'
        )

        self.DONE_BUTTON = (By.XPATH, '//span[text()="Done"]')

        self.EDIT_FORM_BUTTON = (
            By.XPATH,
            '//div[@class="HMRMj"]/div[@role="button"]'
        )

        self.FIRST_ANSWER_INPUT = (
            By.XPATH,
            '(//div[@role="listitem"]//input)[1]'
        )

        self.FIRST_ANSWER_TEXT = (
            By.XPATH,
            '//div[@class="xMZTse Ih4Dzb b6DnMe"]'
            '/div[contains (@class, "yqQS1")]'
        )

        self.FIRST_QUESTION_TITLE = (By.XPATH, '//*[@id="T2Ybvb2"]')

        self.INDIVIDUAL_TAB = (
            By.XPATH,
            '//div[@aria-label="Individual response view"]'
        )

        self.INPUT_ANSWER = (
            By.XPATH,
            '//div[@class="NP6Jz wiS4Xc-bN97Pc"]//input'
        )

        self.MARK_AS_INCORRECT_CHECKBOX = (By.XPATH, '//div[@class="vpc2Xb"]')

        self.QUESTION_NAME = (By.XPATH, '//*[@id="T2Ybvb4"]')

        self.QUIZ_TITLE = (By.XPATH, '//*[@id="T2Ybvb0"]')

        self.REQUIRED_RADIO = (
            By.XPATH,
            '//div[@class="Vjsz1b"]//div[@class="E7QdY espmsb"]'
        )

        self.RESPONSES_BUTTON = (
            By.XPATH,
            '//div[@role="tab" and @aria-controls="ResponsesView"]'
        )

        self.SECOND_ANSWER_INPUT = (
            By.XPATH,
            '(//div[@role="listitem"]//input)[2]'
        )

        self.SECOND_ANSWER_TEXT = (
            By.XPATH,
            '//div[@class="xMZTse Ih4Dzb BJnx9d"]'
            '/div[contains (@class, "yqQS1")]'
        )

        self.SECOND_ANSWER_KEY = (
            By.XPATH,
            '(//span[text()="Answer key"])[2]'
        )

        self.SECOND_CONFIGURE_OPTION = (
            By.XPATH,
            '(//span[text()="Multiple choice"])[2]'
        )

        self.SECOND_QUESTION_NAME = (By.XPATH, '//*[@id="T2Ybvb8"]')

        self.SECOND_QUESTION_TITLE = (By.XPATH, '//*[@id="T2Ybvb6"]')

        self.SECOND_REQUIRED_RADIO = (
            By.XPATH,
            '(//div[@class="Vjsz1b"]//div[@class="E7QdY espmsb"])[2]'
        )

        self.SECOND_SELECT_OPTION = (
            By.XPATH,
            '(//div[@role="option"]//span[text()="Short answer"])[2]'
        )

        self.SELECT_OPTION = (
            By.XPATH,
            '//div[@role="option"]//span[text()="Short answer"]'
        )

        self.SUBMIT_BUTTON = (
            By.XPATH,
            '//div[@class="lRwqcd"]/div[@role="button"]'
        )
