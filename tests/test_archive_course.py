import allure
import pytest
from allure_commons.types import AttachmentType
from datetime import datetime

from core.pages.account_page import AccountPage
from core.pages.classroom_page import ClassroomPage
from core.pages.login_page import LoginPage
from core.util.constants import Constants


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(5),
    pytest.mark.xdist_group(name="Course"),
    pytest.mark.archive_course,
    pytest.mark.course_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Archive Course - " + dt_string),
]


@pytest.fixture(scope="module")
def login_page(driver, test_config):

    login = LoginPage(driver, test_config)
    login.open_main_page()
    login.do_login(Constants.COURSE_LOGIN, Constants.COURSE_PASSWORD)

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


@allure.sub_suite("02. Archive course")
class TestArchiveCourse:
    @pytest.fixture(scope="class")
    def classroom(self, driver, test_config, login_page, text_data):
        classroom = ClassroomPage(driver, test_config, text_data)

        yield classroom

    @allure.title("Archive course")
    def test_archive_course(self, classroom):
        classroom.archive_course()
        with allure.step("Check Course archived"):
            try:
                assert not classroom.course_button.visible
            except:
                allure.attach(classroom.driver.get_screenshot_as_png(),
                              name="Course not archived",
                              attachment_type=AttachmentType.PNG)
                assert False
