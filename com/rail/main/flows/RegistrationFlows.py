
from Config import TEST_EMAIL, TEST_PASSWORD
from com.rail.main.pages.LoginPage import *
from com.rail.main.pages.RegistrationPage import *


class RegistrationFlows:
    def __init__(self, driver):
        self.driver = driver

    def perform_register(self):
        self.driver.send_keys(RegistrationPage.email_input_field, )
        self.driver.send_keys(RegistrationPage.password_input_field)
        self.driver.send_keys(RegistrationPage.firstname_input_field)
        self.driver.send_keys(RegistrationPage.lastname_input_field)
        self.driver.click(RegistrationPage.submit_signup_button)

        self.driver.send_keys(LoginPage.email_input_field, TEST_EMAIL)
        self.driver.send_keys(LoginPage.password_input_field, TEST_PASSWORD)
        self.driver.click(LoginPage.login_submit_button)
