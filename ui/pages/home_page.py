# pages/home_page.py
from selenium.webdriver.common.by import By

class HomePage:
    Login_redirection_button = (By.XPATH, '//*[@class="nav__button-secondary btn-secondary-emphasis btn-md"]')

    def __init__(self, driver):
        self.driver = driver

    def click_login_redirection_button(self):
        self.driver.find_element(*self.Login_redirection_button).click()