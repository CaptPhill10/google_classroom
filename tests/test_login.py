import allure
import pytest
from allure_commons.types import AttachmentType
from datetime import datetime
from core.pages.account_page import AccountPage
from core.pages.login_page import LoginPage
from core.util.constants import Constants

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")

pytestmark = [
    pytest.mark.order(1),
    pytest.mark.xdist_group(name="Login"),
    pytest.mark.login,
    pytest.mark.smoke,
    allure.parent_suite("All tests"),
    allure.suite("Login - " + dt_string),
]


@allure.sub_suite("01. Login View")
class TestLoginView:
    @pytest.fixture(scope="class")
    def login(self, driver, test_config):

        login = LoginPage(driver, test_config)
        login.open_main_page()

        yield login

        login.email_field.input_text(Constants.COURSE_LOGIN)
        login.login_next_button.click()

    @allure.title("Create Account Button")
    def test_create_account_button(self, login):
        with allure.step("Create Account Button is visible"):
            try:
                assert login.create_account_button.text == "Create account"
            except:
                allure.attach(login.driver.get_screenshot_as_png(),
                              name="Create Account Button not visible",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Forgot Email button")
    def test_forgot_email_button(self, login):
        with allure.step("Forgot Email Button is visible"):
            try:
                assert login.forgot_email_button.text == "Forgot email?"
            except:
                allure.attach(login.driver.get_screenshot_as_png(),
                              name="Forgot Email Button not visible",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Empty Email Field")
    def test_empty_email_field(self, login):
        with allure.step("Empty Email Field Text"):
            try:
                assert login.empty_login_field.text == "Email or phone"
            except:
                allure.attach(login.driver.get_screenshot_as_png(),
                              name="'Email or phone' text not visible",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Submit Empty Email")
    def test_empty_email_submit(self, login):
        with allure.step("Submit Empty Email"):
            login.login_next_button.click()
            login.wait_for_element(
                element=login.login_error_message,
                wait_time=30
            )
            try:
                assert login.login_error_message.text == \
                       "Enter an email or phone number"
            except:
                allure.attach(login.driver.get_screenshot_as_png(),
                              name="'Login Error Message not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Submit not Google Email")
    def test_not_google_email(self, login):
        login.email_field.input_text(Constants.INVALID_LOGIN)
        login.login_next_button.click()
        with allure.step("Submit not Google Email"):
            try:
                assert login.login_error_message.text == \
                       "Couldn’t find your Google Account"
            except:
                allure.attach(login.driver.get_screenshot_as_png(),
                              name="Login Error Message not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False


@allure.sub_suite("02. Password View")
class TestPasswordView:
    @pytest.fixture(scope="class")
    def password(self, driver, test_config):

        password = LoginPage(driver, test_config)

        yield password

    @allure.title("Email is displayed")
    def test_email_displayed(self, password):
        with allure.step("Email Link is displayed"):
            password.wait_for_element_clickable(element=password.email_link)
            try:
                assert password.email_link.text == Constants.COURSE_LOGIN
            except:
                allure.attach(password.driver.get_screenshot_as_png(),
                              name="Email Link not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Forgot Password Button")
    def test_forgot_password_button(self, password):
        with allure.step("Forgot Password Button is displayed"):
            password.wait_for_element_clickable(
                element=password.forgot_password_button
            )
            try:
                assert password.forgot_password_button.text == \
                       "Forgot password?"
            except:
                allure.attach(password.driver.get_screenshot_as_png(),
                              name="Forgot Password Button not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Empty Password Field")
    def test_empty_password_field(self, password):
        with allure.step("Empty Password Field text"):
            try:
                assert password.empty_password_field.text == \
                       "Enter your password"
            except:
                allure.attach(password.driver.get_screenshot_as_png(),
                              name="'Enter your password' text not visible",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Submit Empty Password")
    def test_empty_password_submit(self, password):
        with allure.step("Empty Password Submit"):
            password.login_next_button.click()
            try:
                assert password.password_error_message.text == \
                       "Enter a password"
            except:
                allure.attach(password.driver.get_screenshot_as_png(),
                              name="Password Error Message not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Use Incorrect Password")
    def test_incorrect_password_submit(self, password):
        with allure.step("Use Incorrect Password"):
            password.password_field.input_text(Constants.INVALID_PASSWORD)
            password.login_next_button.click()
            try:
                assert password.password_error_message.text == \
                       "Wrong password. Try again or click Forgot " \
                       "password to reset it."
            except:
                allure.attach(password.driver.get_screenshot_as_png(),
                              name="Password Error Message not displayed",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Show Password Checkbox")
    def test_show_password_checkbox(self, password):
        with allure.step("Show Password Checkbox"):
            password.password_field.input_text(Constants.INVALID_PASSWORD)
            password.wait_for_element_clickable(
                element=password.show_password_checkbox
            )
            password.show_password_checkbox.click()
            try:
                password_field_data = \
                    password.password_field.get_attribute(
                        "data-initial-value"
                    )
                assert password_field_data == Constants.INVALID_PASSWORD
            except:
                allure.attach(password.driver.get_screenshot_as_png(),
                              name="Show Password Checkbox error",
                              attachment_type=AttachmentType.PNG)
                assert False

    @allure.title("Valid Password Submit")
    def test_submit_valid_password(self, driver, password, test_config):
        with allure.step("Valid Password Submit"):
            password.password_field.input_text(Constants.COURSE_PASSWORD)
            password.login_next_button.click()
            account = AccountPage(driver, test_config)
            try:
                assert account.google_apps_button.visible
            except:
                allure.attach(password.driver.get_screenshot_as_png(),
                              name="Login failed. Account page not opened",
                              attachment_type=AttachmentType.PNG)
                assert False
