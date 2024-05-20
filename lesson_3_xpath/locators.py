import time

from selenium import webdriver

# Header
HYPERSKILL_LOGO_BUTTON = ("xpath", "//a[div[@class='d-flex align-items-center']]")
PRICING_BUTTON = ("xpath", "(//li[a[@class='nav-link']])[2]")
FOR_BUSINESS_BUTTON = ("xpath", "(//li[a[@class='nav-link']])[3]")
SIGN_IN_BUTTON = ("xpath", "//button[contains(@class, 'btn btn-outline-light')]")
START_FOR_FREE_BUTTON = ("xpath", "//button[contains(@class, 'btn btn-primary btn-sm')]")

# Body
TITLE = ("xpath", "//h1")
CATEGORIES_BUTTONS_LIST = ("xpath", "//div[@class='categories mb-3']/a[contains(@class, 'active-route')]")

PYTHON_CORE_CARD = ("xpath", "//a[@aria-label='Python Core']")
PYTHON_CORE_CERTIFICATE_LABEL = ("xpath", "//a[@aria-label='Python Core']//span[text()=' Certificate ']")

INTRODUCTION_TO_PYTHON_CARD = ("xpath", "//a[@aria-label='Introduction to Python']")

driver = webdriver.Chrome()

driver.get("https://hyperskill.org/tracks")
time.sleep(2)
driver.find_element(*HYPERSKILL_LOGO_BUTTON)
driver.find_element(*PRICING_BUTTON)
driver.find_element(*FOR_BUSINESS_BUTTON)
driver.find_element(*SIGN_IN_BUTTON)
driver.find_element(*START_FOR_FREE_BUTTON)
driver.find_element(*TITLE)
driver.find_elements(*CATEGORIES_BUTTONS_LIST)

# time.sleep(2)
# categories_buttons_list = driver.find_elements(*CATEGORIES_BUTTONS_LIST)
# for category in categories_buttons_list:
#     category.click()

driver.find_element(*PYTHON_CORE_CARD)
driver.find_element(*INTRODUCTION_TO_PYTHON_CARD)