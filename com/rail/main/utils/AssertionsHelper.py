from selenium.webdriver.common.by import By

from com.rail.main.utils.ProjectLog import ProjectLog


class AssertionsHelper:

    def __init__(self, driver):
        self.driver = driver
        self.logger = ProjectLog().get_logger()

    def assert_element_is_displayed(self, web_element_locator):
        """
        perform an assertion at the end of a test - that an element is displayed in the DOM
        :param web_element_locator: tuple of locator type and DOM locator
            Example: (By.XPATH, "//input[@name='email']")
        """
        assert self.driver.find_element(web_element_locator).is_displayed()

    def assert_correct_page(self, expected_url):
        """
        given an expected url - asserts if the current url is == to expected url
        :param expected_url: expected resulting url after test steps
        """
        self.logger.info(f"expected url: {expected_url} - current_url: {self.driver.get_current_url()}")
        assert self.driver.get_current_url() == expected_url

