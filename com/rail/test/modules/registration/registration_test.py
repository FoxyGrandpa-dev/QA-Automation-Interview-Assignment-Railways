import time

import pytest

from Config import REGISTRATION_PAGE
from com.rail.main.pages.RegistrationPage import RegistrationPage
from com.rail.main.flows.LoginFlows import LoginFlows
from com.rail.main.flows.RegistrationFlows import RegistrationFlows
from com.rail.main.utils.AssertionsHelper import AssertionsHelper
from com.rail.main.utils.ProjectLog import ProjectLog
from com.rail.main.utils.WebdriverHelper import WebdriverHelper
import random


class TestRegistration:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = WebdriverHelper(REGISTRATION_PAGE)
        self.login_flows = LoginFlows(self.driver)
        self.registration_flows = RegistrationFlows(self.driver)
        self.assertions = AssertionsHelper(self.driver)
        self.logger = ProjectLog().get_logger()

    def teardown_method(self):
        self.driver.close_driver()

    def test_registration_sanity(self):
        self.logger.info("starting test_registration_sanity()...")
        x = random.randrange(1, 1000)
        random_email = f"anyAddress{x}@anyDomain.com"
        random_pw = f"MyNameJeff{x}!"
        self.logger.info(f"email: '{random_email}' - password: '{random_pw}'")

        self.driver.send_keys(RegistrationPage.firstname_input_field, f"testerFname")
        self.driver.send_keys(RegistrationPage.lastname_input_field, f"testerLname")
        self.driver.send_keys(RegistrationPage.email_input_field, random_email)
        self.driver.send_keys(RegistrationPage.password_input_field, random_pw)
        if self.driver.find_element(RegistrationPage.email_me_news_and_updates_checkbox).is_selected():
            self.driver.click(RegistrationPage.email_me_news_and_updates_checkbox)
        self.driver.click(RegistrationPage.submit_signup_button)    # OFTEN TRIGGERS CAPTCHA - will not be handled
        self.assertions.assert_element_is_displayed(RegistrationPage.successful_registration_message)
        time.sleep(10)

