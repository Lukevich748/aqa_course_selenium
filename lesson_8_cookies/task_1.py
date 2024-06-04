from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

driver.get("https://vk.com")

driver.add_cookie(
    {
        "name": "username",
        "value": "user123"
    }
)
driver.refresh()
cookie = driver.get_cookie("username")

assert cookie is not None, "The cookie was not added"
assert cookie["name"] == "username" and cookie["value"] == "user123", "Сookie data is incorrect"

print(cookie)

driver.quit()