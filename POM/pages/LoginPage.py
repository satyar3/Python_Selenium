from POM.pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class Login(BasePage):
    EMAIL_ID = (By.NAME, "user_name")
    PASSWORD = (By.ID, "password_field")
    SUBMIT_BTN = (By.CSS_SELECTOR, "#submit")

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    """Page Actions"""

    def get_login_page_title(self):
        return self.get_title()

    def is_signup_link_exist(self):
        return self.is_enabled()

    def do_login(self, user_name, password):
        self.do_send_keys(self.EMAIL_ID, user_name)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SUBMIT_BTN)
