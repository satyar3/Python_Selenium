import pytest

from POM.pages.LoginPage import Login
from POM.tests.test_Base import BaseTest
from POM.pages import HomePage


class Test_HomePage(BaseTest):

    @pytest.mark.parametrize("user_id, password", [('student', 'Password123')])
    def test_validate_home_page_title(self, user_id, password):
        self.home_page = Login(self.driver).do_login(user_id, password)
        assert "Logged In Successfully" in self.home_page.get_home_page_title()

    @pytest.mark.parametrize("user_id, password", [('student', 'Password123')])
    def test_validate_home_page_landing(self, user_id, password):
        self.home_page = Login(self.driver).do_login(user_id, password)
        assert "Logged In Successfully" in self.home_page.get_home_page_landing()
