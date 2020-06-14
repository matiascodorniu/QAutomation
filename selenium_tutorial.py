
from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.python.org/")
time.sleep(3)

enter_searchbar = driver.find_element_by_id("id-search-field")
enter_searchbar.send_keys("loops")

click_button = driver.find_element_by_id("submit")
click_button.click()

time.sleep(100)
driver.close()








