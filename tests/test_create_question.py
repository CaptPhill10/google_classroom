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
    pytest.mark.create_question,
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

        yield classroom

        course = CoursePage(driver, test_config)
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


@allure.sub_suite("02. Course page")
class TestCoursePage:
    @pytest.fixture(scope="class")
    def course(self, driver, test_config):
        course = CoursePage(driver, test_config)
        course.classwork_button.click()

        yield course


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


@allure.sub_suite("04. Question")
class TestQuestion:
    @pytest.fixture(scope="class")
    def question(self, driver, test_config):
        question_form = ClassworkPage(driver, test_config)

        yield question_form

    @allure.title("Create question")
    def test_create_question(self, question):
        question.create_button.click()
        question.question_button.click()
        question.title_field.input_text("q")
        question.question_listbox.click()
        question.listbox_option.click()
        question.answer_option_1.input_text("a")
        question.add_answer_option.click()
        question.answer_option_2.input_text("b")
        question.topic_field.click()
        question.select_topic.click()
        question.due_date.click()
        question.due_date_field.click()
        question.ask_button.click()


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


@allure.sub_suite("05. Archive course")
class TestArchiveCourse:
    @pytest.fixture(scope="class")
    def classroom(self, driver, test_config):
        classroom = ClassroomPage(driver, test_config)
        time.sleep(2)
        classroom.main_menu_button.click()
        classroom.classes_button.click()

        yield classroom

        classroom.main_menu_button.click()

    @allure.title("Archive course")
    def test_archive_course(self, classroom):
        classroom.archive_course()


@allure.sub_suite("06. Delete course")
class TestDeleteCourse:
    @pytest.fixture(scope="class")
    def archive(self, driver, test_config):
        archive = ArchivePage(driver, test_config)

        yield archive

    @allure.title("Delete course")
    def test_delete_course(self, archive):
        archive.delete_course()
