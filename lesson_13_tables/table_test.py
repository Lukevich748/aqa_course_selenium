from selenium import webdriver
from lesson_13_table_handler import TableHandler


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

table = TableHandler(driver)

driver.get("https://editor.datatables.net/examples/extensions/responsive.html")

# table.get_content_by_name("Timothy Mooney")

# print(table.search_content("New York"))

# print(table.add_content(
#     first_name="Artem",
#     last_name="Lukevich",
#     position="AQA",
#     office="Warsaw",
#     extn=1488,
#     start_date="2024-06-27",
#     salary=5325))

# print(table.edit_content(
#     search_name="Caesar Vance",
#     new_first_name="Artem",
#     new_last_name="Lukevich",
#     position="AQA",
#     office="Warsaw",
#     extn=1488,
#     start_date="2024-06-27",
#     salary=5325))

# print(table.delete_content("Caesar Vance"))
