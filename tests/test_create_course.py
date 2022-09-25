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
        course.classwork_button.click()

        yield course

    @allure.title("Change stream settings")
    def test_stream_settings(self, course):
        # course.got_it_button.click()
        course.wait_for_element(element=course.stream_settings_button, wait_time=10)
        assert course.stream_settings_button.visible


# @allure.sub_suite("03. Classwork")
# class TestClassworkPage:
#     @pytest.fixture(scope="class")
#     def classwork(self, driver, test_config):
#         classwork = ClassworkPage(driver, test_config)
#
#         yield classwork
#
#     @allure.title("Create topic")
#     def test_create_topic(self, classwork):
#         classwork.create_button.click()
#         classwork.topic_button.click()
#         classwork.topic_name_field.input_text(Constants.TOPIC_NAME)
#         classwork.add_button.click()
#         assert classwork.topic_name.text == Constants.TOPIC_NAME
#
#
# @allure.sub_suite("04. Assignment")
# class TestAssignment:
#     @pytest.fixture(scope="class")
#     def assignment(self, driver, test_config):
#         assignment = ClassworkPage(driver, test_config)
#
#         yield assignment
#
#         # assignment.wait_for_element(element=assignment.create_button, wait_time=10)
#         time.sleep(10)
#
#     @allure.title("Create assignment")
#     def test_create_assignment(self, assignment, driver):
#         assignment.create_button.click()
#         assignment.assignment_button.click()
#         # if assignment.close_button.visible:
#         #     assignment.close_button.click()
#         # else:
#         #     pass
#         assignment.title_field.input_text("Multiplication table video")
#         # if assignment.got_it_button.visible:
#         #     assignment.got_it_button.click()
#         # else:
#         #     pass
#         # assignment.wait_for_element(element=assignment.assignment_instructions, wait_time=10)
#         # assignment.assignment_instructions.input_text("1. Watch video"
#         #                                               "2. Find tricks to remember"
#         #                                               "multiplication table")
#
#         assignment.attach_video_button.click()
#         driver.switch_to.frame("newt-iframe")
#         assert assignment.search_video_field.visible
#         assignment.search_video_field.input_text("https://www.youtube.com/watch?v=v1Ih3-mDPUk")
#         # driver.switch_to.parent_frame()
#         # assignment.got_it_button.click()
#         # driver.switch_to.frame("inproduct-guide-modal")
#         assignment.search_button.click()
#         assignment.add_video_button.click()
#         driver.switch_to.parent_frame()
#         assignment.topic_field.click()
#         assignment.select_topic.click()
#         assignment.due_date.click()
#         assignment.due_date_field.click()
#         assignment.assign_button.click()
#
#
# @allure.sub_suite("05. Assignment with test")
# class TestAssignmentWithTest:
#     @pytest.fixture(scope="class")
#     def quiz_assignment(self, driver, test_config):
#         assignment_wt = ClassworkPage(driver, test_config)
#
#         yield assignment_wt
#
#     @allure.title("Create assignment with test")
#     def test_create_assignment_with_test(self, quiz_assignment, driver):
#         quiz_assignment.create_button.click()
#         quiz_assignment.quiz_assignment.click()
#         quiz_assignment.title_field.input_text("Multiplication table test")
#         # assert quiz_assignment.description.visible
#         # quiz_assignment.description.click()
#         # quiz_assignment.description.input_text("Fill the gaps in the test")
#         assert quiz_assignment.open_quiz.visible
#         quiz_assignment.open_quiz.click()
#         window_after = driver.window_handles[2]
#         driver.switch_to.window(window_after)
#         if quiz_assignment.guide.visible:
#             quiz_assignment.no_thanks_button.click()
#         if quiz_assignment.guide.visible:
#             quiz_assignment.okay_button.click()
#         quiz_assignment.quiz_title.input_text("Multiplication quiz")
#
#     @allure.title("Create first question")
#     def test_create_first_question(self, quiz_assignment):
#         quiz_assignment.first_question_title.input_text("7 x 4")
#         quiz_assignment.configure_option.click()
#         quiz_assignment.select_option.click()
#         time.sleep(1)
#         quiz_assignment.required_radio.click()
#         quiz_assignment.answer_key.click()
#         time.sleep(1)
#         quiz_assignment.add_answer_field.click()
#         quiz_assignment.input_answer.input_text("28")
#         time.sleep(1)
#         quiz_assignment.mark_as_incorrect_checkbox.click()
#         quiz_assignment.done_button.click()
#
#     @allure.title("Create second question")
#     def test_create_second_question(self, quiz_assignment, driver):
#         quiz_assignment.add_question_button.click()
#         quiz_assignment.second_question_title.input_text("3 x 8")
#         quiz_assignment.second_configure_option.click()
#         quiz_assignment.second_select_option.click()
#         time.sleep(1)
#         quiz_assignment.second_required_radio.click()
#         quiz_assignment.second_answer_key.click()
#         time.sleep(1)
#         quiz_assignment.add_answer_field.click()
#         quiz_assignment.input_answer.input_text("24")
#         time.sleep(1)
#         quiz_assignment.mark_as_incorrect_checkbox.click()
#         quiz_assignment.done_button.click()
#         previous_window = driver.window_handles[1]
#         driver.switch_to.window(previous_window)
#         quiz_assignment.topic_field.click()
#         quiz_assignment.select_topic.click()
#         quiz_assignment.due_date.click()
#         quiz_assignment.due_date_field.click()
#         quiz_assignment.assign_button.click()
#
#         assert quiz_assignment.quiz_assignment_title.visible

#
# @allure.sub_suite("06. Question")
# class TestQuestion:
#     @pytest.fixture(scope="class")
#     def question(self, driver, test_config):
#         question_form = ClassworkPage(driver, test_config)
#
#         yield question_form
#
#     @allure.title("Create question")
#     def test_create_question(self, question):
#         question.create_button.click()
#         question.question_button.click()
        # question.title_field.input_text("q")
        # question.question_listbox.click()
        # question.listbox_option.click()
        # question.answer_option_1.input_text("a")
        # question.add_answer_option.click()
        # question.answer_option_2.input_text("b")
        # question.topic_field.click()
        # question.select_topic.click()
        # question.due_date.click()
        # question.due_date_field.click()
        # question.ask_button.click()
        # breakpoint()


@allure.sub_suite("07. Material")
class TestMaterial:
    @pytest.fixture(scope="class")
    def material(self, driver, test_config):
        material_form = ClassworkPage(driver, test_config)

        yield material_form

    @allure.title("Create material")
    def test_create_material(self, material):
        material.create_button.click()
        material.material_button.click()
        material.title_field.input_text("Multiplication table")
        # material.description.click()
        # material.description_text_input.input_text("Read the article about Multiplication table")
        material.material_topic_field.click()
        material.select_topic.click()
        material.post_button.click()

        assert material.material_name.visible
        breakpoint()


@pytest.mark.skip
@allure.sub_suite("Archive course")
class TestArchiveCourse:
    @pytest.fixture(scope="class")
    def classroom(self, driver, test_config):
        classroom = ClassroomPage(driver, test_config)
        breakpoint()

        yield classroom

        classroom.main_menu_button.click()

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

