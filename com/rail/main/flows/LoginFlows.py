
from Config import TEST_EMAIL, TEST_PASSWORD
from com.rail.main.pages.LoginPage import *


class LoginFlows:
    def __init__(self, driver):
        self.driver = driver

    def perform_login(self):
        self.driver.send_keys(LoginPage.email_input_field, TEST_EMAIL)
        self.driver.send_keys(LoginPage.password_input_field, TEST_PASSWORD)
        self.driver.click(LoginPage.login_submit_button)

