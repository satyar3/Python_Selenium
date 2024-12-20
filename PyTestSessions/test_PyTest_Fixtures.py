import pytest
from selenium import webdriver

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print(f'Set Up steps has been started.')
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.maximize_window()
    print(f'Set Up steps has been completed.')

    # yield keyword will replace the teardown step
    yield
    driver.quit()


def test_google(init_driver):
    driver.get("https://google.com")
    assert driver.title.lower().__contains__('google')


# One more way to define fixture
@pytest.mark.usefixtures('init_driver')
def test_fb():
    driver.get("https://fb.com")
    assert driver.title.lower().__contains__('facebook1')
