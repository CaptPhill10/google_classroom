from selenium.webdriver.common.by import By

from core.locators.base_locators import BaseLocators


class ClassworkPageLocators(BaseLocators):
    def __init__(self, test_config):
        super().__init__(test_config)

        self.test_config = test_config

        self.ADD_BUTTON = (
            By.XPATH,
            '//div[@role="alertdialog"]/div[3]/div[2]'
        )

        self.ADD_LINK_BUTTON = (
            By.XPATH,
            '//div[@class="OE6hId J9fJmf"]//span[text()="Add link"]'
        )

        self.ADD_VIDEO_BUTTON = (
            By.XPATH,
            '//*[@id="ibP6qb"]//footer//button'
        )

        self.ALERTDIALOG_HAND_IN_BUTTON = (
            By.XPATH,
            '//div[@role="alertdialog"]//div[contains (@class, "M9Bg4d")]'
        )

        self.ALERTDIALOG_INPUT = (
            By.XPATH,
            '//div[@role="alertdialog"]//input'
        )

        self.ALERTDIALOG_MARK_AS_DONE = (
            By.XPATH,
            '//div[@class="OE6hId J9fJmf"]//span[contains (text(), "Mark")]'
        )

        self.ALERTDIALOG_RENAME_BUTTON = (
            By.XPATH,
            '//div[@role="alertdialog"]/div[3]/div[2]'
        )

        self.ANSWER_INPUT = (
            By.XPATH,
            '//div[@class="Y6Mzcf Wic03c"]/textarea'
        )

        self.ASSIGNED_TASK = (By.XPATH, '//ol[@class="Xzp3fc"]/li[1]')

        self.ASSIGNED_TASK_VIEW_BUTTON = (
            By.XPATH,
            '//ol[@class="Xzp3fc"]/li[1]'
            '//a[@class="WpHeLc VfPpkd-mRLv6 VfPpkd-RLmnJb"]'
        )

        self.ASSIGNED_WORK = (By.XPATH, '//div[@class="SFCE1b"]')

        self.ASSIGNMENT_BUTTON = (
            By.XPATH,
            '//li[@role="menuitem"]/span[text()="Assignment"]'
        )

        self.ASSIGNMENT_NAME = (By.XPATH, '//textarea[@aria-label="Title"]')

        self.ASSIGNMENT_SETTINGS_BUTTON = (
            By.XPATH,
            '//div[contains (@class, "u73Apc")]'
            '//div[@aria-label="Assignment options"]'
        )

        self.ATTACH_LINK_BUTTON = (
            By.XPATH,
            '//button[@aria-label="Add link"]'
        )

        self.ATTACHMENT_LINK = (By.XPATH, '//div[@class="luto0c"]')

        self.ATTACH_VIDEO_BUTTON = (
            By.XPATH, '//button[@aria-label="Add YouTube video"]'
        )

        self.CHANGED_OTHER_NAME = (
            By.XPATH,
            '//ol[@class="Xzp3fc"]/li[1]//div[@class="lio3ib"]//span'
        )

        self.CHANGED_ASSIGNMENT_NAME = (
            By.XPATH,
            '//div[@class="lio3ib"]//span[contains (text(), "Trigon")]'
        )

        self.COURSE_TITLE = (By.XPATH, '//span[@id="UGb2Qe"]')

        self.CREATE_BUTTON = (
            By.XPATH,
            '//div[@class="VfPpkd-dgl2Hf-ppHlrf-sM5MNb"]'
            '/..//span[text()="Create"]'
        )

        self.CREATE_QUIZ_BUTTON = (By.XPATH, '//div[@class="bxp7vf i3bmcb"]')

        self.DATE_PICKER_BUTTON = (
            By.XPATH,
            '//div[@role="button" and @aria-label="Add due date"]'
        )

        self.DUE_DATE_BUTTON = (
            By.XPATH,
            '//div[@role="button" and @aria-label="No due date"]'
        )

        self.DUE_DATE_FIELD = (
            By.XPATH,
            "//input[@aria-label='Due date']"
        )

        self.EDIT_BUTTON = (By.XPATH,
                            '//span[@aria-label="Edit"]')

        self.FORMS_BUTTON = (
            By.XPATH,
            '//div[contains (@class, "qjTEB")]//div[text()="Forms"]')

        self.GOOGLE_QUIZ = (
            By.XPATH,
            '//div[@class="r0VQac QRiHXd Aopndd "]'
            '//a[contains (@aria-label, "Attachment")]'
        )

        self.HAND_IN_BUTTON = (
            By.XPATH,
            '//div[contains (@class, "YkTkoe")]'
            '//div[contains (@class, "GAU0yc")]'
        )

        self.MARK_AS_DONE = (
            By.XPATH,
            '//aside//div[contains (@class, "Y5sE8d")]'
        )

        self.MATERIAL_ATTACHMENT = (By.XPATH, '//div[@class="F1bQqd"]/a')

        self.MATERIAL_ATTACHMENT_LINK = (
            By.XPATH,
            '//div[@class="t2wIBc"]//a[contains (@aria-label, "Attachment")]'
        )

        self.MATERIAL_BUTTON = (
            By.XPATH,
            '//li[@role="menuitem"]/span[text()="Material"]'
        )

        self.MATERIAL_PAGE_TITLE = (
            By.XPATH,
            '//div[@class="HvC6Tb"]//div[@class="e0prFf"]'
        )

        self.MATERIAL_SETTINGS_BUTTON = (
            By.XPATH,
            '//div[contains (@class, "u73Apc")]'
            '//div[@aria-label="Material options"]'
        )

        self.MATERIAL_TITLE = (By.XPATH, '//textarea[@aria-label="Title"]')

        self.NEXT_MONTH_BUTTON = (
            By.XPATH,
            '//button[@class="XaepId-SKd3Ne XaepId-jx5HS"'
            ' and @title="Next month"]'
        )

        self.OPEN_QUIZ = (By.XPATH, '//div[@class="F1bQqd"]/a')

        self.OTHER_NAME = (
            By.XPATH,
            '//ol[@class="Xzp3fc"]//span[@class="YVvGBb UzbjTd"]'
        )

        self.POST_BUTTON = (By.XPATH, '//div[@jsmodel="hGbFme"]/div[1]')

        self.QUESTION_BUTTON = (
            By.XPATH,
            '//li[@role="menuitem"]/span[text()="Question"]'
        )

        self.QUESTION_SETTINGS_BUTTON = (
            By.XPATH,
            '//div[@class="yOdyF"]//div[@aria-label="Question options"]'
        )

        self.QUESTION_STATUS = (
            By.XPATH,
            '//div[@class="Dy8Cxc QRiHXd"]'
            '//span[@class="u7S8tc YVvGBb"]'
            '//span[contains (text(), "in")]'
        )

        self.QUESTION_TITLE = (By.XPATH, '//textarea[@aria-label="Question"]')

        self.QUIZ_BUTTON = (
            By.XPATH,
            '//li[@role="menuitem"]/span[text()="Quiz assignment"]'
        )

        self.QUIZ_NAME = (By.XPATH, '//textarea[@aria-label="Title"]')

        self.REMOVE_ATTACHMENT = (
            By.XPATH,
            '//div[@class="ZgfM9 QRiHXd"]//span[@class="XuQwKc"]'
        )

        self.RENAME_BUTTON = (
            By.XPATH,
            '//div[@role="menu"]/div[1]/div[1]/span[1]'
        )

        self.SAVE_BUTTON = (By.XPATH, '//div[contains (@class, "ZQXs7e")]')

        self.SEARCH_BUTTON = (By.XPATH, '//*[@id="ibP6qb"]//button')

        self.SEARCH_VIDEO_FIELD = (By.XPATH, '//form//*[@id="search"]')

        self.TASK_TITLE = (By.XPATH, '//div[@class="e0prFf"]')

        self.TOPIC_BUTTON = (
            By.XPATH,
            '//li[@role="menuitem"]/span[text()="Topic"]'
        )

        self.TOPIC_NAME = (By.XPATH, '//h2[@class="PazDv"]')

        self.TOPIC_NAME_FIELD = (
            By.XPATH,
            '//div[@role="alertdialog"]//input'
        )

        self.TOPIC_SETTINGS_BUTTON = (
            By.XPATH,
            '//div[@aria-label="Topic options"]'
        )

        self.UNSUBMIT_BUTTON = (By.XPATH, '//aside//span[text()="Unsubmit"]')

        self.YOUR_WORK_LABEL = (
            By.XPATH,
            '//aside[@class="asCVDb BiaLW"]//span[@class="z3vRcc"]'
        )
