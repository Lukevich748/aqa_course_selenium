from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver=driver, timeout=15, poll_frequency=1)

GRID_TAB_BUTTON_LOCATOR = ("xpath", "//nav[@role='tablist']/a[@id='demo-tab-grid']")

get_grid_item_locator = lambda item_name: ("xpath", f"//div[@class='tab-content']//li[text()='{item_name}']")

driver.get("https://demoqa.com/selectable")

wait.until(EC.element_to_be_clickable(GRID_TAB_BUTTON_LOCATOR), "Tab is not clickable").click()

one_item_checkbox = wait.until(EC.element_to_be_clickable(get_grid_item_locator("One")), "Item is not clickable")
five_item_checkbox = wait.until(EC.element_to_be_clickable(get_grid_item_locator("Five")), "Item is not clickable")
nine_item_checkbox = wait.until(EC.element_to_be_clickable(get_grid_item_locator("Nine")), "Item is not clickable")

selected_items = [one_item_checkbox, five_item_checkbox, nine_item_checkbox]
for item in selected_items:
    item.click()
    assert "active" in item.get_attribute("class"), f"'{item.text}' Checkbox is not active"

for item in selected_items:
    item.click()
    assert "active" not in item.get_attribute("class"), f"'{item.text}' Checkbox is active"

driver.quit()