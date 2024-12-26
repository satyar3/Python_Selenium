import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_tests")
class BaseTest:
    pass


class Test_Google(BaseTest):

    @pytest.mark.parametrize("input_search_string", ['selenium', 'python'])
    def test_title(self, input_search_string):
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME, "q").send_keys(input_search_string)
        assert self.driver.title.lower().__contains__('google')


class Test_FB(BaseTest):

    def test_title(self):
        self.driver.get("https://fb.com")
        assert self.driver.title.lower().__contains__('facebook')
