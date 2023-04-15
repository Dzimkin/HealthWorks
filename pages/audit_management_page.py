from .locators import AuditManagementPageLocator
import time


class AuditManagementPage:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(AuditManagementPageLocator.URL_AUDIT_MANAGEMENT)
        time.sleep(5)