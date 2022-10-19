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
    pytest.mark.xdist_group(name="Topic"),
    pytest.mark.order(16),
    pytest.mark.create_topic,
    pytest.mark.smoke,
    pytest.mark.topic_flow,
    allure.parent_suite("All tests"),
    allure.suite("Create Topic - " + dt_string),
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

    @allure.title("Classroom page is opened")
    def test_is_classroom_page(self, classroom):
        with allure.step("Classroom title is displayed"):
            try:
                assert classroom.classroom_page_header.text == "Classroom"
            except:
                allure.attach(classroom.driver.get_screenshot_as_png(),
                              name="Classroom title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("02. Create Course")
class TestCreateCoursePage:
    @pytest.fixture(scope="class")
    def course(self, driver, test_config):
        classroom = ClassroomPage(driver, test_config)

        classroom.create_join_button.click()
        classroom.create_class_button.click()
        if classroom.agree_checkbox.visible:
            classroom.agree_checkbox.click()
            attribute_value = \
                classroom.continue_button.get_attribute("tabindex")
            if attribute_value == "0":
                classroom.continue_button_2.click()
            else:
                while attribute_value != "0":
                    print(attribute_value)
                    attribute_value = \
                        classroom.continue_button.get_attribute("tabindex")
                    print(attribute_value)
                    if attribute_value == "0":
                        classroom.continue_button_2.click()

        classroom.enter_class_name(TextData.CLASS_NAME)
        classroom.enter_section(TextData.SECTION)
        classroom.enter_subject(TextData.SUBJECT)
        classroom.enter_room(TextData.ROOM)
        attribute_value = classroom.create_button.get_attribute("tabindex")
        if attribute_value == "0":
            classroom.create_button.click()
        else:
            while attribute_value != "0":
                print(attribute_value)
                attribute_value = \
                    classroom.create_button.get_attribute("tabindex")
                print(attribute_value)
                if attribute_value == "0":
                    classroom.create_button.click()

        course = CoursePage(driver, test_config)

        yield course

        course.wait_for_element_clickable(element=course.classwork_button)
        course.classwork_button.click()

    @allure.title("Course created")
    def test_create_class(self, course):
        with allure.step("Check Course is created"):
            course.wait_for_element_clickable(
                element=course.stream_settings_button
            )
            try:
                assert course.stream_settings_button.visible
            except:
                allure.attach(course.driver.get_screenshot_as_png(),
                              name="Course not created",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("03. Classwork Page")
class TestClassworkPage:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config):
        classwork = ClassworkPage(driver, test_config)

        classwork.create_button.click()
        classwork.topic_button.click()
        classwork.topic_name_field.input_text(TextData.TOPIC_NAME)
        classwork.add_button.click()

        yield classwork

    @allure.title("Created Topic Title")
    def test_create_topic(self, classwork):
        with allure.step("Check Topic Title"):
            try:
                classwork.wait_for_element_clickable(
                    element=classwork.topic_name
                )
                assert classwork.topic_name.text == TextData.TOPIC_NAME
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Topic Title is incorrect",
                              attachment_type=AttachmentType.PNG)
                assert False
