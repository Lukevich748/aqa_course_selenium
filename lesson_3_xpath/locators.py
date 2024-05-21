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
PYTHON_CORE_CARD_CERTIFICATE_LABEL = ("xpath", "//a[@aria-label='Python Core']//span[text()=' Certificate ']")
PYTHON_CORE_CARD_RATING = ("xpath", "//a[@aria-label='Python Core']//div[@class='d-flex align-items-center gap-2']")
PYTHON_CORE_CARD_TEXT = ("xpath", "//a[@aria-label='Python Core']//span[@class='flex-1 track-description']")
PYTHON_CORE_CARD_STUDENTS_AMOUNT = ("xpath", "//a[@aria-label='Python Core']//DIV[@class='font-size-sm ml-auto']")
INTRODUCTION_TO_PYTHON_CARD = ("xpath", "//a[@aria-label='Introduction to Python']")

# Footer
TOP_TRACKS_BUTTON = ("xpath", "//a[text()='Top tracks']")
BEGINNER_FRIENDLY_BUTTON = ("xpath", "//a[@click-event-target='Beginner-friendly']")
HYPERSKILL_ON_REDDIT_BUTTON = ("xpath", "//a[@click-event-target='Reddit']")
HYPERSKILL_ON_FACEBOOK_BUTTON = ("xpath", "//a[@click-event-target='Facebook']")
FULL_CATALOG_BUTTON = ("xpath", "(//a[@click-event-target='full_catalog'])[2]")
GOOGLE_PLAY_BUTTON = ("xpath", "//a[@click-event-target='google-play']")
APP_STORE_BUTTON = ("xpath", "//a[@click-event-target='app-store']")

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

driver.find_element(*PYTHON_CORE_CARD)
driver.find_element(*PYTHON_CORE_CARD_CERTIFICATE_LABEL)
driver.find_element(*PYTHON_CORE_CARD_RATING)
driver.find_element(*PYTHON_CORE_CARD_TEXT)
driver.find_element(*PYTHON_CORE_CARD_STUDENTS_AMOUNT)
driver.find_element(*INTRODUCTION_TO_PYTHON_CARD)
driver.find_element(*TOP_TRACKS_BUTTON)
driver.find_element(*BEGINNER_FRIENDLY_BUTTON)
driver.find_element(*HYPERSKILL_ON_REDDIT_BUTTON)
driver.find_element(*HYPERSKILL_ON_FACEBOOK_BUTTON)
driver.find_element(*FULL_CATALOG_BUTTON)
driver.find_element(*GOOGLE_PLAY_BUTTON)
driver.find_element(*APP_STORE_BUTTON)

time.sleep(2)
categories_buttons_list = driver.find_elements(*CATEGORIES_BUTTONS_LIST)
for category in categories_buttons_list:
    category.click()