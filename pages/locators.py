from selenium.webdriver.common.by import By


class MainPageLocator:
    TITLE = (By.XPATH, "(//section[contains(.,'Welcome to HealthWorks Analytics™!Visual Intelligence™ Brought to Life for Your Organization')])[4]")
    ANALYTICS = (By.XPATH, "//h3[contains(.,'Analytics')]")
    DION = (By.XPATH, "//h3[contains(.,'Dìon®')]")
    CASE_MANAGEMENT = (By.XPATH, "//h3[contains(.,'Case Management')]")
    ADMINISTRATION = (By.XPATH, "//h3[contains(.,'Administration')]")
    AUDIT_MANAGEMENT = (By.XPATH, "//h3[contains(.,'Audit Management')]")
    CARDS = (By.XPATH, "//div[@class='cards']/div")


class LoginPageLocator:
    URL = "https://dev.hwa-demo2.com/"
    USERNAME = (By.ID, "basic_username")
    PASSWORD = (By.ID, "basic_password")
    AGREE_CHECKBOX = (By.ID, "basic_agree")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(.,'Submit')]")
    ERROR_MESSAGE = (By.XPATH, "(//div[contains(.,'You must agree to HWA Terms and Conditions')])[4]")

