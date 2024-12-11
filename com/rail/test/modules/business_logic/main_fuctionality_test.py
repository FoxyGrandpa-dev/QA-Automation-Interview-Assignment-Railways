import time

import pytest

from Config import HOME_PAGE
from com.rail.main.utils.AssertionsHelper import AssertionsHelper
from com.rail.main.utils.ProjectLog import ProjectLog
from com.rail.main.utils.WebdriverHelper import WebdriverHelper
from com.rail.main.flows.HomeFlows import HomeFlows


class TestMainFunctionality:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = WebdriverHelper(HOME_PAGE)
        self.assertions = AssertionsHelper(self.driver)
        self.logger = ProjectLog().get_logger()
        self.home_flows = HomeFlows(self.driver)

    def teardown_method(self):
        self.logger.log(20, "Starting Teardown")
        self.driver.close_driver()

    def test_search_bar(self):
        self.home_flows.perform_search_select_first("HTML Button tag")
        self.assertions.assert_correct_page("https://www.w3schools.com/tags/tag_button.asp")
