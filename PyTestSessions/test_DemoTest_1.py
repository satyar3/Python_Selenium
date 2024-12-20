import pytest


# Run  py.test in your terminal

# It'll pick all the test files where the string 'test' is present in the file
# Method should have test in it

# For a specific test to run, use below command :
# py.test -k login -v

# Execute test cases only with marker as login
# py.test -m login

# Execute test cases only from a specific file
# py.test -s test_DemoTest_1.py -m login

# Run Tests in Parallel
# py.test -m login -n 2 # Here n = 2 is the number of workers

# Generate html file
# pytest -s test_PyTest_Fixtures.py -v --html=google_fb_test_report.html

# -s -> To see the print statement


def test_m1():
    assert 'PYTHON' == 'PYTHON'


def test_m2(lang_name: str):
    assert lang_name.casefold() == 'PYTHON'


def test_m3():
    assert True == False, 'True will never match to false'


@pytest.mark.login
def test_login_gm():
    assert "login_gm" == "login_gm", "Gmail login successful"
