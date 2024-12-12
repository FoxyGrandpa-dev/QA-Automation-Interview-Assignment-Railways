
from Config import TEST_EMAIL, TEST_PASSWORD
from com.rail.main.pages.LoginPage import *
from com.rail.main.pages.RegistrationPage import *
import random


class RegistrationFlows:
    def __init__(self, driver):
        self.driver = driver

    def perform_register(self):
        """
        perform website registration with slightly randomized credentials
        :return:
        """
        x = random.randrange(1, 1000)
        random_email = f"anyAddress{x}@anyDomain.com"
        random_pw = f"MyNameJeff{x}!"
        print(f"\nemail: '{random_email}' - password: '{random_pw}'")

        self.driver.send_keys(RegistrationPage.firstname_input_field, f"testerFname")
        self.driver.send_keys(RegistrationPage.lastname_input_field, f"testerLname")
        self.driver.send_keys(RegistrationPage.email_input_field, random_email)
        self.driver.send_keys(RegistrationPage.password_input_field, random_pw)
        if self.driver.find_element(RegistrationPage.email_me_news_and_updates_checkbox).is_selected():
            self.driver.click(RegistrationPage.email_me_news_and_updates_checkbox)
        self.driver.click(RegistrationPage.submit_signup_button)  # OFTEN TRIGGERS CAPTCHA - will not be handled

