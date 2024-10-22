import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Utils import config_helper

class BrowserActions:

    def initialize_driver(self):
        # Use the absolute path to the CSV file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, '../test_cases/config.csv')

        # Read the browser type from the config file
        config_helper_instance = config_helper.ConfigHelper(config_path)
        browser_type = config_helper_instance.get_browser()

        # Initialize the appropriate WebDriver
        if browser_type == 'chrome':
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_type == 'firefox':
            service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service)
        elif browser_type == 'edge':
            edge_service = EdgeService()
            self.driver = webdriver.Edge(service=edge_service)
        elif browser_type == 'safari':
            self.driver = webdriver.Safari()
        else:
            raise ValueError("Unsupported browser: {}".format(browser_type))

        return self.driver