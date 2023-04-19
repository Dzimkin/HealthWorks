from .locators import CaseManagementPageLocator
from generate_user import generate_name, generate_source, generate_date, generate_program, generate_number
from selenium.webdriver.common.by import By
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

    def is_new_referral_displayed(self):
        time.sleep(5)
        # name = generate_name()
        # source = generate_source()
        # date = generate_date()
        # program = generate_program()
        # number = generate_number()
        print(name)
        print(source)
        print(date)
        print(program)
        print(number)
        name_selector = str(f"//td[contains(.,'{name}')]")
        source_selector = str(f"//td[contains(.,'{source}')]")
        date_selector = str(f"//td[contains(.,'{date}')]")
        program_selector = str(f"//td[contains(.,'{program}')]")
        number_selector = str(f"//td[contains(.,'{number}')]")
        print(name_selector, source_selector, date_selector, program_selector, number_selector)
        return self.browser.find_element(By.XPATH, name_selector).is_displayed() and \
            self.browser.find_element(By.XPATH, source_selector).is_displayed() and \
            self.browser.find_element(By.XPATH, date_selector).is_displayed() and \
            self.browser.find_element(By.XPATH, program_selector).is_displayed() and \
            self.browser.find_element(By.XPATH, number_selector).is_displayed()
