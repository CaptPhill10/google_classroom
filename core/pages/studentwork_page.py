import allure
from core.base_element import BaseElement
from core.locators.studentwork_page_locators import StudentworkPageLocators
from core.pages.base_page import BasePage


class StudentworkPage(BasePage):
    def __init__(self, driver, test_config):
        super().__init__(driver, test_config)
        self.driver = driver
        self.test_config = test_config
        self.locators = StudentworkPageLocators(test_config=self.test_config)
        self.studentwork_step()

    @allure.step("Studentwork step")
    def studentwork_step(self):
        pass

    @property
    def add_grade_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ADD_GRADE_BUTTON
        )

    @property
    def alertdialog_return_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ALERTDIALOG_RETURN_BUTTON
        )

    @property
    def attachment_link(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.ATTACHMENT_LINK
        )

    @property
    def graded_label(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.GRADED_LABEL
        )

    @property
    def grade_points(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.GRADE_POINTS
        )

    @property
    def input_grade_box(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.INPUT_GRADE_BOX
        )

    @property
    def post_comment(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.POST_COMMENT
        )

    @property
    def private_comment_field(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.PRIVATE_COMMENT_FIELD
        )

    @property
    def published_comment(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.PUBLISHED_COMMENT
        )

    @property
    def return_button(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.RETURN_BUTTON
        )

    @property
    def student_answer(self):
        return BaseElement(
            driver=self.driver,
            locator=self.locators.STUDENT_ANSWER
        )
