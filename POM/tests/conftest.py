import pytest
from selenium import webdriver

from POM.config.test_config import TestConfig



@pytest.fixture(params=['chrome'], scope='function')
def init_driver(request):
    print("Going for set up")
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.get(TestConfig.base_url)

    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.maximize_window()

    yield
    print("Going for tear down")
    driver.quit()
