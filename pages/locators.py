from selenium.webdriver.common.by import By


class MainPageLocator:
    TITLE = (By.XPATH,
             "(//section[contains(.,'Welcome to HealthWorks Analytics™!"
             "Visual Intelligence™ Brought to Life for Your Organization')])[4]")

    ANALYTICS = (By.XPATH, "(//h3[@class='card-info__title'])[1]")
    DION = (By.XPATH, "(//h3[@class='card-info__title'])[2]")
    CASE_MANAGEMENT = (By.XPATH, "(//h3[@class='card-info__title'])[3]")
    ADMINISTRATION = (By.XPATH, "(//h3[@class='card-info__title'])[4]")
    AUDIT_MANAGEMENT = (By.XPATH, "(//h3[@class='card-info__title'])[5]")
    CARDS = (By.XPATH, "//div[@class='cards']/div")


class LoginPageLocator:
    URL = "https://dev.hwa-demo2.com/"
    USERNAME = (By.ID, "basic_username")
    PASSWORD = (By.ID, "basic_password")
    AGREE_CHECKBOX = (By.ID, "basic_agree")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(.,'Submit')]")
    ERROR_MESSAGE = (By.XPATH, "(//div[contains(.,'You must agree to HWA Terms and Conditions')])[4]")


class AnalyticsPageLocator:
    URL_ANALYTICS = (By.XPATH, "(//h3[@class='card-info__title'])[1]")
    ANALYTICS_TITLE = (By.XPATH, "//span[contains(@title,'Dashboards list')]")
    ANALYTICS_SUBSCRIBED_TAB = (By.XPATH, "//div[@role='tab'][contains(.,'Subscribed')]")
    ANALYTICS_DASHBOARD_CARDS = (By.XPATH, "//div[@class='ant-layout-sider-children']")

class DionPageLocator:
    URL_DION = (By.XPATH, "(//h3[@class='card-info__title'])[2]")
    DION_TITLE = (By.XPATH, "//span[contains(@title,'Dìon® settings')]")
    DION_ETL_DB_CONFIGURATION_TAB = (By.XPATH, "(//span[contains(.,'ETL DB Configuration')])[2]")
    DION_TOPICS_HEALTH_ASSESSMENT_DASHBOARD = (By.XPATH, "//a[contains(.,'Health Assessment Dashboard')]")
    DION_TOPICS_HEALTH_ASSESSMENT_DASHBOARD = (By.XPATH, "//a[contains(.,'Health Assessment Dashboard')]")