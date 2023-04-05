from .locators import AnalyticsPageLocator
import time


class AnalyticsPage:
    def __init__(self, browser):
        self.browser = browser

    def load_analytics(self):
        time.sleep(10)
        self.browser.find_element(*AnalyticsPageLocator.URL_ANALYTICS).click()

    def is_analytics_title_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*AnalyticsPageLocator.ANALYTICS_TITLE).is_displayed()

    def is_analytics_subscribed_tab_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*AnalyticsPageLocator.ANALYTICS_DASHBOARD_CARDS).is_displayed()

    def is_analytics_dashboard_cards_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*AnalyticsPageLocator.ANALYTICS_DASHBOARD_CARDS).is_displayed()
