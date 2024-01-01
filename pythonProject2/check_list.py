import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://manujaggarwal.com/"
driver = webdriver.Edge()


driver.get("https://gtmetrix.com/")
driver.maximize_window()
search_ele = "js-analyze-form-url"
driver.find_element(By.CLASS_NAME, search_ele).send_keys(url)
time.sleep(5)
button = "analyze-form-button"
driver.find_element(By.CLASS_NAME, button).click()
time.sleep(8)
driver.save_screenshot("GT_Metrix.png")

current_window = driver.current_window_handle

# Open a new tab using JavaScript
driver.execute_script("window.open('', '_blank');")

# Switch to a new tab
driver.switch_to.window(driver.window_handles[1])


# Navigate in the new tab
driver.get("https://pagespeed.web.dev/")

driver.find_element(By.CLASS_NAME, "VfPpkd-fmcmS-wGMbrd ").send_keys(url)
driver.find_element(By.XPATH, "//span[contains(text(),'Analyze')]").click()
time.sleep(50)
driver.save_screenshot("page_speed.png")

# Open a new tab using JavaScript
driver.execute_script("window.open('', '_blank');")

driver.switch_to.window(driver.window_handles[2])

# Navigate in the new tab
driver.get("https://www.deadlinkchecker.com/")

text_field = driver.find_element(By.XPATH, "//input[@id='url']")
text_field.clear()
driver.find_element(By.XPATH, "//input[@id='url']").send_keys(url)
driver.find_element(By.XPATH, "//button[contains(text(),'check')]").click()

time.sleep(40)

# Open a new tab using Javascript

driver.execute_script("window.open('', '_blank');")

driver.switch_to.window(driver.window_handles[3])

# Navigate in the new tab
driver.get("https://www.ssllabs.com/ssltest/")

driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]/input[1]").send_keys(url)
driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/input[1]").click()

time.sleep(50)

driver.save_screenshot("SSL_Report.png")

driver.quit()


