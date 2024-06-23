import time
from selenium import webdriver
from lesson_13_table_handler import TableHandler


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

table = TableHandler(driver)

driver.get("https://editor.datatables.net/examples/extensions/responsive.html")

table.get_content_by_name("Timothy Mooney")

