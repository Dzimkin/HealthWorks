from .locators import AuditManagementPageLocator
import time


class AuditManagementPage:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(AuditManagementPageLocator.URL_AUDIT_MANAGEMENT)
        time.sleep(5)

    def load_audit_management(self):
        time.sleep(10)
        self.browser.find_element(*AuditManagementPageLocator.URL_AUDIT_MANAGEMENT).click()

    def is_audit_management_title_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*AuditManagementPageLocator.AUDIT_MANAGEMENT_TITLE).is_displayed()

    def is_audit_management_table_with_logs_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*AuditManagementPageLocator.AUDIT_MANAGEMENT_TABLE_WITH_LOG).is_displayed()
