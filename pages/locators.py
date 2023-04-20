from selenium.webdriver.common.by import By


class MainPageLocator:
    TITLE = (By.XPATH,
             "//div[@class='ant-page-header-heading'][contains(.,'Welcome to HealthWorks Analytics™!')]")

    ANALYTICS = (By.XPATH, "//h3[@class='card-info__title'][contains(.,'Analytics')]")
    DION = (By.XPATH, "//h3[@class='card-info__title'][contains(.,'Dìon®')]")
    CASE_MANAGEMENT = (By.XPATH, "//h3[@class='card-info__title'][contains(.,'Case Management')]")
    ADMINISTRATION = (By.XPATH, "//h3[@class='card-info__title'][contains(.,'Administration')]")
    AUDIT_MANAGEMENT = (By.XPATH, "//h3[@class='card-info__title'][contains(.,'Audit Management')]")
    CARDS = (By.XPATH, "//div[@class='cards']/div")


class LoginPageLocator:
    URL = "https://dev.hwa-demo2.com/"
    USERNAME = (By.ID, "basic_username")
    PASSWORD = (By.ID, "basic_password")
    AGREE_CHECKBOX = (By.ID, "basic_agree")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(.,'Submit')]")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='ant-notification-notice-message']"
                               "[contains(.,'You must agree to HWA Terms and Conditions')]")


class AnalyticsPageLocator:
    URL_ANALYTICS = (By.XPATH, "//h3[@class='card-info__title'][contains(.,'Analytics')]")
    ANALYTICS_TITLE = (By.XPATH, "//span[contains(@title,'Dashboards list')]")
    ANALYTICS_SUBSCRIBED_TAB = (By.XPATH, "//div[@role='tab'][contains(.,'Subscribed')]")
    ANALYTICS_DASHBOARD_CARDS = (By.XPATH, "//div[@class='ant-layout-sider-children']")


class DionPageLocator:
    URL_DION = (By.XPATH, "//h3[@class='card-info__title'][contains(.,'Dìon®')]")
    DION_TITLE = (By.XPATH, "//span[contains(@title,'Dìon® settings')]")
    DION_ETL_DB_CONFIGURATION_TAB = (By.XPATH, "//button[contains(.,'ETL DB Configuration')]")
    DION_TOPICS_HEALTH_ASSESSMENT_DASHBOARD = (By.XPATH, "//a[contains(.,'Health Assessment Dashboard')]")


class CaseManagementPageLocator:
    URL_CASE_MANAGEMENT = (By.XPATH, "//h3[@class='card-info__title'][contains(.,'Case Management')]")
    CASE_MANAGEMENT_TITLE = (By.XPATH, "//span[@class='header-title'][contains(.,'My Cases')]")
    CASE_MANAGEMENT_PARTICIPANT = (By.XPATH, "//table[contains(@style, 'table-layout')]")
    CASE_MANAGEMENT_ITEM = (By.XPATH, "//div[@class='ant-menu-submenu-title'][contains(.,'Case management')]")
    CASE_MANAGEMENT_NEW_REFERRALS = (By.XPATH, "//span[@class='ant-menu-title-content'][contains(.,'New Referrals')]")
    CASE_MANAGEMENT_ADD_NEW_REFERRAL = (By.XPATH, "//button[contains(.,'Add new referral')]")
    CASE_MANAGEMENT_PARTICIPANT_NAME = (By.XPATH, "//input[@placeholder='Enter participant name here...']")
    CASE_MANAGEMENT_REFERRAL_SOURCE = (By.XPATH, "//input[@placeholder='Enter referral source here...']")
    CASE_MANAGEMENT_REFERRAL_DATE = (By.XPATH, "//input[contains(@id,'date')][@placeholder='Select date here...']")
    CASE_MANAGEMENT_REFERRAL_PROGRAM = (By.XPATH, "//input[@placeholder='Enter referral program here...']")
    CASE_MANAGEMENT_CONTACT_NUMBER = (By.XPATH, "//input[@placeholder='(000) 000-0000']")
    CASE_MANAGEMENT_CONTACT_EMAIL = (By.XPATH, "// input[contains( @ id, 'email')]")
    CASE_MANAGEMENT_SUBMIT = (By.XPATH, "//span[contains(.,'Submit')]")
    CASE_MANAGEMENT_MESSAGE = (By.XPATH, "// div[ @class ='ant-notification-notice-message']"
                                         "[contains(., 'The referral has been added successfully')]")
    CASE_MANAGEMENT_NEW_REFERRALS_ADD = (By.XPATH, "//tr//td[contains(text(),'shdn')]")






class AdministrationPageLocator:
    URL_ADMINISTRATION = (By.XPATH, "//h3[@class='card-info__title'][contains(.,'Administration')]")
    ADMINISTRATION_TITLE = (By.XPATH, "//span[contains(@title,'Users')]")
    ADMINISTRATION_ADD_USER = (By.XPATH, "//button[contains(.,'Add User')]")
    ADMINISTRATION_IMPORT_USER = (By.XPATH, "//button[contains(.,'Import users')]")
    ADMINISTRATION_DEACTIVATE = (By.XPATH, "//button[contains(.,'Deactivate')]")
    ADMINISTRATION_FORCE_LOG_OUT = (By.XPATH, "//button[contains(.,'Force Log Out')]")
    ADMINISTRATION_REQUEST_RESET_PASSWORD = (By.XPATH, "//button[contains(.,'Request reset password')]")
    ADMINISTRATION_USERS = (By.XPATH, '//tr[contains(@class, "ant-table")]')


class AuditManagementPageLocator:
    URL_AUDIT_MANAGEMENT = (By.XPATH, "//h3[contains(.,'Audit Management')]")
    AUDIT_MANAGEMENT_TITLE = (By.XPATH, "//span[contains(@title,'Audit log')]")
    AUDIT_MANAGEMENT_TABLE_WITH_LOG = (By.XPATH, "//table[contains(@style, 'table-layout')]")
