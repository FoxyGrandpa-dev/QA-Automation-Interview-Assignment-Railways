import pytest
from com.rail.main.pages.UserProfilePage import *
from Config import LOGIN_PAGE
from com.rail.main.utils.AssertionsHelper import AssertionsHelper
from com.rail.main.flows.LoginFlows import LoginFlows
from com.rail.main.utils.WebdriverHelper import WebdriverHelper

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = WebdriverHelper(LOGIN_PAGE)
        self.login_flows = LoginFlows(self.driver)
        self.assertions = AssertionsHelper(self.driver)

    def teardown_method(self):
        self.driver.close_driver()

    def test_login_sanity(self):
        self.login_flows.perform_login()
        self.assertions.assert_element_is_displayed(UserProfilePage.my_profile)

