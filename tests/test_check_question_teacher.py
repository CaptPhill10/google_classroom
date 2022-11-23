import allure
import pytest
from allure_commons.types import AttachmentType
from datetime import datetime
from core.pages.account_page import AccountPage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.course_page import CoursePage
from core.pages.gmail_page import GmailPage
from core.pages.login_page import LoginPage
from core.pages.studentwork_page import StudentworkPage
from core.util.constants import Constants

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(17),
    pytest.mark.xdist_group(name="Question"),
    pytest.mark.check_question,
    pytest.mark.question_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Check Question Teacher - " + dt_string),
]


@pytest.fixture(scope="module")
def login_page(driver, test_config):

    login = LoginPage(driver, test_config)
    login.open_main_page()
    login.do_login(
        Constants.QUESTION_TEACHER_LOGIN,
        Constants.QUESTION_TEACHER_PASSWORD
    )

    account = AccountPage(driver, test_config)

    yield account


@allure.sub_suite("01. Teacher Gmail")
class TestTeacherGmail:
    @pytest.fixture(scope="class")
    def invitation(self, driver, test_config, login_page, text_data):

        account = AccountPage(driver, test_config)

        account.open_gmail()

        gmail = GmailPage(driver, test_config)

        gmail.wait_for_element_clickable(
            element=gmail.search_box,
            wait_time=30
        )
        gmail.search_box.input_text(text_data.SEARCH_KEYWORD_TEACHER)
        gmail.teacher_invitation_mail.click()
        gmail.wait_for_element(element=gmail.search_term)
        if gmail.show_content_button.visible:
            gmail.show_content()
        gmail.join_class()
        driver.switch_to.window(driver.window_handles[2])

        invitation = ClassroomPage(driver, test_config, text_data)

        yield invitation

        invitation.wait_for_element_clickable(
            element=invitation.accept_button,
            wait_time=30
        )
        invitation.accept_button.click()

        course = CoursePage(driver, test_config)

        while course.announcement_popup.visible:
            course.got_it_button.click()
            if not course.got_it_button.visible:
                course.next_button.click()
            else:
                break

        if course.alertdialog.visible:
            course.close_button.click()

        course.wait_for_element_clickable(
            element=course.classwork_button,
            wait_time=30
        )
        course.classwork_button.click()

    @allure.title("Check Teacher Gmail")
    def test_teacher_classroom_join(self, invitation):
        with allure.step("Invitation page is opened"):
            try:
                invitation.wait_for_element(
                    element=invitation.teacher_dialog_header,
                    wait_time=30
                )
                assert invitation.teacher_dialog_header.text == \
                       "Co-teach class?"
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

        while classwork.announcement_popup.visible:
            classwork.got_it_button.click()
            if not classwork.got_it_button.visible:
                classwork.next_button.click()
            else:
                break

        if classwork.alertdialog.visible:
            classwork.close_button.click()

        yield classwork

        if not classwork.assigned_task_view_button.visible:
            driver.refresh()
            classwork.wait_for_element_clickable(
                element=classwork.assigned_work
            )
            classwork.assigned_task.click()
            classwork.wait_for_element_clickable(
                element=classwork.assigned_task_view_button
            )

        classwork.wait_for_element_clickable(element=classwork.assigned_task)
        classwork.assigned_task.click()

        if not classwork.assigned_task_view_button.visible:
            driver.refresh()
            classwork.wait_for_element_clickable(
                element=classwork.assigned_work
            )
            classwork.assigned_task.click()
            classwork.wait_for_element_clickable(
                element=classwork.assigned_task_view_button
            )

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


@allure.sub_suite("03. Check Student's answer")
class TestCheckAnswer:
    @pytest.fixture(scope="class")
    def studentwork(self, driver, test_config):

        studentwork = StudentworkPage(driver, test_config)

        while studentwork.announcement_popup.visible:
            studentwork.got_it_button.click()
            if not studentwork.got_it_button.visible:
                studentwork.next_button.click()
            else:
                break

        if studentwork.alertdialog.visible:
            studentwork.close_button.click()

        yield studentwork

    @allure.title("Check Student's answer")
    def test_check_student_answer(self, studentwork, text_data):
        with allure.step("Student's Answer text"):
            try:
                studentwork.wait_for_element_clickable(
                    element=studentwork.student_answer
                )
                assert studentwork.student_answer.text == \
                       text_data.QUESTION_ANSWER
            except:
                allure.attach(studentwork.driver.get_screenshot_as_png(),
                              name="Student's Answer text not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("04. Check Student's answer")
class TestCheckAnswer:
    @pytest.fixture(scope="class")
    def studentwork(self, driver, test_config, text_data):
        studentwork = StudentworkPage(driver, test_config)

        studentwork.wait_for_element_clickable(
            element=studentwork.add_grade_button
        )
        studentwork.add_grade_button.click()
        studentwork.input_grade_box.input_text(text_data.GRADE)
        studentwork.wait_for_element_clickable(
            element=studentwork.return_button,
            wait_time=30
        )
        studentwork.return_button.click()
        studentwork.wait_for_element_clickable(
            element=studentwork.alertdialog_return_button,
            wait_time=30
        )
        studentwork.alertdialog_return_button.click()

        yield studentwork

    @allure.title("Student Grade Points")
    def test_student_grade_points(self, studentwork):
        with allure.step("Student Grade Points are added"):
            try:
                studentwork.wait_for_element(element=studentwork.grade_points)
                assert studentwork.grade_points.text == \
                       "100 points out of a possible 100"
            except:
                allure.attach(studentwork.driver.get_screenshot_as_png(),
                              name="Student Grade Points not added",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Student Graded")
    def test_student_graded(self, studentwork):
        with allure.step("Student Task Status"):
            try:
                studentwork.wait_for_element(element=studentwork.graded_label)
                assert studentwork.graded_label.text == "Marked"
            except:
                allure.attach(studentwork.driver.get_screenshot_as_png(),
                              name="Student Status not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False
