from .locators import CaseManagementPageLocator
import time


class CaseManagementPage:
    def __init__(self, browser):
        self.browser = browser

    def load_case_management(self):
        time.sleep(10)
        self.browser.find_element(*CaseManagementPageLocator.URL_CASE_MANAGEMENT).click()

    def is_case_management_title_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_TITLE).is_displayed()

    def is_case_management_participant_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_PARTICIPANT).is_displayed()
