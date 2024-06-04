import pickle
import os
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver=driver, timeout=10, poll_frequency=1)

# Cart
CART_BUTTON_LOCATOR = ("xpath", "//div[@id='userbar']//a[@title='Корзина']")
ADD_TO_CART_BUTTON_LOCATOR = ("xpath", "//div[contains(@class, 'item_primary')]//a[text()='В корзину']")
ITEM_IN_CART_BUTTON = ("xpath", "//div[contains(@class, 'item_primary')]//a[text()='В корзине']")

# Items
LG_ULTRA_GEAR_MONITOR_CARD_LOCATOR = ("xpath", "//div[@class='catalog-offers']//div[@data-item-id='24gn60rb']")
YANDEX_MINI_CARD_LOCATOR = ("xpath", "//div[@class='catalog-offers']//div[@data-item-id='yandstmini2blk']")


driver.get("https://www.onliner.by")

wait.until(EC.visibility_of_element_located(LG_ULTRA_GEAR_MONITOR_CARD_LOCATOR)).click()
wait.until(EC.visibility_of_element_located(ADD_TO_CART_BUTTON_LOCATOR)).click()
wait.until(EC.visibility_of_element_located(ITEM_IN_CART_BUTTON))
driver.back()

wait.until(EC.visibility_of_element_located(YANDEX_MINI_CARD_LOCATOR)).click()
wait.until(EC.visibility_of_element_located(ADD_TO_CART_BUTTON_LOCATOR)).click()
wait.until(EC.visibility_of_element_located(ITEM_IN_CART_BUTTON))

wait.until(EC.visibility_of_element_located(CART_BUTTON_LOCATOR)).click()

pickle.dump(driver.get_cookies(), open(os.path.join(os.getcwd(), "cookies", "cookies.pkl"), "wb"))
driver.delete_all_cookies()
driver.refresh()

cookies = pickle.load(open(os.path.join(os.getcwd(), "cookies", "cookies.pkl"), "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()

driver.quit()