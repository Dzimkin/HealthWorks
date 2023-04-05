from .locators import LoginPageLocator
import time


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(LoginPageLocator.URL)
        time.sleep(5)

    def set_username(self, username):
        self.browser.find_element(*LoginPageLocator.USERNAME).send_keys(username)

    def set_password(self, password):
        self.browser.find_element(*LoginPageLocator.PASSWORD).send_keys(password)

    def agree_to_terms(self):
        self.browser.find_element(*LoginPageLocator.AGREE_CHECKBOX).click()

    def submit(self):
        self.browser.find_element(*LoginPageLocator.SUBMIT_BUTTON).click()

    def is_error_displayed(self):
        time.sleep(1)
        return self.browser.find_element(*LoginPageLocator.ERROR_MESSAGE).is_displayed()
