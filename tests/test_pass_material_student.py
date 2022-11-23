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
from core.pages.gmail_page import GmailPage

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(20),
    pytest.mark.xdist_group(name="Material"),
    pytest.mark.pass_material,
    pytest.mark.material_flow,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Pass Material Student - " + dt_string),
]


@pytest.fixture(scope="module")
def login_page(driver, test_config):

    login = LoginPage(driver, test_config)
    login.open_main_page()
    login.do_login(
        Constants.MATERIAL_STUDENT_LOGIN,
        Constants.MATERIAL_STUDENT_PASSWORD
    )

    account = AccountPage(driver, test_config)

    yield account


@allure.sub_suite("01. Student Gmail")
class TestStudentGmail:
    @pytest.fixture(scope="class")
    def invitation(self, driver, test_config, login_page, text_data):

        account = AccountPage(driver, test_config)

        account.open_gmail()

        gmail = GmailPage(driver, test_config)

        gmail.search_box.input_text(text_data.SEARCH_KEYWORD_STUDENT)
        gmail.class_invitation_mail.click()
        gmail.wait_for_element(element=gmail.search_term)
        if gmail.show_content_button.visible:
            gmail.show_content()
        gmail.join_class()
        driver.switch_to.window(driver.window_handles[2])

        invitation = ClassroomPage(driver, test_config, text_data)

        yield invitation

        invitation.wait_for_element_clickable(
            element=invitation.join_button,
            wait_time=30
        )
        invitation.join_button.click()

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

    @allure.title("Check Student Gmail")
    def test_student_classroom_join(self, invitation):
        with allure.step("Invitation page is opened"):
            try:
                invitation.wait_for_element(element=invitation.dialog_header)
                assert invitation.dialog_header.text == "Join class?"
            except:
                allure.attach(invitation.driver.get_screenshot_as_png(),
                              name="Invitation page not opened",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("02. Check in Classwork")
class TestStudentCheck:
    @pytest.fixture(scope="class")
    def classwork(self, driver, test_config, login_page):

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

        if not classwork.assigned_task.visible:
            driver.refresh()

        classwork.wait_for_element_clickable(element=classwork.assigned_task)
        classwork.assigned_task.click()

        if not classwork.assigned_task_view_button.visible:
            driver.refresh()
            classwork.wait_for_element_clickable(
                element=classwork.assigned_task,
                wait_time=30
            )
            classwork.assigned_task.click()
        classwork.assigned_task_view_button.click()

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


@allure.sub_suite("03. Classwork. Open Material page")
class TestClassworkPage:
    @pytest.fixture(scope="class")
    def material(self, driver, test_config):
        material = ClassworkPage(driver, test_config)

        while material.announcement_popup.visible:
            material.got_it_button.click()
            if not material.got_it_button.visible:
                material.next_button.click()
            else:
                break

        if material.alertdialog.visible:
            material.close_button.click()

        material.material_attachment_link.click()
        driver.switch_to.window(driver.window_handles[3])

        yield material

    @allure.title("Student Review Material")
    def test_student_review_material(self, driver, material, text_data):
        with allure.step("Review Material by Student"):
            try:
                assert driver.current_url == text_data.MATERIAL_ATTACHMENT
            except:
                allure.attach(material.driver.get_screenshot_as_png(),
                              name="Material not reviewed",
                              attachment_type=AttachmentType.PNG)
                assert False
