import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Открываем веб-браузер и переходим на страницу входа
browser = webdriver.Chrome()
browser.get("https://dev.hwa-demo2.com/login")

# Устанавливаем ожидание в 10 секунд
time.sleep(10)

# Находим поле ввода логина и вводим данные
username = browser.find_element(By.ID, "basic_username")
username.send_keys("forndldoka7+admin@gmail.com")

# Находим поле ввода пароля и вводим данные
password = browser.find_element(By.ID, "basic_password")
password.send_keys("1234567Zx!")

# Устанавливаем  ожидание в 10 секунд
time.sleep(10)

# Нажимаем кнопку "Submit"
submit_button = browser.find_element(By.XPATH, "//button[contains(.,'Submit')]")
submit_button.click()

# Проверяем, что сообщение об ошибке "You must agree to HWA Terms and Conditions" отображается на странице
time.sleep(1) # ждем 2 секунды для загрузки страницы
error_message = browser.find_element(By.XPATH, "(//div[contains(.,'You must agree to HWA Terms and Conditions')])[4]")
assert error_message.is_displayed(), "Error message is not displayed"

# Закрываем браузер
browser.quit()