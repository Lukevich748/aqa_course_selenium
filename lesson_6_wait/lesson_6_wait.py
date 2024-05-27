from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

CHANGE_TEXT_TO_SELENIUM_WEBDRIVER_BUTTON = ("xpath", "//button[@id='populate-text']")
TEXT_TO_CHANGE = ("xpath", "//h2[@id='h2']")

DISPLAY_BUTTON_AFTER_10_SECONDS_BUTTON = ("xpath", "//button[@id='display-other-button']")
ENABLED_BUTTON = ("xpath", "//button[@id='hidden']")

ENABLE_BUTTON_AFTER_10_SECONDS_BUTTON = ("xpath", "//button[@id='enable-button']")
DISABLE_BUTTON = ("xpath", "//button[@id='disable']")

OPEN_AN_ALERT_AFTER_5_SECONDS_BUTTON = ("xpath", "//button[@id='alert']")

driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

wait.until(EC.text_to_be_present_in_element(TEXT_TO_CHANGE, "site"))
change_text_to_selenium_webdriver_button = driver.find_element(*CHANGE_TEXT_TO_SELENIUM_WEBDRIVER_BUTTON)
change_text_to_selenium_webdriver_button.click()
wait.until(EC.text_to_be_present_in_element(TEXT_TO_CHANGE, "Selenium Webdriver"))

display_button_after_10_seconds_button = driver.find_element(*DISPLAY_BUTTON_AFTER_10_SECONDS_BUTTON)
display_button_after_10_seconds_button.click()
wait.until(EC.visibility_of_element_located(ENABLED_BUTTON))

enable_button_after_10_seconds_button = driver.find_element(*ENABLE_BUTTON_AFTER_10_SECONDS_BUTTON)
enable_button_after_10_seconds_button.click()
wait.until(EC.element_to_be_clickable(DISABLE_BUTTON))

open_an_alert_after_5_seconds_button = driver.find_element(*OPEN_AN_ALERT_AFTER_5_SECONDS_BUTTON)
open_an_alert_after_5_seconds_button.click()
wait.until(EC.alert_is_present())