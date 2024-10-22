import time
import unittest
from selenium import webdriver
from helpers.driver_actions import BasePage
from pages import home_page, login_page

class GoogleLoginTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.base_page = BasePage(options=options)
        self.driver = self.base_page.driver
        self.driver.get("https://www.linkedin.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        Homepages = home_page.HomePage(self.driver)
        Homepages.click_login_redirection_button()
        time.sleep(1)

    def test_valid_credentials(self):
        LoginPage = login_page.LoginPage(self.driver)
        LoginPage.fill_email_field("Correct email")
        LoginPage.fill_password_field("Correct password")
        time.sleep(2)
        self.assertEqual(self.driver.current_url, "https://www.linkedin.com/feed/")

    def test_invalid_credentials(self):
        LoginPage = login_page.LoginPage(self.driver)
        LoginPage.fill_email_field("invalid email")
        LoginPage.fill_password_field("wrong password")
        time.sleep(1)
        assert "Please enter a valid username." in self.driver.page_source

    def test_empty_fields(self):
        LoginPage = login_page.LoginPage(self.driver)
        LoginPage.fill_email_field("")
        LoginPage.fill_password_field("")
        time.sleep(1)
        assert "Please enter an email address or phone number." in self.driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()