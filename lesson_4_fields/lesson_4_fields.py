from selenium import webdriver

driver = webdriver.Chrome()

# # 1
driver.get("https://demoqa.com/text-box")

FULL_NAME_FIELD = ("xpath", "//input[@id='userName']")
EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
CURRENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='currentAddress']")
PERMANENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='permanentAddress']")


full_name_field = driver.find_element(*FULL_NAME_FIELD)
full_name_field.clear()
assert full_name_field.get_attribute("value") == ""
full_name_field.send_keys("Lukevich Artem")
assert "Lukevich Artem" in full_name_field.get_attribute("value")

email_field = driver.find_element(*EMAIL_FIELD)
email_field.clear()
assert email_field.get_attribute("value") == ""
email_field.send_keys("lukevichartem@gmail.com")
assert "lukevichartem@gmail.com" in email_field.get_attribute("value")

current_address_field = driver.find_element(*CURRENT_ADDRESS_FIELD)
current_address_field.clear()
assert current_address_field.get_attribute("value") == ""
current_address_field.send_keys("Rondo Daszynskiego 100")
assert "Rondo Daszynskiego 100" in current_address_field.get_attribute("value")

permanent_address_field = driver.find_element(*PERMANENT_ADDRESS_FIELD)
permanent_address_field.clear()
assert permanent_address_field.get_attribute("value") == ""
permanent_address_field.send_keys("Rondo Daszynskiego 50")
assert "Rondo Daszynskiego 50" in permanent_address_field.get_attribute("value")

# 2
driver.get("https://the-internet.herokuapp.com/login")

USER_NAME_FILED = ("xpath", "//input[@id='username']")
PASSWORD_FILED = ("xpath", "//input[@id='password']")
LOGIN_BUTTON = ("xpath", "//button[@type='submit']")
LOGOUT_BUTTON = ("xpath", "//a[@class='button secondary radius']")

login = "tomsmith"
password = "SuperSecretPassword!"

user_name_field = driver.find_element(*USER_NAME_FILED)
user_name_field.clear()
assert user_name_field.get_attribute("value") == ""
user_name_field.send_keys(login)
assert "tomsmith" in user_name_field.get_attribute("value")

password_field = driver.find_element(*PASSWORD_FILED)
password_field.clear()
assert password_field.get_attribute("value") == ""
password_field.send_keys(password)
assert "SuperSecretPassword!" in password_field.get_attribute("value")

login_button = driver.find_element(*LOGIN_BUTTON)
login_button.click()
assert driver.find_element(*LOGOUT_BUTTON).is_displayed() or driver.find_element(*LOGIN_BUTTON).is_displayed() is False
