from .locators import CaseManagementPageLocator
import time


class AddUserPage:
    def __init__(self, browser):
        self.browser = browser

    def set_name(self, name):
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_PARTICIPANT_NAME).send_keys(name)

    def set_source(self, source):
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_REFERRAL_SOURCE).send_keys(source)

    def set_date(self, date):
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_REFERRAL_DATE).send_keys(date)

    def set_program(self, program):
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_REFERRAL_PROGRAM).send_keys(program)

    def set_number(self, number):
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_CONTACT_NUMBER).send_keys(number)

    def submit(self):
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_SUBMIT).click()
