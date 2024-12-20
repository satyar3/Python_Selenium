import pytest
# Run  py.test in your terminal
# It'll pick all the test files where the string 'test' is present in the file
# Method should have test in it
# For a specific test to run, use below command :
# py.test -k login -v

def test_m1():
    assert 'PYTHON' == 'PYTHON'


def test_m2(lang_name: str):
    assert lang_name.casefold() == 'PYTHON'


def test_m3():
    assert True == False, 'True will never match to false'

@pytest.mark.login
def test_login_fb():
    assert "login_fb" == "login_fb", "FB login successful"
