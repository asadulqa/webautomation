from selenium.webdriver.common.by import By
from page.basepage import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.driver.find_element(By.ID, LoginLocators.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, LoginLocators.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, LoginLocators.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(By.XPATH, LoginLocators.ERROR_MESSAGE).text
