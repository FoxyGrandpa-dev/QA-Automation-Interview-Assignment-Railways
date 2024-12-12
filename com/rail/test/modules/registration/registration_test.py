import pytest

from Config import REGISTRATION_PAGE
from com.rail.main.pages.RegistrationPage import RegistrationPage
from com.rail.main.flows.LoginFlows import LoginFlows
from com.rail.main.flows.RegistrationFlows import RegistrationFlows
from com.rail.main.utils.AssertionsHelper import AssertionsHelper
from com.rail.main.utils.WebdriverHelper import WebdriverHelper



class TestRegistration:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = WebdriverHelper(REGISTRATION_PAGE)
        self.registration_flows = RegistrationFlows(self.driver)
        self.assertions = AssertionsHelper(self.driver)

    def teardown_method(self):
        self.driver.close_driver()

    def test_registration_sanity(self):
        self.registration_flows.perform_register()
        self.assertions.assert_element_is_displayed(RegistrationPage.successful_registration_message)