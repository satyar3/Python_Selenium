import pytest
from selenium import webdriver


@pytest.mark.usefixtures("init_tests")
class BaseTest:
    pass


class Test_Google(BaseTest):

    def test_title(self):
        self.driver.get("https://google.com")
        assert self.driver.title.lower().__contains__('google')


class Test_FB(BaseTest):

    def test_title(self):
        self.driver.get("https://fb.com")
        assert self.driver.title.lower().__contains__('facebook')
