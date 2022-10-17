import time
from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType

from core.pages.account_page import AccountPage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.course_page import CoursePage
from core.pages.googleform_page import GoogleformPage
from core.pages.login_page import LoginPage
from core.pages.studentwork_page import StudentworkPage
from core.data.text_data import TextData
from core.util.constants import Constants


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(8),
    pytest.mark.check_quiz_teacher,
    pytest.mark.quiz_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Check Quiz Teacher - " + dt_string),
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
class TestTeacherCheck:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config, login_page):

        classwork = ClassworkPage(driver, test_config)

        yield classwork

        # while not classwork.assigned_task.visible:
        #     driver.refresh()

        time.sleep(3)

        # classwork.wait_for_element_clickable(element=classwork.assigned_task)
        classwork.assigned_task.click()

        classwork.wait_for_element_clickable(
            element=classwork.attachment_link
        )
        classwork.attachment_link.click()

        driver.switch_to.window(driver.window_handles[2])

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


@allure.sub_suite("03. Check Googleform Quiz")
class TestGoogleformPage:
    @pytest.fixture(scope="class")
    def googleform(self, driver, test_config):
        googleform = GoogleformPage(driver, test_config)

        googleform.edit_form_button.click()
        googleform.wait_for_element_clickable(
            element=googleform.responses_button
        )
        googleform.responses_button.click()

        googleform.wait_for_element_clickable(
            element=googleform.individual_tab
        )
        googleform.individual_tab.click()

        yield googleform

        driver.switch_to.window(driver.window_handles[1])

    @allure.title("Check First Question")
    def test_check_first_question(self, googleform):
        with allure.step("First Question Answer"):
            try:
                assert googleform.first_answer_text.text == "28"
            except:
                allure.attach(googleform.driver.get_screenshot_as_png(),
                              name="First Question Answer not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Check Second Question")
    def test_check_second_question(self, googleform):
        with allure.step("Second Question Answer"):
            try:
                assert googleform.second_answer_text.text == "13"
            except:
                allure.attach(googleform.driver.get_screenshot_as_png(),
                              name="Second Question Answer not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("04. Student Page")
class TestStudentPage:
    @pytest.fixture(scope="class")
    def studentwork(self, driver, test_config):
        classwork = ClassworkPage(driver, test_config)

        classwork.wait_for_element_clickable(
            element=classwork.assigned_task_view_button
        )
        classwork.assigned_task_view_button.click()

        studentwork = StudentworkPage(driver, test_config)

        studentwork.wait_for_element_clickable(
            element=studentwork.add_grade_button
        )
        studentwork.add_grade_button.click()
        studentwork.input_grade_box.input_text(TextData.GRADE_50)
        studentwork.wait_for_element_clickable(
            element=studentwork.return_button
        )
        studentwork.return_button.click()
        studentwork.wait_for_element_clickable(
            element=studentwork.alertdialog_return_button
        )
        studentwork.alertdialog_return_button.click()

        yield studentwork

    @allure.title("Student Grade Points")
    def test_student_grade_points(self, studentwork):
        with allure.step("Student Grade Points are added"):
            try:
                studentwork.wait_for_element(element=studentwork.grade_points)
                assert studentwork.grade_points.text == \
                       "50 points out of possible 100"
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
                assert studentwork.graded_label.text == "Graded"
            except:
                allure.attach(studentwork.driver.get_screenshot_as_png(),
                              name="Student Status not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False
