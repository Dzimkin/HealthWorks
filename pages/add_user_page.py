from .locators import CaseManagementPageLocator
from generate_user import generate_name, generate_source, generate_date, generate_program, generate_number
import time


class AddUserPage:
    def __init__(self, browser):
        self.browser = browser

    def set_name(self):
        name = generate_name()
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_PARTICIPANT_NAME).send_keys(name)

    def set_source(self):
        source = generate_source()
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_REFERRAL_SOURCE).send_keys(source)

    def set_date(self):
        date = generate_date()
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_REFERRAL_DATE).send_keys(date)

    def set_program(self):
        program = generate_program()
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_REFERRAL_PROGRAM).send_keys(program)

    def set_number(self):
        number = generate_number()
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_CONTACT_NUMBER).send_keys(number)

    def email(self):
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_CONTACT_EMAIL).click()

    time.sleep(5)

    def submit(self):
        self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_SUBMIT).click()

    def is_message_displayed(self):
        time.sleep(5)
        return self.browser.find_element(*CaseManagementPageLocator.CASE_MANAGEMENT_MESSAGE).is_displayed()
