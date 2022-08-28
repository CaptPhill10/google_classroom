import os
import random


class TestConfig(object):
    def __init__(self):

        self.full_name = os.getenv("PYTEST_CURRENT_TEST").split(" ")[0]
        self.test_file = self.full_name.split("::")[0].split("/")[-1].split(".py")[0]
        self.test_name = self.full_name.split("::")[1]
        self.test_scope = ""
        self.set_test_scope()

    def set_test_scope(self):
        if "create_course" in self.test_file:
            self.test_scope = "create_course"
        elif "test_login_page" in self.test_file:
            self.test_scope = "test_login_page"
