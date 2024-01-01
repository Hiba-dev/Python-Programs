import time
from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.python.org/')
time.sleep(5)
driver.maximize_window()

search_field_id = "id-search-field"
search_ele = driver.find_element(By.ID, search_field_id)
search_ele.send_keys("testing")

go_button_id = "submit"
go_button_ele = driver.find_element(By.ID, go_button_id)
go_button_ele.click()

time.sleep(3)

