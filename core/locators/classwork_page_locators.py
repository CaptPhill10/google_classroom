from selenium.webdriver.common.by import By


class ClassworkPageLocators:
    def __init__(self, test_config):
        # super().__init__(test_config)
        #
        # self.test_config = test_config

        self.ADD_BUTTON = (
            By.XPATH,
            '//*[@id="yDmH0d"]//div[3]/div//span[text()="Add"]'
        )

        self.ADD_VIDEO_BUTTON = (By.XPATH, '//*[@id="ibP6qb"]//footer//button')

        self.ASSIGN_BUTTON = (By.XPATH, '//span[text()="Assign"]')

        self.ASSIGNMENT_BUTTON = (
            By.XPATH, '//li//span[text()="Assignment"]'
        )

        self.ASSIGNMENT_INSTRUCTIONS = (By.XPATH, '//div[@id="T2Ybvb0"]')

        self.ASSIGNMENT_TITLE_FIELD = (
            By.XPATH, '//div[@class="Y6Mzcf Wic03c"]/textarea'
        )

        self.ATTACH_VIDEO_BUTTON = (
            By.XPATH, '//button[@aria-label="Add YouTube video"]'
        )

        self.CLOSE_BUTTON = (By.XPATH, '//span[text()="Close"]')

        self.CREATE_BUTTON = (
            By.XPATH,
            '//div[@class="VfPpkd-Jh9lGc"]/..//span[text()="Create"]'
        )

        self.DUE_DATE = (By.XPATH, '//span[@class="BUagKb tLDEHd"]')

        self.DUE_DATE_FIELD = (By.XPATH, '//div[@class="RPt7lf dKKcxf"]')

        self.GOT_IT_BUTTON = (
            By.XPATH, '//button[@class="iph-button"]'
        )

        # self.NEXT_MONTH = (By.XPATH, '//button[@title = "Next month"]')

        self.QUIZ_ASSIGNMENT = (By.XPATH, '//li//span[text()="Quiz assignment"]')

        self.SEARCH_BUTTON = (By.XPATH, '//*[@id="ibP6qb"]//button')

        self.SEARCH_VIDEO_FIELD = (By.XPATH, '//form//*[@id="search"]')

        self.SELECT_DATE = (By.XPATH, '//tbody//td[@class="XaepId-gElRsf"]')

        self.SELECT_TOPIC = (By.XPATH, '//li[@data-value="Multiplication table"]')

        self.TOPIC_BUTTON = (By.XPATH, '//*[@id="c24"]//ul/li[7]')\

        self.TOPIC_FIELD = (By.XPATH, '//div[@class="VfPpkd-TkwUic"]')

        self.TOPIC_NAME = (By.XPATH, '//h2[contains(text(), "Multi")]')

        self.TOPIC_NAME_FIELD = (By.XPATH, '//input')
