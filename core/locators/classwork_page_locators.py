from selenium.webdriver.common.by import By


class ClassworkPageLocators:
    def __init__(self, test_config):
        # super().__init__(test_config)
        #
        # self.test_config = test_config

        self.ADD_ANSWER_FIELD = (By.XPATH, '//div[@class="XBufad "]//input')

        self.ADD_ANSWER_OPTION = (By.XPATH, '//div[@class="uEtsdd xkhr8"]')

        self.ADD_BUTTON = (
            By.XPATH,
            '//*[@id="yDmH0d"]//div[3]/div//span[text()="Add"]'
        )

        self.ADD_LINK_BUTTON = (By.XPATH, '//div[@class="OE6hId J9fJmf"]//span[text()="Add link"]')

        self.ADD_QUESTION_BUTTON = (By.XPATH, '//*[@id="SchemaEditor"]//div[@guidedhelpid="addQuestionGH"]')

        self.ADD_VIDEO_BUTTON = (By.XPATH, '//*[@id="ibP6qb"]//footer//button')

        self.ALERTDIALOG = (By.XPATH, '//div[@role="alertdialog"]')

        self.ALERTDIALOG_RENAME_BUTTON = (By.XPATH, '//div[@class="OE6hId J9fJmf"]//span[text()="Rename"]')

        self.ALERTDIALOG_INPUT = (By.XPATH, '//div[@role="alertdialog"]//input')

        self.ANSWER_KEY = (By.XPATH, '//span[text()="Answer key"]')

        self.ANSWER_OPTION_1 = (By.XPATH, '//input[@class="whsOnd zHQkBf"]')

        self.ANSWER_OPTION_2 = (By.XPATH, '(//input[@class="whsOnd zHQkBf"])[2]')

        self.ASK_BUTTON = (By.XPATH, '//div[contains (@class, "qs9Ooe")]')

        self.ASSIGN_BUTTON = (By.XPATH, '//span[text()="Assign"]')

        self.ASSIGNMENT_BUTTON = (
            By.XPATH, '//li//span[text()="Assignment"]'
        )

        self.ASSIGNMENT_EDIT_BUTTON = (By.XPATH, '//span[@aria-label="Edit"]')

        self.ASSIGNMENT_INSTRUCTIONS = (By.XPATH, '//div[@id="T2Ybvb0"]')

        self.ASSIGNMENT_OPTIONS_BUTTON = (By.XPATH, '//div[@class=" lGm3nb"]//div[@aria-label="Assignment options"]')

        self.ASSIGNMENT_TITLE = (By.XPATH, '//div[@class="kByKEb QRiHXd asQXV"]//span')

        self.ATTACH_LINK_BUTTON = (By.XPATH, '//button[@aria-label="Add link"]')

        self.ATTACH_VIDEO_BUTTON = (
            By.XPATH, '//button[@aria-label="Add YouTube video"]'
        )

        self.CLOSE_BUTTON = (By.XPATH, '//span[text()="Close"]')

        self.CONFIGURE_OPTION = (By.XPATH, '//div[@role="listbox" and contains(@class, "llrsB")]')

        self.CREATE_BUTTON = (
            By.XPATH,
            '//div[@class="VfPpkd-Jh9lGc"]/..//span[text()="Create"]'
        )

        self.CREATE_QUIZ_BUTTON = (By.XPATH, '//div[@class="bxp7vf i3bmcb"]')

        self.DESCRIPTION = (By.XPATH, '//div[@role="textbox"]')

        self.DESCRIPTION_TEXT_INPUT = (By.XPATH, '//div[@id="T2Ybvb4"]')

        self.DONE_BUTTON = (By.XPATH, '//span[text()="Done"]')

        self.DUE_DATE = (By.XPATH, '//span[@class="BUagKb tLDEHd"]')

        self.DUE_DATE_FIELD = (By.XPATH, '//div[@class="RPt7lf dKKcxf"]')

        self.FIRST_QUESTION_TITLE = (By.XPATH, '//*[@id="T2Ybvb2"]')

        self.FORMS_BUTTON = (By.XPATH, '//div[contains (@class, "qjTEB")]//div[text()="Forms"]')

        self.GOT_IT_BUTTON = (
            By.XPATH, '//button[@class="iph-button"]'
        )

        self.GUIDE = (By.XPATH, '//*[@id="inproduct-guide-modal"]')

        self.INPUT_ANSWER = (By.XPATH, '//*[@id="SchemaEditor"]//input[@data-initial-value="Correct Answer"]')

        self.LISTBOX_OPTION = (By.XPATH, '//div[@role="option" and @class="MocG8c HZ3kWc LMgvRb"]')

        self.MARK_AS_INCORRECT_CHECKBOX = (By.XPATH, '//div[@class="vpc2Xb"]')

        self.MATERIAL_BUTTON = (By.XPATH, '//li//span[text()="Material"]')

        self.MATERIAL_NAME = (By.XPATH, '//ol[@class="Xzp3fc"]//span[text()="Multiplication table"]')

        self.MATERIAL_TOPIC_FIELD = (By.XPATH, '//div[contains (@class, "TIKlJe")]')

        self.NEW_TOPIC = (By.XPATH, '//a[text()="iPhone 14 Pro Max"]')

        self.NO_THANKS_BUTTON = (By.XPATH, '//button[text()="No, thanks"]')

        self.OKAY_BUTTON = (By.XPATH, '//button[contains(text(), "Ok")]')

        self.OPEN_QUIZ = (By.XPATH, '//div[@class="F1bQqd"]/a')

        self.PEOPLE_BUTTON = (By.XPATH, '(//div[@class="R2tE8e VHRSDf"]//a)[3]')

        self.POPUP = (By.XPATH, '//div[@id="inproduct-guide-modal"]')

        self.POST_BUTTON = (By.XPATH, '//div[contains (@class, "qs9Ooe")]')

        self.QUESTION_BUTTON = (By.XPATH, '//li//span[text()="Question"]')

        self.QUESTION_LISTBOX = (By.XPATH, '//div[@class="TWyWEc"]//div[@role="listbox"]')

        self.QUIZ_ASSIGNMENT = (By.XPATH, '//li//span[text()="Quiz assignment"]')

        # self.QUIZ_ASSIGNMENT_TITLE = (By.XPATH, '//span[text()="Multiplication table test"]')

        self.QUIZ_ASSIGNMENT_TITLE = (By.XPATH, '//div[@class="kByKEb QRiHXd asQXV"]/span')

        self.QUIZ_TITLE = (By.XPATH, '//*[@id="T2Ybvb0"]')

        self.REMOVE_ATTACHMENT = (By.XPATH, '//div[@class="ZgfM9 QRiHXd"]//span[@class="XuQwKc"]')

        self.RENAME_BUTTON = (By.XPATH, '//div[text()="Rename"]')

        self.REQUIRED_RADIO = (By.XPATH, '//div[@class="Vjsz1b"]//div[@class="E7QdY espmsb"]')

        # self.NEXT_MONTH = (By.XPATH, '//button[@title = "Next month"]')

        self.SAVE_BUTTON = (By.XPATH, '//div[contains (@class, "ZQXs7e")]')

        self.SEARCH_BUTTON = (By.XPATH, '//*[@id="ibP6qb"]//button')

        self.SEARCH_VIDEO_FIELD = (By.XPATH, '//form//*[@id="search"]')

        self.SECOND_ANSWER_KEY = (By.XPATH, '(//span[text()="Answer key"])[2]')

        self.SECOND_CONFIGURE_OPTION = (By.XPATH, '(//span[text()="Multiple choice"])[2]')

        self.SECOND_REQUIRED_RADIO = (By.XPATH, '(//div[@class="Vjsz1b"]//div[@class="E7QdY espmsb"])[2]')

        self.SECOND_QUESTION_FIELD = (By.XPATH, '//*[@id="T2Ybvb4"]')

        self.SECOND_QUESTION_TITLE = (By.XPATH, '//*[@id="T2Ybvb6"]')

        self.SECOND_SELECT_OPTION = (By.XPATH, '(//div[@role="option"]//span[text()="Short answer"])[2]')

        self.SELECT_DATE = (By.XPATH, '//tbody//td[@class="XaepId-gElRsf"]')

        self.SELECT_OPTION = (By.XPATH, '//div[@role="option"]//span[text()="Short answer"]')

        self.SELECT_TOPIC = (By.XPATH, '//li[@data-value="Multiplication table"]')

        self.SEND_BUTTON = (By.XPATH, '//div[contains (@class, "CTi8 M9Bg4d")]')

        self.TITLE_FIELD = (
            By.XPATH, '//div[@class="Y6Mzcf Wic03c"]/textarea'
        )

        self.TOPIC = (By.XPATH, '//div[@class="bFjUmb-Wvd9Cc O1l69"]')

        self.TOPIC_BUTTON = (By.XPATH, '//li[@role="menuitem"]/span[text()="Topic"]')\

        self.TOPIC_FIELD = (By.XPATH, '//div[@class="VfPpkd-TkwUic"]')

        self.TOPIC_NAME = (By.XPATH, '//h2[contains(text(), "Multi")]')

        self.TOPIC_NAME_FIELD = (By.XPATH, '//input')

        self.TOPIC_SETTINGS_BUTTON = (By.XPATH, '//h2[contains (text(), "Multi")]/..//div[@class="ClSQxf"]')
