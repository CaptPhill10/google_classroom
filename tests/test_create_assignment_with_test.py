import time
from datetime import datetime, timedelta

import allure
import pytest
from core.pages.account_page import AccountPage
from core.pages.archive_page import ArchivePage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.course_page import CoursePage
from core.pages.login_page import LoginPage
from core.pages.people_page import PeoplePage
from core.util.constants import Constants


now = datetime.now() - timedelta(hours=4)
dt_string = now.strftime("%d/%m/%Y %H:%M") + " ET"

pytestmark = [
    pytest.mark.all,
    pytest.mark.assignment_with_test,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Create Assignment With Test - " + dt_string),
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

        yield classroom

        course = CoursePage(driver, test_config)
        course.wait_for_element_clickable(course.classwork_button)
        course.classwork_button.click()

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


@allure.sub_suite("04. Assignment with test")
class TestAssignmentWithTest:
    @pytest.fixture(scope="class")
    def quiz_assignment(self, driver, test_config):
        assignment_wt = ClassworkPage(driver, test_config)

        yield assignment_wt

        assignment_wt.wait_for_element(element=assignment_wt.people_button, wait_time=10)
        assignment_wt.people_button.click()

    @allure.title("Create assignment with test")
    def test_create_assignment_with_test(self, quiz_assignment, driver):
        quiz_assignment.create_button.click()
        quiz_assignment.quiz_assignment.click()
        quiz_assignment.title_field.input_text("Multiplication table test")
        # assert quiz_assignment.description.visible
        # quiz_assignment.description.click()
        # quiz_assignment.description.input_text("Fill the gaps in the test")
        assert quiz_assignment.open_quiz.visible
        quiz_assignment.open_quiz.click()
        window_after = driver.window_handles[2]
        driver.switch_to.window(window_after)
        if quiz_assignment.guide.visible:
            quiz_assignment.no_thanks_button.click()
        if quiz_assignment.guide.visible:
            quiz_assignment.okay_button.click()
        quiz_assignment.quiz_title.input_text("Multiplication quiz")

    @allure.title("Create first question")
    def test_create_first_question(self, quiz_assignment):
        quiz_assignment.first_question_title.input_text("7 x 4")
        quiz_assignment.configure_option.click()
        quiz_assignment.select_option.click()
        time.sleep(1)
        quiz_assignment.required_radio.click()
        quiz_assignment.answer_key.click()
        time.sleep(1)
        quiz_assignment.add_answer_field.click()
        quiz_assignment.input_answer.input_text("28")
        time.sleep(1)
        quiz_assignment.mark_as_incorrect_checkbox.click()
        quiz_assignment.done_button.click()

    @allure.title("Create second question")
    def test_create_second_question(self, quiz_assignment, driver):
        quiz_assignment.add_question_button.click()
        quiz_assignment.second_question_title.input_text("3 x 8")
        quiz_assignment.second_configure_option.click()
        quiz_assignment.second_select_option.click()
        time.sleep(1)
        quiz_assignment.second_required_radio.click()
        quiz_assignment.second_answer_key.click()
        time.sleep(1)
        quiz_assignment.add_answer_field.click()
        quiz_assignment.input_answer.input_text("24")
        time.sleep(1)
        quiz_assignment.mark_as_incorrect_checkbox.click()
        quiz_assignment.done_button.click()
        previous_window = driver.window_handles[1]
        driver.switch_to.window(previous_window)
        quiz_assignment.topic_field.click()
        quiz_assignment.select_topic.click()
        quiz_assignment.due_date.click()
        quiz_assignment.due_date_field.click()
        quiz_assignment.assign_button.click()

        assert quiz_assignment.quiz_assignment_title.visible
        print(quiz_assignment.quiz_assignment_title.text)


@allure.sub_suite("05. Assign Teacher")
class TestAssignTeacher:
    @pytest.fixture(scope="class")
    def people_page(self, driver, test_config):
        people_page = PeoplePage(driver, test_config)
        people_page.invite_teacher_button.click()

        yield people_page

    @allure.title("Assign Teacher by Email")
    def test_invite_teacher_email(self, people_page):
        people_page.people_email.input_text("chrislusttrue@gmail.com")

        if people_page.people_option.text == "chrislusttrue@gmail.com":
            people_page.people_option.click()
        people_page.invite_button.click()

        assert people_page.teacher_name.visible


@allure.sub_suite("06. Assign Student")
class TestAssignStudent:
    @pytest.fixture(scope="class")
    def people_page(self, driver, test_config):
        people_page = PeoplePage(driver, test_config)
        people_page.invite_student_button.click()

        yield people_page

    @allure.title("Assign Student by Email")
    def test_invite_student_email(self, people_page):
        people_page.people_email.input_text("sherlocktrue@gmail.com")

        if people_page.people_option.text == "sherlocktrue@gmail.com":
            people_page.people_option.click()
        people_page.invite_button.click()

        assert people_page.student_name.visible


# @allure.sub_suite("05. Archive course")
# class TestArchiveCourse:
#     @pytest.fixture(scope="class")
#     def classroom(self, driver, test_config):
#         classroom = ClassroomPage(driver, test_config)
#         time.sleep(2)
#         classroom.main_menu_button.click()
#         classroom.classes_button.click()
#
#         yield classroom
#
#         classroom.main_menu_button.click()
#
#     @allure.title("Archive course")
#     def test_archive_course(self, classroom):
#         classroom.archive_course()
#
#
# @allure.sub_suite("06. Delete course")
# class TestDeleteCourse:
#     @pytest.fixture(scope="class")
#     def archive(self, driver, test_config):
#         archive = ArchivePage(driver, test_config)
#
#         yield archive
#
#     @allure.title("Delete course")
#     def test_delete_course(self, archive):
#         archive.delete_course()
