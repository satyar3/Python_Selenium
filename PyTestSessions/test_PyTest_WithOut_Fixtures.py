import pytest
from selenium import webdriver

driver = None


def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.maximize_window()


def teardown_module(module):
    driver.quit()


def test_google():
    driver.get("https://google.com")
    assert driver.title.lower().__contains__('google')


def test_fb():
    driver.get("https://fb.com")
    assert driver.title.lower().__contains__('facebook')
