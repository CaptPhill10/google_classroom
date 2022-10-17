from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType

from core.pages.account_page import AccountPage
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
    pytest.mark.order(17),
    pytest.mark.change_topic,
    pytest.mark.topic_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Change Topic - " + dt_string),
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

        classroom.course_button.click()

        course = CoursePage(driver, test_config)

        while course.got_it_button.visible:
            course.got_it_button.click()

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


@allure.sub_suite("02. Change Topic")
class TestChangeTopic:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config):
        classwork = ClassworkPage(driver, test_config)

        classwork.topic_settings_button.click()
        classwork.wait_for_element_clickable(element=classwork.rename_button)
        classwork.rename_button.click()
        classwork.alertdialog_input.input_text(TextData.CHANGED_TOPIC_NAME)
        classwork.alertdialog_rename_button.click()

        if not classwork.topic_name.text == \
               TextData.CHANGED_TOPIC_NAME:
            driver.refresh()

        yield classwork

    @allure.title("Changed Topic Title")
    def test_change_topic_name(self, classwork):
        with allure.step("Check Changed Topic Title"):
            try:
                classwork.wait_for_element_clickable(
                    element=classwork.topic_name
                )
                assert classwork.topic_name.text == \
                       TextData.CHANGED_TOPIC_NAME
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Changed Topic Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False
