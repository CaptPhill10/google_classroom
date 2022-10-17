from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType

from core.pages.account_page import AccountPage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.course_page import CoursePage
from core.pages.login_page import LoginPage
from core.data.text_data import TextData
from core.util.constants import Constants

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(13),
    pytest.mark.change_question,
    pytest.mark.question_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Change Question - " + dt_string),
]


@pytest.fixture(scope="module")
def login_page(driver, test_config):

    login = LoginPage(driver, test_config)
    login.open_main_page()
    login.do_login(Constants.VALID_LOGIN, Constants.VALID_PASSWORD)

    account = AccountPage(driver, test_config)

    yield account


@allure.sub_suite("01. Classroom Page")
class TestClassPage:
    @pytest.fixture(scope="class")
    def classroom(self, driver, test_config, login_page):

        account = AccountPage(driver, test_config)

        account.open_classroom()
        classroom = ClassroomPage(driver, test_config)

        if classroom.dialog_window.visible:
            classroom.wait_for_element(classroom.dialog_continue_button)
            classroom.dialog_continue_button.click()

        yield classroom

        classroom.course_button.click()

        course = CoursePage(driver, test_config)

        while course.got_it_button.visible:
            course.got_it_button.click()

        course.wait_for_element_clickable(element=course.classwork_button)
        course.classwork_button.click()

    @allure.title("Classroom page is opened")
    def test_is_classroom_page(self, classroom):
        with allure.step("Classroom title is displayed"):
            try:
                classroom.wait_for_element(
                    element=classroom.classroom_page_header
                )
                assert classroom.classroom_page_header.text == "Classroom"
            except:
                allure.attach(classroom.driver.get_screenshot_as_png(),
                              name="Classroom title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("02. Classwork Page")
class TestChangeTopic:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config):
        classwork = ClassworkPage(driver, test_config)

        yield classwork

        classwork.question_settings_button.click()
        classwork.wait_for_element_clickable(element=classwork.edit_button)

        if not classwork.edit_button.visible:
            driver.refresh()
            classwork.assignment_settings_button.click()
            classwork.wait_for_element_clickable(element=classwork.edit_button)

        classwork.edit_button.click()

    @allure.title("Classwork Page is Opened")
    def test_classwork_page_opened(self, classwork):
        with allure.step("Course Title is displayed"):
            try:
                classwork.wait_for_element(element=classwork.course_title)
                assert classwork.course_title.text == TextData.CLASS_NAME
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Course Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("03. Change Question")
class TestQuestionPage:
    @pytest.fixture(scope="class")
    def question(self, driver, test_config):
        question = ClassworkPage(driver, test_config)
        question.question_title.input_text(TextData.NEW_QUESTION)

        attribute_value = question.post_button.get_attribute("tabindex")
        if attribute_value == "0":
            question.post_button.click()
        else:
            while attribute_value != "0":
                print(attribute_value)
                attribute_value = \
                    question.post_button.get_attribute("tabindex")
                print(attribute_value)
                if attribute_value == "0":
                    question.post_button.click()

        if not question.changed_other_name.text == TextData.NEW_QUESTION:
            driver.refresh()

        yield question

    @allure.title("Change Question")
    def test_change_question_topic(self, question):
        with allure.step("Changed Question is displayed"):
            try:
                assert question.changed_other_name.text == \
                       TextData.NEW_QUESTION
            except:
                allure.attach(question.driver.get_screenshot_as_png(),
                              name="Changed Question not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False
