from .locators import MainPageLocator
import time

class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def is_title_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*MainPageLocator.TITLE).is_displayed()
