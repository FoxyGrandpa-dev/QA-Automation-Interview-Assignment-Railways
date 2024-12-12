
from Config import TEST_EMAIL, TEST_PASSWORD
from com.rail.main.pages.LoginPage import *


class LoginFlows:
    def __init__(self, driver):
        self.driver = driver

    def perform_login(self, email=TEST_EMAIL, pw=TEST_PASSWORD):
        """
        perform login to website with default credentials or email+password supplied
        :return: None
        """
        self.driver.send_keys(LoginPage.email_input_field, email)
        self.driver.send_keys(LoginPage.password_input_field, pw)
        self.driver.click(LoginPage.login_submit_button)

