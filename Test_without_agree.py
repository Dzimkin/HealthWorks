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

time.sleep(10)

submit_button = browser.find_element(By.XPATH, "//button[contains(.,'Submit')]")
submit_button.click()

time.sleep(1)
error_message = browser.find_element(By.XPATH, "(//div[contains(.,'You must agree to HWA Terms and Conditions')])[4]")
assert error_message.is_displayed(), "Error message is not displayed"

browser.quit()