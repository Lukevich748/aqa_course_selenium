import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
preferences = {
    "download.default_directory": os.path.join(os.getcwd(), "downloads"),
}
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(options=options)

# 1
driver.get("https://demoqa.com/upload-download")

UPLOAD_FILE_FIELD = ("xpath", "//input[@id='uploadFile']")

upload_file_field = driver.find_element(*UPLOAD_FILE_FIELD)
upload_file_field.send_keys(os.path.join(os.getcwd(), "upload_file.jpg"))

# 2
driver.get("https://the-internet.herokuapp.com/download")

DOWNLOADS_LINKS_LIST = ("xpath", "//div[@class='example']/a")

downloads_links_list = driver.find_elements(*DOWNLOADS_LINKS_LIST)
for link in downloads_links_list:
    link.click()