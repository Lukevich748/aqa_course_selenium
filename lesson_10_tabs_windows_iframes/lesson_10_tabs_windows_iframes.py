import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

HYPERSKILL_PRICING_BUTTON_LOCATOR = ("xpath", "//li[@click-event-part='head']/a[contains(text(), 'Pricing')]")
ONLINER_FORUM_BUTTON_LOCATOR = ("xpath", "//nav[@class='b-top-navigation']//span[contains(text(), 'Форум')]")
OZON_CATALOG_BUTTON_LOCATOR = ("xpath", "//header[@data-widget='header']//button[@class='b214-a0 b214-b5']")

driver.get("https://hyperskill.org/login")
hyperskill_tab = driver.current_window_handle

driver.switch_to.new_window("tab")
driver.get("https://www.onliner.by")
onliner_tab = driver.current_window_handle

driver.switch_to.new_window("tab")
driver.get("https://www.ozon.ru")
ozon_tab = driver.current_window_handle

driver.switch_to.window(hyperskill_tab)
hyperskill_title = driver.title
print(hyperskill_title)

driver.switch_to.window(onliner_tab)
onliner_title = driver.title
print(onliner_title)

driver.switch_to.window(ozon_tab)
wait.until(EC.url_to_be("https://www.ozon.ru/?__rr=1&abt_att=1"), "url is not correct")
ozon_title = driver.title
print(ozon_title)

driver.switch_to.window(hyperskill_tab)
wait.until(EC.element_to_be_clickable(HYPERSKILL_PRICING_BUTTON_LOCATOR), "Element is not clickable").click()

driver.switch_to.window(onliner_tab)
wait.until(EC.element_to_be_clickable(ONLINER_FORUM_BUTTON_LOCATOR), "Element is not clickable").click()

driver.switch_to.window(ozon_tab)
wait.until(EC.element_to_be_clickable(OZON_CATALOG_BUTTON_LOCATOR), "Element is not clickable").click()

driver.quit()
