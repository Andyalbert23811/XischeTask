import unittest
from xmlrunner import XMLTestRunner
import os
from Utils import csv_helper
from pages import login_page, home_page
from helpers import browser_actions

class TestLogin(unittest.TestCase):
    def setUp(self):
        browser_actions_instance = browser_actions.BrowserActions()
        self.driver = browser_actions_instance.initialize_driver()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_dir, 'testdata.csv')

        csv_helper_instance = csv_helper.CSVHelper()
        self.test_data = csv_helper_instance.read_csv(csv_path)

        self.driver.get("https://www.linkedin.com/")
        self.driver.maximize_window()
        HomePage = home_page.HomePage(self.driver)
        HomePage.click_login_redirection_button()
        self.driver.implicitly_wait(10)

    def test_login_with_correct_credentials(self):
        username, password = self.test_data[0]
        LoginPage = login_page.LoginPage(self.driver)
        LoginPage.fill_email_field(username)
        LoginPage.fill_password_field(password)
        LoginPage.click_sign_in_button()
        # As we cant add real credentials assertion should be
        # assert self.driver.current_url == "https://www.linkedin.com/feed/"

    def test_login_with_invalid_credentials(self):
        username, password = self.test_data[1]
        LoginPage = login_page.LoginPage(self.driver)
        LoginPage.fill_email_field(username)
        LoginPage.fill_password_field(password)
        LoginPage.click_sign_in_button()
        assert "Please enter a valid username." in self.driver.page_source

    def test_login_with_empty_credentials(self):
        username, password = self.test_data[2]
        LoginPage = login_page.LoginPage(self.driver)
        LoginPage.fill_email_field(username)
        LoginPage.fill_password_field(password)
        LoginPage.click_sign_in_button()
        assert "Please enter an email address or phone number." in self.driver.page_source

    def test_login_with_valid_user_name_and_empty_password(self):
        username, password = self.test_data[3]
        LoginPage = login_page.LoginPage(self.driver)
        LoginPage.fill_email_field(username)
        LoginPage.fill_password_field(password)
        LoginPage.click_sign_in_button()
        assert "Please enter a password." in self.driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test-reports.xml')
    print("report path:")
    print(report_path)
    with open(report_path, 'wb') as output:
        unittest.main(testRunner=XMLTestRunner(output=output))