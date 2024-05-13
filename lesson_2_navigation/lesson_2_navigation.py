import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

# 1
WIKI_ICON = driver.find_element(By.CLASS_NAME, "wikipedia-icon")
WIKI_INPUT = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
WIKI_SEARCH_BUTTON = driver.find_element(By.CSS_SELECTOR, ".wikipedia-search-button")
TITLE = driver.find_element(By.TAG_NAME, "h1")