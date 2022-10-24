import allure
import pytest
from allure_commons.types import AttachmentType
from datetime import datetime

from core.pages.account_page import AccountPage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.invite_page import InvitePage
from core.pages.login_page import LoginPage
from core.util.constants import Constants


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(7),
    pytest.mark.xdist_group(name="Assignment"),
    pytest.mark.assignment_flow,
    pytest.mark.create_assignment,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Create Change Assignment - " + dt_string),
]


@pytest.fixture(scope="module")
def login_page(driver, test_config):

    login = LoginPage(driver, test_config)
    login.open_main_page()
    login.do_login(
        Constants.ASSIGNMENT_LOGIN,
        Constants.ASSIGNMENT_PASSWORD
    )

    account = AccountPage(driver, test_config)

    yield account


@allure.sub_suite("01. Classroom Page")
class TestClassPage:
    @pytest.fixture(scope="class")
    def classroom(self, driver, test_config, login_page, text_data):

        account = AccountPage(driver, test_config)

        account.open_classroom()
        classroom = ClassroomPage(driver, test_config, text_data)

        if classroom.dialog_window.visible:
            classroom.wait_for_element(classroom.dialog_continue_button)
            classroom.dialog_continue_button.click()

        yield classroom

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


@allure.sub_suite("02. Create or open Course")
class TestOpenCoursePage:
    @pytest.fixture(scope="class")
    def invite(self, driver, test_config, text_data):
        classroom = ClassroomPage(driver, test_config, text_data)

        classroom.create_course(text_data.CLASS_NAME)

        while classroom.announcement_popup.visible:
            classroom.got_it_button.click()
            if not classroom.got_it_button.visible:
                classroom.next_button.click()
            else:
                break

        if classroom.alertdialog.visible:
            classroom.close_button.click()

        invite = InvitePage(driver, test_config)
        invite.invite_people(
            teacher_login=Constants.ASSIGNMENT_TEACHER_LOGIN,
            student_login=Constants.ASSIGNMENT_STUDENT_LOGIN
        )

        yield invite

        invite.wait_for_element_clickable(
            element=invite.classwork_button,
            wait_time=30
        )
        invite.classwork_button.click()

        if not invite.classwork_button.visible:
            driver.refresh()
            invite.wait_for_element_clickable(
                element=invite.classwork_button,
                wait_time=30
            )
            invite.classwork_button.click()

    @allure.title("Invite Teacher")
    def test_invite_teacher(self, invite):
        with allure.step("Teacher invited"):
            try:
                invite.wait_for_element_clickable(
                    element=invite.teacher_name,
                    wait_time=30
                )
                assert invite.teacher_name.text == \
                       Constants.ASSIGNMENT_TEACHER_LOGIN
            except:
                allure.attach(invite.driver.get_screenshot_as_png(),
                              name="Teacher not invited",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Invite Student")
    def test_invite_student(self, invite):
        with allure.step("Student invited"):
            try:
                invite.wait_for_element_clickable(element=invite.student_name)
                assert invite.student_name.text == \
                       Constants.ASSIGNMENT_STUDENT_LOGIN
            except:
                allure.attach(invite.driver.get_screenshot_as_png(),
                              name="Student not invited",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("03. Classwork Page")
class TestClassworkPage:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config):
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

        classwork.wait_for_element_clickable(
            element=classwork.create_button,
            wait_time=30
        )
        classwork.create_button.click()

        classwork.wait_for_element_clickable(
            element=classwork.assignment_button,
            wait_time=30
        )
        classwork.assignment_button.click()

        if not classwork.assignment_name.visible:
            classwork.assignment_button.click()

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


@allure.sub_suite("04. Create Assignment")
class TestAssignmentPage:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config, text_data):
        assignment = ClassworkPage(driver, test_config)

        while assignment.announcement_popup.visible:
            assignment.got_it_button.click()
            if not assignment.got_it_button.visible:
                assignment.next_button.click()
            else:
                break

        if assignment.alertdialog.visible:
            assignment.close_button.click()

        assignment.assignment_name.input_text(text_data.ASSIGNMENT_NAME)

        assignment.attach_video_button.click()
        driver.switch_to.frame("newt-iframe")
        assignment.wait_for_element_clickable(
            element=assignment.search_video_field,
            wait_time=30
        )
        assignment.search_video_field.input_text(
            text_data.ASSIGNMENT_ATTACHMENT
        )
        assignment.search_button.click()
        assignment.add_video_button.click()
        driver.switch_to.parent_frame()

        assignment.wait_for_element_clickable(
            element=assignment.due_date_button,
            wait_time=30
        )

        assignment.due_date_button.click()
        assignment.date_picker_button.click()
        assignment.step_date()

        attribute_value = assignment.post_button.get_attribute("tabindex")
        if attribute_value == "0":
            assignment.post_button.click()
        else:
            while attribute_value != "0":
                print(attribute_value)
                attribute_value = \
                    assignment.post_button.get_attribute("tabindex")
                print(attribute_value)
                if attribute_value == "0":
                    assignment.post_button.click()

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

    @allure.title("Assignment created")
    def test_create_assignment(self, classwork, text_data):
        with allure.step("Assignment created"):
            try:
                assert classwork.other_name.text == text_data.ASSIGNMENT_NAME
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Assignment not created",
                              attachment_type=AttachmentType.PNG)
                assert False
