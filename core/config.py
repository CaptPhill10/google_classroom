import os


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
        elif "login" in self.test_file:
            self.test_scope = "login"
        elif "create_assignment" in self.test_file:
            self.test_scope = "create_assignment"
        elif "pass_assignment" in self.test_file:
            self.test_scope = "pass_assignment"
        elif "check_assignment" in self.test_file:
            self.test_scope = "check_assignment"
        elif "change_assignment" in self.test_file:
            self.test_scope = "change_assignment"
        elif "create_material" in self.test_file:
            self.test_scope = "create_material"
        elif "pass_material" in self.test_file:
            self.test_scope = "pass_material"
        elif "change_material" in self.test_file:
            self.test_scope = "change_material"
        elif "create_question" in self.test_file:
            self.test_scope = "create_question"
        elif "pass_question" in self.test_file:
            self.test_scope = "pass_question"
        elif "check_question" in self.test_file:
            self.test_scope = "check_question"
        elif "change_question" in self.test_file:
            self.test_scope = "change_question"
        elif "create_quiz" in self.test_file:
            self.test_scope = "create_quiz"
        elif "pass_quiz" in self.test_file:
            self.test_scope = "pass_quiz"
        elif "check_quiz" in self.test_file:
            self.test_scope = "check_quiz"
        elif "change_quiz" in self.test_file:
            self.test_scope = "change_quiz"
        elif "create_topic" in self.test_file:
            self.test_scope = "create_topic"
        elif "change_topic" in self.test_file:
            self.test_scope = "change_topic"
        elif "archive_course" in self.test_file:
            self.test_scope = "archive_course"
        elif "delete_course" in self.test_file:
            self.test_scope = "delete_course"
        else:
            self.test_scope = self.test_file
