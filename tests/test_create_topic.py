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
    pytest.mark.order(3),
    pytest.mark.xdist_group(name="Course"),
    pytest.mark.create_topic,
    pytest.mark.smoke,
    pytest.mark.course_flow,
    allure.parent_suite("All tests"),
    allure.suite("Create Topic - " + dt_string),
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

        classroom.course_button.click()

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


@allure.sub_suite("03. Classwork Page")
class TestClassworkPage:
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
            element=classwork.create_button,
            wait_time=30
        )
        classwork.create_button.click()

        classwork.wait_for_element_clickable(
            element=classwork.topic_button,
            wait_time=30
        )
        classwork.topic_button.click()

        if not classwork.topic_name_field.visible:
            classwork.topic_button.click()

        classwork.wait_for_element_clickable(
            element=classwork.topic_name,
            wait_time=30
        )
        classwork.topic_name_field.input_text(text_data.TOPIC_NAME)
        classwork.add_button.click()

        yield classwork

    @allure.title("Created Topic Title")
    def test_create_topic(self, classwork, text_data):
        with allure.step("Check Topic Title"):
            try:
                classwork.wait_for_element_clickable(
                    element=classwork.topic_name
                )
                assert classwork.topic_name.text == text_data.TOPIC_NAME
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Topic Title is incorrect",
                              attachment_type=AttachmentType.PNG)
                assert False
