from .locators import DionPageLocator
import time


class DionPage:
    def __init__(self, browser):
        self.browser = browser

    def load_analytics(self):
        time.sleep(10)
        self.browser.find_element(*DionPageLocator.URL_DION).click()

    def is_analytics_title_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*DionPageLocator.DION_TITLE).is_displayed()

    def is_analytics_subscribed_tab_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*DionPageLocator.DION_ETL_DB_CONFIGURATION_TAB).is_displayed()


