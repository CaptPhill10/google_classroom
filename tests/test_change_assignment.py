import time
from datetime import datetime, timedelta

import allure
import pytest
from core.pages.account_page import AccountPage
from core.pages.base_page import BasePage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.course_page import CoursePage
from core.pages.login_page import LoginPage
from core.util.constants import Constants


now = datetime.now() - timedelta(hours=4)
dt_string = now.strftime("%d/%m/%Y %H:%M") + " ET"

pytestmark = [
    pytest.mark.all,
    pytest.mark.change_assignment,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Create Topic - " + dt_string),
]


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

        account = AccountPage(driver, test_config)

        account.open_classroom()
        classroom = ClassroomPage(driver, test_config)

        yield classroom

        course = CoursePage(driver, test_config)
        # course.wait_for_element(course.classwork_button)
        course.course_button.click()

        while course.got_it_button.visible:
            course.got_it_button.click()

        course.classwork_button.click()

    @allure.title("Classroom page is opened")
    def test_is_classroom_page(self, classroom):

        if classroom.dialog_window.visible:
            classroom.wait_for_element(classroom.dialog_continue_button)
            classroom.dialog_continue_button.click()

        assert classroom.classroom_page_header.text == "Classroom"


@allure.sub_suite("02. Change Assignment")
class TestChangeTopic:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config):
        classwork = ClassworkPage(driver, test_config)
        classwork.wait_for_element_clickable(classwork.assignment_options_button)
        classwork.assignment_options_button.click()
        time.sleep(1)
        classwork.assignment_edit_button.click()

        yield classwork

    @allure.title("Change Assignment")
    def test_change_assignment_name(self, classwork):
        classwork.title_field.input_text("Trigonometric Functions Article")
        classwork.remove_attachment.click()
        classwork.attach_link_button.click()
        classwork.alertdialog_input.input_text('https://en.wikipedia.org/wiki/Trigonometric_functions')
        classwork.add_link_button.click()
        classwork.save_button.click()

        assert classwork.assignment_title.text == "Trigonometric Functions Article"
