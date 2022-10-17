import time
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
    pytest.mark.order(16),
    pytest.mark.change_material,
    pytest.mark.material_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Change Material - " + dt_string),
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


@allure.sub_suite("02. Change Quiz")
class TestChangeTopic:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config):
        classwork = ClassworkPage(driver, test_config)

        classwork.material_settings_button.click()
        classwork.wait_for_element_clickable(element=classwork.edit_button)

        if not classwork.edit_button.visible:
            driver.refresh()
            classwork.assignment_settings_button.click()
            classwork.wait_for_element_clickable(element=classwork.edit_button)

        classwork.edit_button.click()

        yield classwork

    @allure.title("Classwork Page is Opened")
    def test_classwork_page_opened(self, classwork):
        with allure.step("Course Title is displayed"):
            try:
                classwork.wait_for_element(element=classwork.course_title)
                assert classwork.course_title.text == TextData.CLASS_NAME
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Course Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("03. Change Material")
class TestMaterialPage:
    @pytest.fixture(scope="class")
    def material(self, driver, test_config):
        material = ClassworkPage(driver, test_config)

        material.material_title.input_text(TextData.CHANGED_MATERIAL_TITLE)
        material.remove_attachment.click()
        material.attach_video_button.click()
        driver.switch_to.frame("newt-iframe")
        material.search_video_field.input_text(TextData.MATERIAL_VIDEO)
        material.search_button.click()
        material.add_video_button.click()
        driver.switch_to.parent_frame()

        yield material

        attribute_value = material.post_button.get_attribute("tabindex")
        if attribute_value == "0":
            material.post_button.click()
        else:
            while attribute_value != "0":
                print(attribute_value)
                attribute_value = \
                    material.post_button.get_attribute("tabindex")
                print(attribute_value)
                if attribute_value == "0":
                    material.post_button.click()

    @allure.title("Material Name Text")
    def test_material_name_text(self, material):
        with allure.step("Changed Material Title in text field"):
            try:
                assert material.material_title.text == \
                       TextData.CHANGED_MATERIAL_TITLE
            except:
                allure.attach(material.driver.get_screenshot_as_png(),
                              name="Changed Material Title not displayed"
                                   " in field",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Change Material")
    def test_add_material(self, material):
        with allure.step("Changed Material attached"):
            try:
                material.wait_for_element_clickable(
                    element=material.material_attachment
                )
                attachment_href = \
                    material.material_attachment.get_attribute("href")
                assert attachment_href == TextData.MATERIAL_VIDEO
            except:
                allure.attach(material.driver.get_screenshot_as_png(),
                              name="Changed Material not attached",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("03. Material Changed")
class TestClassworkPage:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config):
        classwork = ClassworkPage(driver, test_config)

        # if not classwork.changed_other_name.text == \
        #        TextData.CHANGED_MATERIAL_TITLE:
        #     driver.refresh()

        time.sleep(3)

        yield classwork

    @allure.title("Material Changed")
    def test_changed_material_title(self, classwork):
        with allure.step("Material Changed. Changed Title is displayed"):
            try:
                assert classwork.changed_other_name.text == \
                       TextData.CHANGED_MATERIAL_TITLE
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Changed Material Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False
