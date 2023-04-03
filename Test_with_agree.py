import time
from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()
browser.get("https://dev.hwa-demo2.com/login")

time.sleep(10)

username = browser.find_element(By.ID, "basic_username")
username.send_keys("forndldoka7+admin@gmail.com")

password = browser.find_element(By.ID, "basic_password")
password.send_keys("1234567Zx!")

agree_checkbox = browser.find_element(By.ID, "basic_agree")
agree_checkbox.click()


submit_button = browser.find_element(By.XPATH, "//button[contains(.,'Submit')]")
submit_button.click()

time.sleep(10)
main_page_title = browser.find_element(By.XPATH, "(//section[contains(.,'Welcome to HealthWorks Analytics™!Visual Intelligence™ Brought to Life for Your Organization')])[4]")
assert main_page_title.is_displayed(), "Is not displayed 'Welcome to HealthWorks Analytics™! Visual Intelligence™ Brought to Life for Your Organization'"

browser.quit()
