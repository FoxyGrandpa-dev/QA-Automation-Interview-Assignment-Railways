from com.rail.main.pages.HomePage import *


class HomeFlows:
    def __init__(self, driver):
        self.driver = driver

    def perform_search_select_first(self, search_term):
        """
        performs a search in the home page search box and selects the first option
        :param search_term: text for the search box
        :return: None
        """
        self.driver.send_keys(HomePage.main_search_box, search_term)
        self.driver.click(HomePage.list_of_search_results)

