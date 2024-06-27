from selenium import webdriver
from lesson_13_table_handler import TableHandler


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

table = TableHandler(driver)

driver.get("https://editor.datatables.net/examples/extensions/responsive.html")

# table.get_content_by_name("Timothy Mooney")
# print(table.search_content("New York"))
# print(table.add_content("Artem", "Lukevich", "AQA"))
# print(table.edit_content("Caesar Vance", "Artem", "Lukevich", "AQA", 9000))
# print(table.delete_content("Caesar Vance"))
