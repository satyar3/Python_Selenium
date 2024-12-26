from selenium import webdriver
import pytest


@pytest.fixture(scope='class', params=['chrome', 'edge'])
def init_tests(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    if request.param == 'edge':
        driver = webdriver.Edge()

    request.cls.driver = driver

    yield
    driver.close()
