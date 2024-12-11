from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class WebdriverHelper:
    """
    WebdriverHelper is a Wrapper of the selenium package designed in a singleton design pattern,
    the driver is instantiated once and no matter how many times the constructor is called
    the same instance is referenced insuring WebDriver continuity and consistency
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(WebdriverHelper, cls).__new__(cls)
        return cls._instance

    def __init__(self, url):
        """
        constructor of the WebdriverHelper class
        sets up the browser options and driver version according to your Chrome version
        and finally opens the web browser to a specified url
        :param url: full address of the webpage the webdriver should open
        """
        service = Service(ChromeDriverManager().install())
        chrome_options = Options()
        second_screen_width = 1920
        chrome_options.add_argument(f"--window-position={second_screen_width},0")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get(url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, web_element_locator):
        """
        wrapper method of the selenium WebDriver.click() method with explicit wait and error handling
        :param web_element_locator: a tuple containing a string representing locator strategy and the locator itself
        example: (By.XPATH, "//input[@type='email']") or ("xpath", "//input[@type='email']")
        :return: None
        """
        try:
            self.wait.until(ec.presence_of_element_located((web_element_locator[0], web_element_locator[1]))).click()
        except NoSuchElementException as e:
            print(e)
        except ElementNotInteractableException as e:
            print(e)

    def send_keys(self, web_element_locator, text):
        """
        wrapper method of the selenium WebDriver.sendKeys() method with explicit wait and error handling
        :param web_element_locator: a tuple containing a string representing locator strategy and the locator itself
        example: (By.XPATH, "//input[@type='email']") or ("xpath", "//input[@type='email']")
        :param text: text that will get sent to the web element (usually an input tag)
        :return: None
        """
        try:
            self.wait.until(ec.presence_of_element_located((web_element_locator[0], web_element_locator[1]))).send_keys(text)
        except NoSuchElementException as e:
            print(e)
        except ElementNotInteractableException as e:
            print(e)

    def find_element(self, web_element_locator):
        """
        wrapper method of the selenium WebDriver.find_element() method with explicit wait and error handling
        :param web_element_locator: a tuple containing a string representing locator strategy and the locator itself
        example: (By.XPATH, "//input[@type='email']") or ("xpath", "//input[@type='email']")
        :return: WebElement Object corresponding to supplied locator
        """
        if web_element_locator[0] == "xpath":
            self.wait.until(ec.presence_of_element_located((By.XPATH, web_element_locator[1])))
            return self.driver.find_element(By.XPATH, web_element_locator[1])
        elif web_element_locator[0] == "css":
            self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, web_element_locator[1])))
            return self.driver.find_element(By.CSS_SELECTOR, web_element_locator[1])

    def find_elements(self, web_element_locator):
        """
        wrapper method of the selenium WebDriver.find_elements() method with explicit wait and error handling
        :param web_element_locator: a tuple containing a string representing locator strategy and the locator itself
        example: (By.XPATH, "//input[@type='email']") or ("xpath", "//input[@type='email']")
        :return: a list [] of WebElement Object corresponding to supplied locator
        """
        list_of_elements = []
        if web_element_locator[0] == "xpath":
            locator_strategy = By.XPATH
            self.wait.until(ec.presence_of_all_elements_located((By.XPATH, web_element_locator[1])))
        elif web_element_locator[0] == "css":
            locator_strategy = By.CSS_SELECTOR
            self.wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, web_element_locator[1])))
        try:
            for web_element in self.driver.find_elements(locator_strategy, web_element_locator[1]):
                list_of_elements.append(web_element)
            return list_of_elements
        except Exception as e:
            print(e)

    def get_element_inner_html(self, web_element):
        """
        :param web_element: webElement object or a list of webElements returned from find_element() or find_elements()
        :return: the inner html text or a list with all webElements texts
        """
        result = []
        if isinstance(web_element, list):
            for element in web_element:
                result.append(element)
            return result
        else:
            return web_element.text

    def js_executor(self, script):
        """
        wrapper of javascript executor
        :param script: js script / command
        :return: None
        """
        self.driver.execute_script(script)

    def get_current_url(self):
        """
        :return: the current url where the WebDriver in currently interacting
        """
        return self.driver.current_url

    def close_driver(self):
        """
        closes the webdriver + browser and frees up system memory
        """
        self.driver.quit()
