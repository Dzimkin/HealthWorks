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

# Выбираем чекбокс "I agree to HWA Terms and Conditions"
agree_checkbox = browser.find_element(By.ID, "basic_agree")
# Кликаем на чекбокс
agree_checkbox.click()


# Нажимаем кнопку "Submit"
submit_button = browser.find_element(By.XPATH, "//button[contains(.,'Submit')]")
submit_button.click()

## ожидание загрузки главной страницы и проверка заголовка
time.sleep(10) # ждем 2 секунды для загрузки страницы
main_page_title = browser.find_element(By.XPATH, "(//section[contains(.,'Welcome to HealthWorks Analytics™!Visual Intelligence™ Brought to Life for Your Organization')])[4]")
# утверждение, что заголовок главной страницы верный
assert main_page_title.is_displayed(), "Is not displayed 'Welcome to HealthWorks Analytics™! Visual Intelligence™ Brought to Life for Your Organization'"

# закрытие браузера
browser.quit()
