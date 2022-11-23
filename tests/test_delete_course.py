import allure
import pytest
from allure_commons.types import AttachmentType
from datetime import datetime
from core.pages.account_page import AccountPage
from core.pages.archive_page import ArchivePage
from core.pages.classroom_page import ClassroomPage
from core.pages.login_page import LoginPage
from core.util.constants import Constants

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(6),
    pytest.mark.xdist_group(name="Course"),
    pytest.mark.course_flow,
    pytest.mark.delete_course,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Delete Course - " + dt_string),
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

        classroom.main_menu_button.click()
        classroom.archive_page_button.click()

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


@allure.sub_suite("02. Delete course")
class TestDeleteCourse:
    @pytest.fixture(scope="class")
    def archive(self, driver, test_config):
        archive = ArchivePage(driver, test_config)

        archive.delete_course()

        yield archive

    @allure.title("Delete course")
    def test_course_deleted(self, archive):
        with allure.step("Course is deleted"):
            try:
                assert not archive.course_details_button.visible
            except:
                allure.attach(archive.driver.get_screenshot_as_png(),
                              name="Course not deleted",
                              attachment_type=AttachmentType.PNG)
                assert False
