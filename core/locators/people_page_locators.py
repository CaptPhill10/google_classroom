from selenium.webdriver.common.by import By


class PeoplePageLocators:
    def __init__(self, test_config):
        # super().__init__(test_config)
        #
        # self.test_config = test_config

        self.INVITE_BUTTON = (By.XPATH, '//div[@role="button"]//span[text()="Invite"]')

        self.INVITE_STUDENT_BUTTON = (By.XPATH, '//button[@data-tooltip-id="pK81de1"]')

        self.INVITE_TEACHER_BUTTON = (By.XPATH, '//button[@data-tooltip-id="pK81de2"]')

        self.PEOPLE_EMAIL = (By.XPATH, '//div[@role="dialog"]//input')

        self.PEOPLE_EMAIL_FIELD = (By.XPATH, '//div[@role="listbox"]//span')

        self.PEOPLE_OPTION = (By.XPATH, '//div[@class="AGJxEc"]//div[@class="G1zVib"]')

        self.STUDENT_NAME = (By.XPATH, '//table[@class="XNIQbd DCIKCc"]//span[text()="sherlocktrue@gmail.com"]')

        self.TEACHER_NAME = (By.XPATH, '//table[@class="XNIQbd Oo2pXc"]//span[text()="chrislusttrue@gmail.com"]')
