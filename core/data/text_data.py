class TextData:
    def __init__(self, test_config):
        self.test_config = test_config

        self.CLASS_NAME = {
            "archive_course": None,
            "change_assignment": "Math online class - Assignment",
            "change_material": "Math online class - Material",
            "change_question": "Math online class - Question",
            "change_quiz": "Math online class - Quiz",
            "change_topic": "Math online class - Topic",
            "check_assignment": "Math online class - Assignment",
            "check_question": "Math online class - Question",
            "check_quiz": "Math online class - Quiz",
            "create_course": "Math online class",
            "create_assignment": "Math online class - Assignment",
            "create_material": "Math online class - Material",
            "create_question": "Math online class - Question",
            "create_quiz": "Math online class - Quiz",
            "create_topic": "Math online class - Topic",
            "delete_course": None,
            "login": None,
            "pass_assignment": "Math online class - Assignment",
            "pass_material": "Math online class - Material",
            "pass_question": "Math online class - Question",
            "pass_quiz": "Math online class - Quiz",
        }[self.test_config.test_scope]

        self.SECTION = ""

        self.SUBJECT = "Math"

        self.ROOM = "1"

        self.ASSIGNMENT_NAME = "Multiplication table"

        self.ASSIGNMENT_NAME_QUIZ = "Multiplication table Quiz"

        self.ASSIGNMENT_ATTACHMENT = \
            "https://www.youtube.com/watch?v=v1Ih3-mDPUk"

        self.ASSIGNMENT_ATTACHMENT_2 = \
            'https://en.wikipedia.org/wiki/Trigonometric_functions'

        self.CHANGED_ASSIGNMENT_NAME = "Trigonometric functions"

        self.CHANGED_MATERIAL_TITLE = "Trigonometric functions"

        self.CHANGED_QUIZ_TITLE = "Trigonometric quiz"

        self.CHANGED_TOPIC_NAME = "Trigonometry"

        self.MATERIAL_ATTACHMENT = 'https://www.mathsisfun.com/tables.html'

        self.MATERIAL_TITLE = "Multiplication table article"

        self.MATERIAL_VIDEO = "https://www.youtube.com/watch?v=WvoFgL4P_rw"

        self.NEW_QUESTION = "Is the trigonometric identity " \
                       "'sin^2(a) + cos^2(a) = 1' true?"

        self.QUESTION = "How would you represent the multiplication" \
                   " '4 x 5' as addition? Results should be equal"

        self.QUESTION_ANSWER = "5 + 5 + 5 + 5"

        self.QUIZ_TITLE = "Multiplication quiz"

        self.SEARCH_KEYWORD_STUDENT = "Class invitation"

        self.SEARCH_KEYWORD_TEACHER = "Invitation to co-teach"

        self.TOPIC_NAME = "Multiplication"

        self.GRADE = "100"

        self.GRADE_50 = "50"
