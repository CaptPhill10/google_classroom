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
from core.pages.studentwork_page import StudentworkPage


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(4),
    pytest.mark.assignment_flow,
    pytest.mark.check_assignment_teacher,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Check Assignment Teacher - " + dt_string),
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


@allure.sub_suite("02. Check in Studentwork")
class TestTeacherCheck:
    @pytest.fixture(scope="class")
    def studentwork(self, driver, test_config):

        classwork = ClassworkPage(driver, test_config)

        if not classwork.assigned_task.visible:
            driver.refresh()

        classwork.wait_for_element_clickable(element=classwork.assigned_work)
        classwork.assigned_task.click()

        classwork.assigned_task_view_button.click()

        studentwork = StudentworkPage(driver, test_config)

        studentwork.wait_for_element_clickable(
            element=studentwork.add_grade_button
        )
        studentwork.add_grade_button.click()
        studentwork.input_grade_box.input_text(TextData.GRADE)
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
                       "100 points out of possible 100"
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
