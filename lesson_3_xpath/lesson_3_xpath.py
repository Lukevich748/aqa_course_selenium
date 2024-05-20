import time

from selenium import webdriver


driver = webdriver.Chrome()

# 1
driver.get("https://vk.com")
print(driver.title)

driver.get("https://ru.wikipedia.org")
print(driver.title)

driver.back()
assert driver.current_url == "https://vk.com/", "url is not correct"
driver.refresh()
print(driver.current_url)
driver.forward()
assert driver.current_url is not "https://vk.com/", "url hasn't changed"