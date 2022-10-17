from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType

from core.pages.account_page import AccountPage
from core.pages.invite_page import InvitePage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.course_page import CoursePage
from core.pages.login_page import LoginPage
from core.data.text_data import TextData
from core.util.constants import Constants


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.all,
    pytest.mark.order(10),
    pytest.mark.create_question,
    pytest.mark.question_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Create Question - " + dt_string),
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


@allure.sub_suite("02. Create Course")
class TestCreateCoursePage:
    @pytest.fixture(scope="class")
    def course(self, driver, test_config):
        classroom = ClassroomPage(driver, test_config)

        classroom.create_join_button.click()
        classroom.create_class_button.click()
        if classroom.agree_checkbox.visible:
            classroom.agree_checkbox.click()
            attribute_value = \
                classroom.continue_button.get_attribute("tabindex")
            if attribute_value == "0":
                classroom.continue_button_2.click()
            else:
                while attribute_value != "0":
                    print(attribute_value)
                    attribute_value = \
                        classroom.continue_button.get_attribute("tabindex")
                    print(attribute_value)
                    if attribute_value == "0":
                        classroom.continue_button_2.click()

        classroom.enter_class_name(TextData.CLASS_NAME)
        classroom.enter_section(TextData.SECTION)
        classroom.enter_subject(TextData.SUBJECT)
        classroom.enter_room(TextData.ROOM)
        attribute_value = classroom.create_button.get_attribute("tabindex")
        if attribute_value == "0":
            classroom.create_button.click()
        else:
            while attribute_value != "0":
                print(attribute_value)
                attribute_value = \
                    classroom.create_button.get_attribute("tabindex")
                print(attribute_value)
                if attribute_value == "0":
                    classroom.create_button.click()

        course = CoursePage(driver, test_config)

        yield course

        course.wait_for_element_clickable(element=course.classwork_button)
        course.classwork_button.click()

    @allure.title("Course created")
    def test_create_class(self, course):
        with allure.step("Stream settings button. Course is created"):
            try:
                course.wait_for_element_clickable(
                    element=course.stream_settings_button
                )
                assert course.stream_settings_button.visible
            except:
                allure.attach(course.driver.get_screenshot_as_png(),
                              name="Stream settings button not visible. "
                                   "Course not created",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("03. Classwork Page")
class TestClassworkPage:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config):
        classwork = ClassworkPage(driver, test_config)

        yield classwork

        classwork.create_button.click()
        classwork.question_button.click()

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


@allure.sub_suite("04. Create Question")
class TestQuestionPage:
    @pytest.fixture(scope="class")
    def question(self, driver, test_config):
        question = ClassworkPage(driver, test_config)

        question.question_title.input_text(TextData.QUESTION)

        question.due_date_button.click()
        question.date_picker_button.click()
        question.step_date()

        yield question

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

    @allure.title("Question Title")
    def test_question_title_text(self, question):
        with allure.step("Question Title text in field"):
            try:
                assert question.question_title.text == TextData.QUESTION
            except:
                allure.attach(question.driver.get_screenshot_as_png(),
                              name="Question Title not displayed in"
                                   " title field",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("05. Question Created")
class TestQuestionCreated:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config):
        classwork = ClassworkPage(driver, test_config)

        yield classwork

        while not classwork.people_button.visible:
            driver.refresh()
        while classwork.got_it_button.visible:
            classwork.got_it_button.click()
        classwork.people_button.click()

    @allure.title("Check Question is created")
    def test_question_created(self, classwork):
        with allure.step("Question is created"):
            try:
                assert classwork.other_name.text == TextData.QUESTION
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Question Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("06. Invite")
class TestInvitePage:
    @pytest.fixture(scope="class")
    def invite(self, driver, test_config):
        invite = InvitePage(driver, test_config)

        invite.invite_student_button.click()
        invite.dialog_student_email.input_text(Constants.STUDENT_LOGIN)
        invite.dialog_select_first_person.click()
        attribute_value = \
            invite.dialog_invite_button.get_attribute("tabindex")
        if attribute_value == "0":
            invite.dialog_invite_button.click()
        else:
            while attribute_value != "0":
                print(attribute_value)
                attribute_value = \
                    invite.dialog_invite_button.get_attribute("tabindex")
                print(attribute_value)
                if attribute_value == "0":
                    invite.dialog_invite_button.click()

        yield invite

    @allure.title("Invite Student")
    def test_invite_student(self, invite):
        with allure.step("Student invited"):
            try:
                invite.wait_for_element_clickable(element=invite.student_name)
                assert invite.student_name.text == Constants.STUDENT_LOGIN
            except:
                allure.attach(invite.driver.get_screenshot_as_png(),
                              name="Student not invited",
                              attachment_type=AttachmentType.PNG)
                assert False
