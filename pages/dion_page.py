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

    def is_analytics_dashboard_cards_displayed(self):
        time.sleep(10)
        return self.browser.find_element(*DionPageLocator.ANALYTICS_DASHBOARD_CARDS).is_displayed()


import requests
from bs4 import BeautifulSoup

# Получение HTML-кода первой страницы
page1 = requests.get("https://www.example.com/page1")
soup1 = BeautifulSoup(page1.content, 'html.parser')

# Извлечение текста из первой страницы
text1 = soup1.get_text()

# Получение HTML-кода второй страницы
page2 = requests.get("https://www.example.com/page2")
soup2 = BeautifulSoup(page2.content, 'html.parser')

# Извлечение текста из второй страницы
text2 = soup2.get_text()

# Сравнение текста на двух страницах
if text1 == text2:
    print("Текст на двух страницах идентичен")
else:
    print("Текст на двух страницах отличается")