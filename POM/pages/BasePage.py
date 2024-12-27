from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

""" This is the base page for all classes"""


class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def do_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        element.click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self):
        return self.driver.title
