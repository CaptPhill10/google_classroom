import allure
import pytest
from allure_commons.types import AttachmentType
from datetime import datetime
from core.pages.account_page import AccountPage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.course_page import CoursePage
from core.pages.login_page import LoginPage
from core.util.constants import Constants

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(10),
    pytest.mark.xdist_group(name="Assignment"),
    pytest.mark.assignment_flow,
    pytest.mark.change_assignment,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Change Assignment - " + dt_string),
]


@pytest.fixture(scope="module")
def login_page(driver, test_config):

    login = LoginPage(driver, test_config)
    login.open_main_page()
    login.do_login(Constants.ASSIGNMENT_LOGIN, Constants.ASSIGNMENT_PASSWORD)

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

        classroom.assignment_course_button.click()

        course = CoursePage(driver, test_config)

        while course.announcement_popup.visible:
            course.got_it_button.click()
            if not course.got_it_button.visible:
                course.next_button.click()
            else:
                break

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
                    element=classroom.classroom_page_header,
                    wait_time=30
                )
                assert classroom.classroom_page_header.text == "Classroom"
            except:
                allure.attach(classroom.driver.get_screenshot_as_png(),
                              name="Classroom title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("02. Change Assignment")
class TestChangeTopic:
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
            element=classwork.assignment_settings_button
        )
        classwork.assignment_settings_button.click()
        classwork.wait_for_element_clickable(
            element=classwork.edit_button,
            wait_time=30
        )

        if not classwork.edit_button.visible:
            driver.refresh()
            classwork.assignment_settings_button.click()
            classwork.wait_for_element_clickable(
                element=classwork.edit_button
            )

        classwork.edit_button.click()

        if not classwork.task_title.visible:
            classwork.edit_button.click()

    @allure.title("Classwork Page is Opened")
    def test_classwork_page_opened(self, classwork, text_data):
        with allure.step("Course Title is displayed"):
            try:
                classwork.wait_for_element_clickable(
                    element=classwork.course_title,
                    wait_time=30
                )
                assert classwork.course_title.text == text_data.CLASS_NAME
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Course Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("03. Change Assignment")
class TestAssignmentPage:
    @pytest.fixture(scope="class")
    def assignment(self, driver, test_config, text_data):
        assignment = ClassworkPage(driver, test_config)

        while assignment.announcement_popup.visible:
            assignment.got_it_button.click()
            if not assignment.got_it_button.visible:
                assignment.next_button.click()
            else:
                break

        if assignment.alertdialog.visible:
            assignment.close_button.click()

        assignment.assignment_name.input_text(
            text_data.CHANGED_ASSIGNMENT_NAME
        )
        assignment.remove_attachment.click()
        assignment.attach_link_button.click()
        assignment.alertdialog_input.input_text(
            text_data.ASSIGNMENT_ATTACHMENT_2
        )
        assignment.add_link_button.click()
        attribute_value = assignment.save_button.get_attribute("tabindex")
        if attribute_value == "0":
            assignment.save_button.click()
        else:
            while attribute_value != "0":
                print(attribute_value)
                attribute_value = \
                    assignment.save_button.get_attribute("tabindex")
                print(attribute_value)
                if attribute_value == "0":
                    assignment.save_button.click()

        assignment.wait_for_element_clickable(
            element=assignment.changed_other_name,
            wait_time=30
        )
        if not assignment.changed_assignment_name == \
               text_data.CHANGED_ASSIGNMENT_NAME:
            driver.refresh()
            assignment.wait_for_element_clickable(
                element=assignment.changed_assignment_name,
                wait_time=30
            )

        yield assignment

    @allure.title("Change Assignment")
    def test_change_assignment_topic(self, assignment, text_data):
        with allure.step("Assignment Title changed"):
            try:
                assert assignment.changed_assignment_name.text == \
                       text_data.CHANGED_ASSIGNMENT_NAME
            except:
                allure.attach(assignment.driver.get_screenshot_as_png(),
                              name="Changed Assignment Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False
