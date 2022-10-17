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
        elif "login_page" in self.test_file:
            self.test_scope = "login_page"
        elif "create_assignment" in self.test_file:
            self.test_scope = "create_assignment"
        elif "pass_assignment_st" in self.test_file:
            self.test_scope = "pass_assignment_st"
        elif "check_assignment_teacher" in self.test_file:
            self.test_scope = "check_assignment_teacher"
        elif "change_assignment" in self.test_file:
            self.test_scope = "change_assignment"
        elif "create_material" in self.test_file:
            self.test_scope = "create_material"
        elif "pass_material_st" in self.test_file:
            self.test_scope = "pass_material_st"
        elif "change_material" in self.test_file:
            self.test_scope = "change_material"
        elif "create_question" in self.test_file:
            self.test_scope = "create_question"
        elif "pass_question_st" in self.test_file:
            self.test_scope = "pass_question_st"
        elif "check_question_teacher" in self.test_file:
            self.test_scope = "check_question_teacher"
        elif "change_question" in self.test_file:
            self.test_scope = "change_question"
        elif "create_quiz" in self.test_file:
            self.test_scope = "create_quiz"
        elif "pass_quiz_st" in self.test_file:
            self.test_scope = "pass_quiz_st"
        elif "check_quiz_teacher" in self.test_file:
            self.test_scope = "check_quiz_teacher"
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
