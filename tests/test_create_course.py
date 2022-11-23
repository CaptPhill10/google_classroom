import allure
import pytest
from allure_commons.types import AttachmentType
from datetime import datetime
from core.pages.account_page import AccountPage
from core.pages.classroom_page import ClassroomPage
from core.pages.course_page import CoursePage
from core.pages.invite_page import InvitePage
from core.pages.login_page import LoginPage
from core.util.constants import Constants

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(2),
    pytest.mark.xdist_group(name="Course"),
    pytest.mark.create_course,
    pytest.mark.course_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Create Course - " + dt_string),
]


@pytest.fixture(scope="module")
def login_page(driver, test_config):
    login = LoginPage(driver, test_config)
    login.open_main_page()
    login.do_login(Constants.COURSE_LOGIN, Constants.COURSE_PASSWORD)

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
                assert classroom.classroom_page_header.text == "Classroom"
            except:
                allure.attach(classroom.driver.get_screenshot_as_png(),
                              name="Classroom title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("02. Create Course")
class TestCreateCoursePage:
    @pytest.fixture(scope="class")
    def course(self, driver, test_config, text_data):
        classroom = ClassroomPage(driver, test_config, text_data)
        classroom.create_course(text_data.CLASS_NAME)

        course = CoursePage(driver, test_config)

        while course.announcement_popup.visible:
            course.got_it_button.click()
            if not course.got_it_button.visible:
                course.next_button.click()
            else:
                break

        if course.alertdialog.visible:
            course.close_button.click()

        yield course

        course.stream_settings_button.click()

    @allure.title("Course created")
    def test_create_class(self, course):
        with allure.step("Check Course is created"):
            course.wait_for_element_clickable(
                element=course.stream_settings_button
            )
            try:
                assert course.stream_settings_button.visible
            except:
                allure.attach(course.driver.get_screenshot_as_png(),
                              name="Course not created",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("03. Stream Settings")
class TestSettingsPage:
    @pytest.fixture(scope="class")
    def settings(self, driver, test_config, text_data):
        settings = CoursePage(driver, test_config)

        while settings.announcement_popup.visible:
            settings.got_it_button.click()
            if not settings.got_it_button.visible:
                settings.next_button.click()
            else:
                break

        if settings.alertdialog.visible:
            settings.close_button.click()

        settings.wait_for_element_clickable(
            element=settings.stream_options,
            wait_time=30
        )
        settings.stream_options.click()

        settings.wait_for_element_clickable(
            element=settings.select_stream_option,
            wait_time=30
        )
        settings.select_stream_option.click()

        settings.save_button.click()

        yield settings

    @allure.title("Settings changed")
    def test_settings_changed(self, settings):
        with allure.step("Stream Settings changed"):
            try:
                settings.wait_for_element(
                    element=settings.saved_message,
                    wait_time=30
                )
                assert settings.saved_message.text == "Settings saved"
            except:
                allure.attach(settings.driver.get_screenshot_as_png(),
                              name="Stream Settings not changed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("03. Invite people")
class TestInvitePage:
    @pytest.fixture(scope="class")
    def invite(self, driver, test_config):
        invite = InvitePage(driver, test_config)

        invite.invite_people(
            teacher_login=Constants.TEACHER_LOGIN,
            student_login=Constants.STUDENT_LOGIN
        )

        yield invite

    @allure.title("Invite Teacher")
    def test_invite_teacher(self, invite):
        with allure.step("Teacher invited"):
            try:
                invite.wait_for_element_clickable(element=invite.teacher_name)
                assert invite.teacher_name.text == \
                       Constants.TEACHER_LOGIN
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
                       Constants.STUDENT_LOGIN
            except:
                allure.attach(invite.driver.get_screenshot_as_png(),
                              name="Student not invited",
                              attachment_type=AttachmentType.PNG)
                assert False
