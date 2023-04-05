from .locators import AnaliticsPageLocator
import time

class AnaliticsPage:
    def __init__(self, browser):
        self.browser = browser

    def load_Analitics(self):
        self.browser.get(AnaliticsPageLocator.URL_ANALYTICS)
        time.sleep(5)