import pytest

from POM.pages.LoginPage import Login
from POM.tests.test_Base import BaseTest


class Test_Login(BaseTest):

    def test_verify_title(self):
        self.login_page = Login(self.driver)
        assert "Google" == self.login_page.get_login_page_title()

    @pytest.mark.parametrize("user_id, password", [('student', 'Password123')])
    def test_do_login(self, user_id, password):
        self.login_page = Login(self.driver)
        self.login_page.do_login(user_name=user_id, password=password)

