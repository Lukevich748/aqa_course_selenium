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
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

driver.get("https://hyperskill.org/login")
hyperskill_tab = driver.current_window_handle

driver.switch_to.new_window("tab")
driver.get("https://www.onliner.by")
onliner_tab = driver.current_window_handle

driver.switch_to.new_window("tab")
driver.get("https://www.ozon.ru")
ozon_tab = driver.current_window_handle



time.sleep(3)

driver.quit()