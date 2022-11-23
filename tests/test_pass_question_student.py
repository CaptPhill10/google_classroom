import allure
import pytest
from allure_commons.types import AttachmentType
from datetime import datetime
from core.pages.account_page import AccountPage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.gmail_page import GmailPage
from core.pages.login_page import LoginPage
from core.util.constants import Constants

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(16),
    pytest.mark.xdist_group(name="Question"),
    pytest.mark.pass_question,
    pytest.mark.question_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Pass Question Student - " + dt_string),
]


@pytest.fixture(scope="module")
def login_page(driver, test_config):

    login = LoginPage(driver, test_config)
    login.open_main_page()
    login.do_login(
        Constants.QUESTION_STUDENT_LOGIN,
        Constants.QUESTION_STUDENT_PASSWORD
    )

    account = AccountPage(driver, test_config)

    yield account


@allure.sub_suite("01. Student Gmail")
class TestStudentGmail:
    @pytest.fixture(scope="class")
    def invitation(self, driver, test_config, login_page, text_data):

        account = AccountPage(driver, test_config)

        account.open_gmail()

        gmail = GmailPage(driver, test_config)

        gmail.wait_for_element_clickable(
            element=gmail.search_box,
            wait_time=30
        )
        gmail.search_box.input_text(text_data.SEARCH_KEYWORD_STUDENT)
        gmail.class_invitation_mail.click()
        gmail.wait_for_element(element=gmail.search_term)
        if gmail.show_content_button.visible:
            gmail.show_content()
        gmail.join_class()
        driver.switch_to.window(driver.window_handles[2])

        invitation = ClassroomPage(driver, test_config, text_data)

        yield invitation

        invitation.wait_for_element_clickable(
            element=invitation.join_button,
            wait_time=30
        )
        invitation.join_button.click()
        invitation.wait_for_element_clickable(
            element=invitation.classwork_button,
            wait_time=30
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
class TestStudentCheck:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config, login_page):

        classwork = ClassworkPage(driver, test_config)

        while classwork.announcement_popup.visible:
            classwork.got_it_button.click()
            if not classwork.got_it_button.visible:
                classwork.next_button.click()
            else:
                break

        if classwork.alertdialog.visible:
            classwork.close_button.click()

        yield classwork

        if not classwork.assigned_task.visible:
            driver.refresh()

        classwork.wait_for_element_clickable(element=classwork.assigned_task)
        classwork.assigned_task.click()

        if not classwork.assigned_task_view_button.visible:
            driver.refresh()
            classwork.wait_for_element_clickable(
                element=classwork.assigned_task,
                wait_time=30
            )
            classwork.assigned_task.click()
        classwork.assigned_task_view_button.click()

    @allure.title("Classwork Page is Opened")
    def test_classwork_page_opened(self, classwork, text_data):
        with allure.step("Course Title is displayed"):
            try:
                classwork.wait_for_element(element=classwork.course_title)
                assert classwork.course_title.text == text_data.CLASS_NAME
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Course Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("03. Classwork. Open Question page")
class TestQuestionPage:
    @pytest.fixture(scope="class")
    def question(self, driver, test_config, text_data):
        question = ClassworkPage(driver, test_config)

        while question.announcement_popup.visible:
            question.got_it_button.click()
            if not question.got_it_button.visible:
                question.next_button.click()
            else:
                break

        if question.alertdialog.visible:
            question.close_button.click()

        question.answer_input.input_text(text_data.QUESTION_ANSWER)

        question.hand_in_button.click()

        question.alertdialog_hand_in_button.click()

        if not question.question_status.text == "Turned in":
            driver.refresh()

        yield question

    @allure.title("Pass Question Student")
    def test_student_pass_question(self, question):
        with allure.step("Pass Question by Student"):
            try:
                question.wait_for_element_clickable(
                    element=question.question_status,
                    wait_time=30
                )
                assert question.question_status.text == "Turned in"
            except:
                allure.attach(question.driver.get_screenshot_as_png(),
                              name="Question not done",
                              attachment_type=AttachmentType.PNG)
                assert False
