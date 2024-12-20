import pytest


# Grouping test cases
@pytest.mark.login_1
def test_login_1():
    assert "login" == "login"

def test_not_login():
    assert "not_login" == "not_login"

@pytest.mark.login_1
def test_login_2():
    assert "loggedin" == "loggedin"
