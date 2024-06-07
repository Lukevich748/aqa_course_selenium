import random

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

GRID_TAB_BUTTON_LOCATOR = ("xpath", "//nav[@role='tablist']/a[@id='demo-tab-grid']")
GRID_ITEMS_LIST_LOCATOR = ("xpath", "//div[@id='gridContainer']//li")

driver.get("https://demoqa.com/selectable")

driver.find_element(*GRID_TAB_BUTTON_LOCATOR).click()


def random_item_status_check(count: int):
    """
    Выбирает случайные элементы из списка сетки и проверяет их состояние.

    :param count: Количество элементов из сетки для проверки их состояния.
    """
    grid_items_list = driver.find_elements(*GRID_ITEMS_LIST_LOCATOR)
    if count == 0:
        count = 1
    elif count > len(grid_items_list):
        count = len(grid_items_list)

    random_grid_items = random.sample(grid_items_list, count)
    for item in random_grid_items:
        item.click()
        assert "active" in item.get_attribute("class")
        item.click()
        assert "active" not in item.get_attribute("class")


random_item_status_check(6)

driver.quit()