import time

import allure
import json
import pytest
from datetime import date
from core.pages.account_page import AccountPage
from core.pages.archive_page import ArchivePage
from core.pages.base_page import BasePage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.course_page import CoursePage
from core.pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from core.util.constants import Constants


@pytest.fixture(scope="module")
def login_page(driver, test_config):

    login = LoginPage(driver, test_config)
    base = BasePage(driver, test_config)
    base.open_main_page()
    login.do_login(Constants.VALID_LOGIN, Constants.VALID_PASSWORD)

    account = AccountPage(driver, test_config)

    yield account


@allure.sub_suite("01. Classroom Page")
class TestClassPage:
    @pytest.fixture(scope="class")
    def classroom(self, driver, test_config, login_page):
        # login = LoginPage(driver, test_config)
        # base = BasePage(driver, test_config)
        # base.open_main_page()
        # login.do_login(Constants.VALID_LOGIN, Constants.VALID_PASSWORD)

        account = AccountPage(driver, test_config)

        account.open_classroom()
        classroom = ClassroomPage(driver, test_config)

        yield classroom

    @allure.title("Classroom page is opened")
    def test_is_classroom_page(self, classroom):

        if classroom.dialog_window.visible:
            classroom.wait_for_element(classroom.dialog_continue_button)
            classroom.dialog_continue_button.click()

        assert classroom.classroom_page_header.text == "Classroom"

    @allure.title("Create course")
    def test_create_course(self, classroom):

        classroom.create_course_button.click()
        if classroom.agree_checkbox.visible:
            classroom.agree_checkbox.click()
            attribute_value = classroom.continue_button.get_attribute("tabindex")
            if attribute_value == "0":
                classroom.continue_button_2.click()
            else:
                while attribute_value != "0":
                    print(attribute_value)
                    attribute_value = classroom.continue_button.get_attribute("tabindex")
                    print(attribute_value)
                    if attribute_value == "0":
                        classroom.continue_button_2.click()

        classroom.enter_class_name(Constants.CLASS_NAME)
        # classroom.enter_section(Constants.SECTION)
        classroom.enter_subject(Constants.SUBJECT)
        classroom.enter_room(Constants.ROOM)
        classroom.create_button.click()


@allure.sub_suite("02. Course page")
class TestCoursePage:
    @pytest.fixture(scope="class")
    def course(self, driver, test_config):
        course = CoursePage(driver, test_config)

        yield course

        course.classwork_button.click()

    @allure.title("Change stream settings")
    def test_stream_settings(self, course):
        # course.got_it_button.click()
        course.wait_for_element(element=course.stream_settings_button, wait_time=10)
        assert course.stream_settings_button.visible


@allure.sub_suite("03. Classwork")
class TestClassworkPage:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config):
        classwork = ClassworkPage(driver, test_config)

        yield classwork

    @allure.title("Create topic")
    def test_create_topic(self, classwork):
        classwork.create_button.click()
        classwork.topic_button.click()
        classwork.topic_name_field.input_text(Constants.TOPIC_NAME)
        classwork.add_button.click()
        assert classwork.topic_name.text == Constants.TOPIC_NAME


@allure.sub_suite("04. Assignment")
class TestAssignment:
    @pytest.fixture(scope="class")
    def assignment(self, driver, test_config):
        assignment = ClassworkPage(driver, test_config)

        yield assignment

    @allure.title("Create assignment")
    def test_create_assignment(self, assignment, driver):
        assignment.create_button.click()
        assignment.assignment_button.click()
        # if assignment.close_button.visible:
        #     assignment.close_button.click()
        # else:
        #     pass
        assignment.assignment_title_field.input_text("Multiplication table video")
        # if assignment.got_it_button.visible:
        #     assignment.got_it_button.click()
        # else:
        #     pass
        # assignment.wait_for_element(element=assignment.assignment_instructions, wait_time=10)
        # assignment.assignment_instructions.input_text("1. Watch video"
        #                                               "2. Find tricks to remember"
        #                                               "multiplication table")

        assignment.attach_video_button.click()
        driver.switch_to.frame("newt-iframe")
        assert assignment.search_video_field.visible
        assignment.search_video_field.input_text("https://www.youtube.com/watch?v=v1Ih3-mDPUk")
        # driver.switch_to.parent_frame()
        # assignment.got_it_button.click()
        # driver.switch_to.frame("inproduct-guide-modal")
        assignment.search_button.click()
        assignment.add_video_button.click()
        driver.switch_to.parent_frame()
        assignment.topic_field.click()
        assignment.select_topic.click()
        assignment.due_date.click()
        assignment.due_date_field.click()
        assignment.assign_button.click()


@allure.sub_suite("05. Assignment with test")
class TestAssignmentWithTest:
    @pytest.fixture(scope="class")
    def quiz_assignment(self, driver, test_config):
        assignment_wt = ClassworkPage(driver, test_config)
        assignment_wt.wait_for_element(element=assignment_wt.create_button, wait_time=15)

        yield assignment_wt

    @allure.title("Create assignment with test")
    def test_create_assignment_with_test(self, quiz_assignment):
        quiz_assignment.create_button.click()
        quiz_assignment.quiz_assignment.click()
        breakpoint()


@pytest.mark.skip
@allure.sub_suite("Archive course")
class TestArchiveCourse:
    @pytest.fixture(scope="class")
    def classroom(self, driver, test_config):
        classroom = ClassroomPage(driver, test_config)

        yield classroom

        classroom.classroom_menu.click()

    @allure.title("Archive course")
    def test_archive_course(self, classroom):
        classroom.archive_course()


@pytest.mark.skip
@allure.sub_suite("Delete course")
class TestDeleteCourse:
    @pytest.fixture(scope="class")
    def archive(self, driver, test_config):
        archive = ArchivePage(driver, test_config)

        yield archive

    @allure.title("Delete course")
    def test_delete_course(self, archive):
        archive.delete_course()


        # assert classroom.course_name.text is None

