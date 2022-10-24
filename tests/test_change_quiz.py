import time
import allure
import pytest

from allure_commons.types import AttachmentType
from datetime import datetime

from core.pages.account_page import AccountPage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.course_page import CoursePage
from core.pages.googleform_page import GoogleformPage
from core.pages.login_page import LoginPage
from core.util.constants import Constants

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.orger(14),
    pytest.mark.xdist_group(name="Quiz"),
    pytest.mark.change_quiz,
    pytest.mark.quiz_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Change Quiz - " + dt_string),
]


@pytest.fixture(scope="module")
def login_page(driver, test_config):

    login = LoginPage(driver, test_config)
    login.open_main_page()
    login.do_login(Constants.QUIZ_LOGIN, Constants.QUIZ_PASSWORD)

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

        classroom.quiz_course_button.click()

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

        if not course.classwork_button.visible:
            driver.refresh()
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


@allure.sub_suite("02. Change Quiz")
class TestChangeQuiz:
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

        classwork.assignment_settings_button.click()
        classwork.wait_for_element_clickable(
            element=classwork.edit_button,
            wait_time=30
        )

        classwork.edit_button.click()

        if not classwork.task_title.visible:
            classwork.edit_button.click()

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


@allure.sub_suite("03. Change Quiz Assignment")
class TestQuizAssignmentPage:
    @pytest.fixture(scope="class")
    def quiz(self, driver, test_config, text_data):
        quiz = ClassworkPage(driver, test_config)

        while quiz.announcement_popup.visible:
            quiz.got_it_button.click()
            if not quiz.got_it_button.visible:
                quiz.next_button.click()
            else:
                break

        if quiz.alertdialog.visible:
            quiz.close_button.click()

        quiz.quiz_name.input_text(text_data.CHANGED_ASSIGNMENT_NAME)
        quiz.remove_attachment.click()

        yield quiz

        quiz.create_quiz_button.click()
        quiz.wait_for_element_clickable(element=quiz.forms_button)
        quiz.forms_button.click()
        quiz.wait_for_element_clickable(quiz.open_quiz)
        window_after = driver.window_handles[2]
        driver.switch_to.window(window_after)

    @allure.title("Change Quiz Assignment")
    def test_change_quiz_topic(self, quiz, text_data):
        with allure.step("Changed Quiz Title is displayed in field"):
            try:
                assert quiz.quiz_name.text == \
                       text_data.CHANGED_ASSIGNMENT_NAME
            except:
                allure.attach(quiz.driver.get_screenshot_as_png(),
                              name="Changed Quiz Title not "
                                   "displayed in field",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("04. Change Questions in Googleform Quiz")
class TestGoogleformPage:
    @pytest.fixture(scope="class")
    def googleform(self, driver, test_config, text_data):
        googleform = GoogleformPage(driver, test_config)

        while googleform.announcement_popup.visible:
            googleform.got_it_button.click()
            if not googleform.got_it_button.visible:
                googleform.next_button.click()
            else:
                break

        if googleform.alertdialog.visible:
            googleform.close_button.click()

        googleform.wait_for_element_clickable(
            element=googleform.quiz_title,
            wait_time=30
        )
        googleform.quiz_title.input_text(text_data.CHANGED_QUIZ_TITLE)
        googleform.first_question_title.input_text("sin 0°")
        googleform.configure_option.click()
        googleform.select_option.click()
        time.sleep(1)
        googleform.required_radio.click()
        googleform.add_question_button.click()
        googleform.question_name.input_text("tg 45°")
        googleform.second_configure_option.click()
        googleform.second_select_option.click()
        time.sleep(1)
        googleform.second_required_radio.click()

        yield googleform

        previous_window = driver.window_handles[1]
        driver.switch_to.window(previous_window)

    @allure.title("Googleform Quiz Title")
    def test_googleform_title(self, googleform, text_data):
        with allure.step("New Quiz Title is displayed in Googleform"):
            try:
                assert googleform.quiz_title.text == \
                       text_data.CHANGED_QUIZ_TITLE
            except:
                allure.attach(googleform.driver.get_screenshot_as_png(),
                              name="New Quiz Title not displayed "
                                   "in Googleform",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Create first question")
    def test_create_first_question(self, googleform):
        with allure.step("New First question is displayed"):
            try:
                assert googleform.first_question_title.text == "sin 0°"
            except:
                allure.attach(googleform.driver.get_screenshot_as_png(),
                              name="New First Question not displayed "
                                   "in Googleform",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Create second question")
    def test_create_second_question(self, googleform, driver):
        with allure.step("New Second question is displayed"):
            try:
                assert googleform.question_name.text == "tg 45°"
            except:
                allure.attach(googleform.driver.get_screenshot_as_png(),
                              name="New Second Question not displayed "
                                   "in Googleform",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("05. Assignment Quiz Changed")
class TestQuizChanged:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config, text_data):

        classwork = ClassworkPage(driver, test_config)

        while classwork.announcement_popup.visible:
            classwork.got_it_button.click()
            if not classwork.got_it_button.visible:
                classwork.next_button.click()
            else:
                break

        if classwork.alertdialog.visible:
            classwork.close_button.click()

        classwork.wait_for_element_clickable(
            element=classwork.post_button,
            wait_time=30
        )

        attribute_value = classwork.post_button.get_attribute("tabindex")
        if attribute_value == "0":
            classwork.post_button.click()
        else:
            while attribute_value != "0":
                print(attribute_value)
                attribute_value = \
                    classwork.post_button.get_attribute("tabindex")
                print(attribute_value)
                if attribute_value == "0":
                    classwork.post_button.click()

        yield classwork

    @allure.title("Quiz Assignment Changed")
    def test_assignment_quiz_changed(self, classwork, text_data):
        with allure.step("Quiz Assignment Changed"):
            try:
                classwork.wait_for_element(
                    element=classwork.changed_assignment_name
                )
                assert classwork.changed_assignment_name.text == \
                       text_data.CHANGED_ASSIGNMENT_NAME
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Changed Quiz Assignment Title "
                                   "not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False
