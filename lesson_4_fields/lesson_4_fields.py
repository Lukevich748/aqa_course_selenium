import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

FULL_NAME_FIELD = ("xpath", "//input[@id='userName']")


full_name_field = driver.find_element(*FULL_NAME_FIELD)
full_name_field.clear()
full_name_field.send_keys("Lukevich Artem")


time.sleep(3)