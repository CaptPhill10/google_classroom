from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType

from core.pages.account_page import AccountPage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.gmail_page import GmailPage
from core.pages.login_page import LoginPage
from core.data.text_data import TextData
from core.util.constants import Constants


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(3),
    pytest.mark.assignment_flow,
    pytest.mark.pass_assignment_st,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Pass Assignment Student - " + dt_string),
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


@allure.sub_suite("02. Classwork Page")
class TestClassworkPage:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config, login_page):

        classwork = ClassworkPage(driver, test_config)

        yield classwork

        if not classwork.assigned_task.visible:
            driver.refresh()

        classwork.wait_for_element_clickable(element=classwork.assigned_task)
        classwork.assigned_task.click()
        classwork.assigned_task_view_button.click()

        driver.switch_to.window(driver.window_handles[-1])

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


@allure.sub_suite("03.Task Page")
class TestTaskPage:
    @pytest.fixture(scope="class")
    def task(self, driver, test_config, login_page):
        task = ClassworkPage(driver, test_config)

        yield task

    @allure.title("Task is opened")
    def test_task_opened(self, task):
        with allure.step("Task page is opened"):
            try:
                assert task.your_work_label.text == "Your work"
            except:
                allure.attach(task.driver.get_screenshot_as_png(),
                              name="Task Page not opened",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("04. Mark Task as Done")
class TestMarkDonePage:
    @pytest.fixture(scope="class")
    def assignment(self, driver, test_config):
        assignment = ClassworkPage(driver, test_config)

        assignment.mark_as_done.click()
        assignment.wait_for_element_clickable(
            element=assignment.alertdialog_mark_as_done
        )
        assignment.alertdialog_mark_as_done.click()

        yield assignment

    @allure.title("Mark Assignment as Done")
    def test_student_classwork_do_task(self, assignment):
        with allure.step("Mark Assignment as Done"):
            try:
                assert assignment.unsubmit_button.visible
            except:
                allure.attach(assignment.driver.get_screenshot_as_png(),
                              name="Assignment not done",
                              attachment_type=AttachmentType.PNG)
                assert False
