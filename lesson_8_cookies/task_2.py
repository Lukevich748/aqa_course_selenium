from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

driver.get("https://www.onliner.by")

driver.add_cookie(
    {
        "name": "username",
        "value": "user123"
    }
)

driver.refresh()
driver.delete_cookie("username")
driver.refresh()
cookie = driver.get_cookie("username")
assert cookie is None, "Cookie is not deleted"

driver.quit()