import pytest
from selenium import webdriver



@pytest.fixture(scope='class')
def init_driver(request):
    print(f'Set Up steps has been started.')
    driver = webdriver.Chrome()
    print(f'Set Up steps has been completed.')
    request.cls.driver = driver

    # yield keyword will replace the teardown step
    yield
    driver.quit()


@pytest.mark.usefixtures("init_driver")
class a_Test_Base:
    pass


class Test_Google(a_Test_Base):

    def test_title(self):
        self.driver.get("https://google.com")
        assert self.driver.title.lower().__contains__('google')


class Test_FB(a_Test_Base):

    def test_title(self):
        self.driver.get("https://fb.com")
        assert self.driver.title.lower().__contains__('facebook')
