import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


class TestLogin:
    @pytest.mark.need_review
    def test_with_agree(self, browser):
        link = "https://dev.hwa-demo2.com/login"
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(5)
        username = browser.find_element(By.ID, "basic_username")
        username.send_keys("forndldoka7+admin@gmail.com")
        password = browser.find_element(By.ID, "basic_password")
        password.send_keys("1234567Zx!")
        agree_checkbox = browser.find_element(By.ID, "basic_agree")
        agree_checkbox.click()
        submit_button = browser.find_element(By.XPATH, "//button[contains(.,'Submit')]")
        submit_button.click()
        time.sleep(10)
        main_page_title = browser.find_element(By.XPATH,
                                               "(//section[contains(.,'Welcome to HealthWorks Analytics™!Visual Intelligence™ Brought to Life for Your Organization')])[4]")
        assert main_page_title.is_displayed(), "Is not displayed 'Welcome to HealthWorks Analytics™! Visual Intelligence™ Brought to Life for Your Organization'"

    @pytest.mark.need_review
    def test_without_agree(self, browser):
        link = "https://dev.hwa-demo2.com/login"
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(5)
        username = browser.find_element(By.ID, "basic_username")
        username.send_keys("forndldoka7+admin@gmail.com")
        password = browser.find_element(By.ID, "basic_password")
        password.send_keys("1234567Zx!")
        submit_button = browser.find_element(By.XPATH, "//button[contains(.,'Submit')]")
        submit_button.click()
        time.sleep(1)
        error_message = browser.find_element(By.XPATH,
                                             "(//div[contains(.,'You must agree to HWA Terms and Conditions')])[4]")
        assert error_message.is_displayed(), "Error message is not displayed"


class TestMainPage:
    @pytest.mark.need_review
    def test_main_page(self, browser):
        link = "https://dev.hwa-demo2.com/login"
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(5)
        username = browser.find_element(By.ID, "basic_username")
        username.send_keys("forndldoka7+admin@gmail.com")
        password = browser.find_element(By.ID, "basic_password")
        password.send_keys("1234567Zx!")
        agree_checkbox = browser.find_element(By.ID, "basic_agree")
        agree_checkbox.click()
        submit_button = browser.find_element(By.XPATH, "//button[contains(.,'Submit')]")
        submit_button.click()
        time.sleep(10)
        analytics = browser.find_element(By.XPATH, "(//h3[@class='card-info__title'])[1]")
        dion = browser.find_element(By.XPATH, "(//h3[@class='card-info__title'])[2]")
        case_management = browser.find_element(By.XPATH, "(//h3[@class='card-info__title'])[3]")
        administration = browser.find_element(By.XPATH, "(//h3[@class='card-info__title'])[4]")
        audit_management = browser.find_element(By.XPATH, "(//h3[@class='card-info__title'])[5]")
        assert analytics.is_displayed(), "Analytics is not displayed"
        assert dion.is_displayed(), "Dìon® is not displayed"
        assert case_management.is_displayed(), "Case Management is not displayed"
        assert administration.is_displayed(), "Administration is not displayed"
        assert audit_management.is_displayed(), "Audit Management is not displayed"


class TestAnalytics:
    def test_analytics(self, browser):
        link = "https://dev.hwa-demo2.com/login"
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(5)
        username = browser.find_element(By.ID, "basic_username")
        username.send_keys("forndldoka7+admin@gmail.com")
        password = browser.find_element(By.ID, "basic_password")
        password.send_keys("1234567Zx!")
        agree_checkbox = browser.find_element(By.ID, "basic_agree")
        agree_checkbox.click()
        submit_button = browser.find_element(By.XPATH, "//button[contains(.,'Submit')]")
        submit_button.click()
        time.sleep(10)
        analytics = browser.find_element(By.XPATH, "(//h3[@class='card-info__title'])[1]")
        analytics.click()
        time.sleep(5)
        analytics_title = browser.find_element(By.XPATH,
                                               "//span[contains(@title,'Dashboards list')]")
        assert analytics_title.is_displayed(), "Is not displayed 'Dashboards list"
        analytics_subscribed_tab = browser.find_element(By.XPATH,
                                                        "//div[@role='tab'][contains(.,'Subscribed')]")
        assert analytics_subscribed_tab.is_displayed(), "Is not displayed 'Subscribed tab"
        analytics_dashboard_cards = browser.find_element(By.XPATH,
                                                         "//div[@class='ant-layout-sider-children']")
        assert analytics_dashboard_cards.is_displayed(), "Is not displayed 'Subscribed tab"

class TestDion:
    def test_dion(self, browser):
        link = "https://dev.hwa-demo2.com/login"
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(5)
        username = browser.find_element(By.ID, "basic_username")
        username.send_keys("forndldoka7+admin@gmail.com")
        password = browser.find_element(By.ID, "basic_password")
        password.send_keys("1234567Zx!")
        agree_checkbox = browser.find_element(By.ID, "basic_agree")
        agree_checkbox.click()
        submit_button = browser.find_element(By.XPATH, "//button[contains(.,'Submit')]")
        submit_button.click()
        time.sleep(10)
        dion = browser.find_element(By.XPATH, "(//h3[@class='card-info__title'])[2]")
        dion.click()
        time.sleep(5)
        dion_title = browser.find_element(By.XPATH,
                                               "//span[contains(@title,'Dìon® settings')]")
        assert dion_title.is_displayed(), "Is not displayed 'Dìon® settings"
        dion_etl_db_configuration_button = browser.find_element(By.XPATH,
                                                        "(//span[contains(.,'ETL DB Configuration')])[2]")
        assert dion_etl_db_configuration_button.is_displayed(), "Is not displayed 'ETL DB Configuration button"

