from POM.pages.BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    POST_TITLE = (By.CLASS_NAME, 'post-title')

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def get_home_page_title(self):
        return self.get_title()

    def get_home_page_landing(self):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.POST_TITLE))
        return element.text

