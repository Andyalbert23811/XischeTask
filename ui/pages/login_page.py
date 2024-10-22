from selenium.webdriver.common.by import By
from helpers.driver_actions import DriverActions


class LoginPage(DriverActions):
    Email_field = (By.XPATH, '//*[@id="username"]')
    Password_field = (By.XPATH, '//*[@id="password"]')
    Sign_in_button = (By.XPATH, '//*[@type="submit"]')

    def fill_email_field(self,email):
        self.enter_text(self.Email_field,email)

    def fill_password_field(self,password):
        self.enter_text(self.Password_field,password)

    def click_sign_in_button(self):
        self.click_element(self.Sign_in_button)
