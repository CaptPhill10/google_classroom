import allure
import pytest
from allure_commons.types import AttachmentType
from datetime import datetime

from core.pages.account_page import AccountPage
from core.pages.invite_page import InvitePage
from core.pages.classroom_page import ClassroomPage
from core.pages.classwork_page import ClassworkPage
from core.pages.login_page import LoginPage
from core.util.constants import Constants


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(19),
    pytest.mark.xdist_group(name="Material"),
    pytest.mark.create_material,
    pytest.mark.material_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Create Material - " + dt_string),
]


@pytest.fixture(scope="module")
def login_page(driver, test_config):

    login = LoginPage(driver, test_config)
    login.open_main_page()
    login.do_login(Constants.MATERIAL_LOGIN, Constants.MATERIAL_PASSWORD)

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


@allure.sub_suite("02. Create Course")
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
            teacher_login=Constants.MATERIAL_TEACHER_LOGIN,
            student_login=Constants.MATERIAL_STUDENT_LOGIN
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
            element=classwork.material_button,
            wait_time=30
        )
        classwork.material_button.click()

        if not classwork.material_title.visible:
            classwork.material_button.click()

    @allure.title("Invite Teacher")
    def test_invite_teacher(self, invite):
        with allure.step("Teacher invited"):
            try:
                invite.wait_for_element_clickable(element=invite.teacher_name)
                assert invite.teacher_name.text == \
                       Constants.MATERIAL_TEACHER_LOGIN
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
                       Constants.MATERIAL_STUDENT_LOGIN
            except:
                allure.attach(invite.driver.get_screenshot_as_png(),
                              name="Student not invited",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("03. Create Material")
class TestMaterialPage:
    @pytest.fixture(scope="class")
    def material(self, driver, test_config, text_data):
        material = ClassworkPage(driver, test_config)

        while material.announcement_popup.visible:
            material.got_it_button.click()
            if not material.got_it_button.visible:
                material.next_button.click()
            else:
                break

        if material.alertdialog.visible:
            material.close_button.click()

        material.material_title.input_text(text_data.MATERIAL_TITLE)

        material.attach_link_button.click()
        material.wait_for_element_clickable(
            element=material.alertdialog_input,
            wait_time=30
        )
        material.alertdialog_input.input_text(text_data.MATERIAL_ATTACHMENT)
        material.add_link_button.click()

        yield material

        material.wait_for_element_clickable(
            element=material.post_button,
            wait_time=30
        )
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

    @allure.title("Material Page opened")
    def test_is_material_page(self, material):
        with allure.step("Material Page opened"):
            try:
                material.wait_for_element(
                    element=material.material_page_title
                )
                assert material.material_page_title.text == "Material"
            except:
                allure.attach(material.driver.get_screenshot_as_png(),
                              name="Material Page not opened",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Material Title")
    def test_material_title(self, material, text_data):
        with allure.step("Material Title is displayed"):
            try:
                assert material.material_title.text == \
                       text_data.MATERIAL_TITLE
            except:
                allure.attach(material.driver.get_screenshot_as_png(),
                              name="Material Title not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Add Material")
    def test_add_material(self, material, text_data):
        with allure.step("Material Attachment added"):
            try:
                material.wait_for_element_clickable(
                    element=material.material_attachment
                )
                attachment_href = \
                    material.material_attachment.get_attribute("href")
                assert attachment_href == text_data.MATERIAL_ATTACHMENT
            except:
                allure.attach(material.driver.get_screenshot_as_png(),
                              name="Material Attachment not added",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("04. Material Created")
class TestMaterialCreated:
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

    @allure.title("Material title on Classwork page")
    def test_material_on_classwork_page(self, classwork, text_data):
        with allure.step("Material is created"):
            try:
                classwork.wait_for_element_clickable(
                    element=classwork.other_name,
                    wait_time=30
                )
                assert classwork.other_name.text == \
                       text_data.MATERIAL_TITLE
            except:
                allure.attach(classwork.driver.get_screenshot_as_png(),
                              name="Material not created",
                              attachment_type=AttachmentType.PNG)
                assert False
