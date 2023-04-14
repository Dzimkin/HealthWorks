from .locators import AdministrationPageLocator
import time


class AdministrationPage:
    def __init__(self, browser):
        self.browser = browser

    def load_administration(self):
        time.sleep(10)
        self.browser.find_element(*AdministrationPageLocator.URL_ADMINISTRATION).click()

    def is_administration_title_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*AdministrationPageLocator.ADMINISTRATION_TITLE).is_displayed()

    def is_administration_add_user_button_enabled(self):
        time.sleep(10)
        return self.browser.find_element(*AdministrationPageLocator.ADMINISTRATION_ADD_USER).is_enabled()

    def is_administration_import_user_button_enabled(self):
        time.sleep(10)
        return self.browser.find_element(*AdministrationPageLocator.ADMINISTRATION_IMPORT_USER).is_enabled()

    def is_administration_deactivate_button_disabled(self):
        time.sleep(10)
        return not self.browser.find_element(*AdministrationPageLocator.ADMINISTRATION_DEACTIVATE).is_enabled()

    def is_administration_force_log_out_button_disabled(self):
        time.sleep(10)
        return not self.browser.find_element(*AdministrationPageLocator.ADMINISTRATION_FORCE_LOG_OUT).is_enabled()

    def is_administration_add_user_button_disabled(self):
        time.sleep(10)
        return not self.browser.find_element(*AdministrationPageLocator.ADMINISTRATION_REQUEST_RESET_PASSWORD).is_enabled()

    def is_administration_users_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*AdministrationPageLocator.ADMINISTRATION_USERS).is_displayed()
