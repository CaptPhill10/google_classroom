# google_classroom
Google Classroom Python Framework 
-----

Framework includes tests for main functionality of Google Classroom:
- Login: Includes tests for Login page with positive and negative scenarios;
- Course flow: Course creation, Change Ribbon Settings, Creating a topic, Invite teachers, Invite students, Changing the topic, Archive Course, Delete Course;
- Assignment flow: Course creation,Creating an assignment, Invite teachers, Invite students, Go through assignments under the role of a student, Check assignments under teacher role, Changing the assignment;
- Quiz flow: Creating an assignment with a test (quiz), Invite teachers, Invite students, Go through quiz under the role of a student,  Check quiz under teacher role, Changing the quiz;
- Question flow: Creating a question, Invite teachers, Invite students, Go through question under the role of a student, Check question under teacher role, Changing the question;
- Material flow: Creating a material, Invite teachers, Invite students, Go through material under the role of a student, Changing the material.

Test reports can be generated in Allure Reports.
Parallel tests execution implemented using pytest-xdist
---



Run Instructions 
----- 
The python framework can be run directly from the command line using pytest.

Call Example 

Use 'pytest -h' to see usage. 
```
usage: pytest test [-m] -vs
```

Examples 

Execute all 'assignment_flow' tests
```
pytest -m assignment_flow -vs
```
Execute all 'assignment_flow' tests with Allure Report generation
```
pytest -m assignment_flow --alluredir=results -vs
```
Generate Allure result
```
allure serve results
```
Execute tests in parallel on two workers using pytest-xdist with Allure report generation
```
pytest --dist loadgroup -n 2 --alluredir=results -vs 
```
