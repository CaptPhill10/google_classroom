from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType

from core.pages.account_page import AccountPage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.gmail_page import GmailPage
from core.pages.googleform_page import GoogleformPage
from core.pages.login_page import LoginPage
from core.util.constants import Constants
from core.data.text_data import TextData


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(7),
    pytest.mark.pass_quiz_st,
    pytest.mark.quiz_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Pass Quiz Student - " + dt_string),
]


@pytest.fixture(scope="module")
def login_page(driver, test_config):

    login = LoginPage(driver, test_config)
    login.open_main_page()
    login.do_login(Constants.STUDENT_LOGIN, Constants.STUDENT_PASSWORD)

    account = AccountPage(driver, test_config)

    yield account


@allure.sub_suite("01. Student Gmail")
class TestStudentGmail:
    @pytest.fixture(scope="class")
    def invitation(self, driver, test_config, login_page):

        account = AccountPage(driver, test_config)

        account.open_gmail()

        gmail = GmailPage(driver, test_config)

        gmail.search_box.input_text(TextData.SEARCH_KEYWORD)
        gmail.class_invitation_mail.click()
        gmail.wait_for_element(element=gmail.search_term, wait_time=10)
        if gmail.show_content_button.visible:
            gmail.show_content_button.click()
        gmail.join_to_class.click()
        driver.switch_to.window(driver.window_handles[2])

        invitation = ClassroomPage(driver, test_config)

        yield invitation

        invitation.join_button.click()
        invitation.wait_for_element_clickable(
            element=invitation.classwork_button
        )
        invitation.classwork_button.click()

    @allure.title("Check Student Gmail")
    def test_student_classroom_join(self, invitation):
        with allure.step("Invitation page is opened"):
            try:
                invitation.wait_for_element(element=invitation.dialog_header)
                assert invitation.dialog_header.text == "Join class?"
            except:
                allure.attach(invitation.driver.get_screenshot_as_png(),
                              name="Invitation page not opened",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("02. Check in Classwork")
class TestClassworkPage:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config, login_page):

        classwork = ClassworkPage(driver, test_config)

        yield classwork

        while not classwork.assigned_task.visible:
            driver.refresh()

        classwork.wait_for_element_clickable(element=classwork.assigned_task)
        classwork.assigned_task.click()
        classwork.assigned_task_view_button.click()

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


@allure.sub_suite("03. Classwork. Open Quiz page")
class TestQuizPage:
    @pytest.fixture(scope="class")
    def quiz(self, driver, test_config):
        quiz = ClassworkPage(driver, test_config)
        driver.switch_to.window(driver.window_handles[-1])

        yield quiz

        quiz.wait_for_element_clickable(element=quiz.google_quiz)
        quiz.google_quiz.click()
        window_after = driver.window_handles[3]
        driver.switch_to.window(window_after)

    @allure.title("Quiz page is opened")
    def test_task_opened(self, quiz):
        with allure.step("Quiz page is opened"):
            try:
                quiz.wait_for_element(element=quiz.your_work_label)
                assert quiz.your_work_label.text == "Your work"
            except:
                allure.attach(quiz.driver.get_screenshot_as_png(),
                              name="Quiz page not opened",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("04. Pass Google Quiz")
class TestGoogleformPage:
    @pytest.fixture(scope="class")
    def googleform(self, driver, test_config):
        googleform = GoogleformPage(driver, test_config)

        googleform.first_answer_input.input_text("28")
        googleform.second_answer_input.input_text("13")

        yield googleform

        googleform.wait_for_element_clickable(
            element=googleform.submit_button
        )
        googleform.submit_button.click()
        previous_window = driver.window_handles[2]
        driver.switch_to.window(previous_window)

    @allure.title("Pass First Answer")
    def test_first_answer_text(self, googleform):
        with allure.step("Pass First Question in Google Quiz"):
            try:
                first_answer = \
                    googleform.first_answer_input.get_attribute(
                        "data-initial-value"
                    )
                assert first_answer == "28"
            except:
                allure.attach(googleform.driver.get_screenshot_as_png(),
                              name="First Question not passed in Googleform",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Check Second Answer")
    def test_second_answer_text(self, googleform):
        with allure.step("Pass Second Question in Google Quiz"):
            try:
                second_answer = \
                    googleform.second_answer_input.get_attribute(
                        "data-initial-value"
                    )
                assert second_answer == "13"
            except:
                allure.attach(googleform.driver.get_screenshot_as_png(),
                              name="Second Question not passed in Googleform",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("05. Mark Quiz as Done")
class TestMarkDonePage:
    @pytest.fixture(scope="class")
    def quiz(self, driver, test_config):
        quiz = ClassworkPage(driver, test_config)

        quiz.mark_as_done.click()
        quiz.wait_for_element_clickable(element=quiz.alertdialog_mark_as_done)
        quiz.alertdialog_mark_as_done.click()

        yield quiz

    @allure.title("Mark Quiz as Done")
    def test_student_classwork_do_task(self, quiz):
        with allure.step("Mark Quiz as Done"):
            try:
                quiz.wait_for_element_clickable(element=quiz.unsubmit_button)
                assert quiz.unsubmit_button.visible
            except:
                allure.attach(quiz.driver.get_screenshot_as_png(),
                              name="Quiz not done",
                              attachment_type=AttachmentType.PNG)
                assert False
