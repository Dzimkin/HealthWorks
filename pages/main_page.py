from .locators import MainPageLocator
import time


class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def is_title_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*MainPageLocator.TITLE).is_displayed()

    def is_analytics_displayed(self):
        time.sleep(5)
        return self.browser.find_element(*MainPageLocator.ANALYTICS).is_displayed()

    def is_dion_displayed(self):
        time.sleep(5)
        return self.browser.find_element(*MainPageLocator.DION).is_displayed()

    def is_case_management_displayed(self):
        time.sleep(5)
        return self.browser.find_element(*MainPageLocator.CASE_MANAGEMENT).is_displayed()

    def is_administration_displayed(self):
        time.sleep(5)
        return self.browser.find_element(*MainPageLocator.ADMINISTRATION).is_displayed()

    def is_audit_management_displayed(self):
        time.sleep(5)
        return self.browser.find_element(*MainPageLocator.AUDIT_MANAGEMENT).is_displayed()
