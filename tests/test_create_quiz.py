import allure
import pytest
import time
from allure_commons.types import AttachmentType
from datetime import datetime

from core.pages.account_page import AccountPage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.googleform_page import GoogleformPage
from core.pages.invite_page import InvitePage
from core.pages.login_page import LoginPage
from core.util.constants import Constants


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(11),
    pytest.mark.xdist_group(name="Quiz"),
    pytest.mark.create_quiz,
    pytest.mark.quiz_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Create Quiz - " + dt_string),
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
            teacher_login=Constants.QUIZ_TEACHER_LOGIN,
            student_login=Constants.QUIZ_STUDENT_LOGIN
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
                invite.wait_for_element_clickable(element=invite.teacher_name)
                assert invite.teacher_name.text == \
                       Constants.QUIZ_TEACHER_LOGIN
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
                       Constants.QUIZ_STUDENT_LOGIN
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
            element=classwork.quiz_button,
            wait_time=30
        )
        classwork.quiz_button.click()

        if not classwork.quiz_name.visible:
            classwork.quiz_button.click()

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


@allure.sub_suite("04. Create Quiz")
class TestQuizPage:
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

        quiz.quiz_name.input_text(text_data.ASSIGNMENT_NAME_QUIZ)

        quiz.wait_for_element_clickable(
            element=quiz.due_date_button,
            wait_time=30
        )
        quiz.due_date_button.click()
        quiz.date_picker_button.click()
        quiz.step_date()

        yield quiz

        quiz.wait_for_element_clickable(element=quiz.open_quiz)
        quiz.open_quiz.click()
        window_after = driver.window_handles[2]
        driver.switch_to.window(window_after)

        while quiz.announcement_popup.visible:
            quiz.got_it_button.click()
            if not quiz.got_it_button.visible:
                quiz.next_button.click()
            else:
                break

    @allure.title("Quiz Name")
    def test_quiz_name(self, quiz, text_data):
        with allure.step("Quiz Title is displayed in title field"):
            try:
                assert quiz.quiz_name.text == text_data.ASSIGNMENT_NAME_QUIZ
            except:
                allure.attach(quiz.driver.get_screenshot_as_png(),
                              name="Quiz Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("05. Create Googleform Quiz")
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

        googleform.quiz_title.input_text(text_data.QUIZ_TITLE)

        googleform.first_question_title.input_text("7 x 4")
        googleform.configure_option.click()
        googleform.select_option.click()
        time.sleep(1)
        googleform.required_radio.click()
        googleform.answer_key.click()
        time.sleep(1)
        googleform.add_answer_field.click()
        googleform.input_answer.input_text("28")
        time.sleep(1)
        googleform.mark_as_incorrect_checkbox.click()
        googleform.done_button.click()

        googleform.add_question_button.click()
        googleform.second_question_title.input_text("3 x 8")
        googleform.second_configure_option.click()
        googleform.second_select_option.click()
        time.sleep(1)
        googleform.second_required_radio.click()
        googleform.second_answer_key.click()
        time.sleep(1)
        googleform.add_answer_field.click()
        googleform.input_answer.input_text("24")
        time.sleep(1)
        googleform.mark_as_incorrect_checkbox.click()
        googleform.done_button.click()

        yield googleform

        previous_window = driver.window_handles[1]
        driver.switch_to.window(previous_window)

    @allure.title("Googleform Quiz Title")
    def test_quiz_title(self, googleform, text_data):
        with allure.step("Googleform Quiz Title is displayed"):
            try:
                assert googleform.quiz_title.text == text_data.QUIZ_TITLE
            except:
                allure.attach(googleform.driver.get_screenshot_as_png(),
                              name="Googleform Quiz Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("First question title")
    def test_first_question_title(self, googleform):
        with allure.step("First Question Title is displayed"):
            try:
                assert googleform.question_name.text == "7 x 4"
            except:
                allure.attach(googleform.driver.get_screenshot_as_png(),
                              name="First Question Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Create second question")
    def test_second_question_title(self, googleform):
        with allure.step("Second Question Title is displayed"):
            try:
                assert googleform.second_question_name.text == "3 x 8"
            except:
                allure.attach(googleform.driver.get_screenshot_as_png(),
                              name="Second Question Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("06. Quiz Assignment Created")
class TestQuizAssignmentCreated:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config):
        quiz = ClassworkPage(driver, test_config)

        while quiz.announcement_popup.visible:
            quiz.got_it_button.click()
            if not quiz.got_it_button.visible:
                quiz.next_button.click()
            else:
                break

        if quiz.alertdialog.visible:
            quiz.close_button.click()

        quiz.wait_for_element_clickable(
            element=quiz.post_button,
            wait_time=30
        )
        attribute_value = quiz.post_button.get_attribute("tabindex")
        if attribute_value == "0":
            quiz.post_button.click()
        else:
            while attribute_value != "0":
                print(attribute_value)
                attribute_value = quiz.post_button.get_attribute("tabindex")
                print(attribute_value)
                if attribute_value == "0":
                    quiz.post_button.click()

        classwork = ClassworkPage(driver, test_config)

        yield classwork

    @allure.title("Quiz Assignment Created")
    def test_create_assignment(self, classwork, text_data):
        with allure.step("Quiz Assignment Created"):
            try:
                assert classwork.other_name.text == \
                       text_data.ASSIGNMENT_NAME_QUIZ
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Quiz Assignment not Created",
                              attachment_type=AttachmentType.PNG)
                assert False
