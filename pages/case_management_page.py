from .locators import CaseManagementPageLocator
import time


class CaseManagementPage:
    def __init__(self, browser):
        self.browser = browser

    def load_case_management(self):
        time.sleep(5)
        self.browser.find_element(*CaseManagementPageLocator.URL_CASE_MANAGEMENT).click()

    def is_case_management_title_displayed(self):
        time.sleep(2)
        return self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_TITLE).is_displayed()

    def is_case_management_participant_displayed(self):
        time.sleep(2)
        return self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_PARTICIPANT).is_displayed()

    def expand_left_menu(self):
        time.sleep(2)
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_ITEM).click()

    def click_new_referrals(self):
        time.sleep(2)
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_NEW_REFERRALS).click()

    def click_add_new_referral(self):
        time.sleep(2)
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_ADD_NEW_REFERRAL).click()

    def click_all_programs(self):
        time.sleep(2)
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_ALL_PROGRAMS).click()

