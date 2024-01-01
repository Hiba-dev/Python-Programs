from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace 'path/to/chromedriver', 'your_username', and 'your_password' with appropriate values
driver = webdriver.Chrome()
driver.get('https://launchpad.37signals.com/signin')

# Wait for the login form to be present and visible
try:
    login_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login_form"]')))
except TimeoutException:
    print("Login form not found or not visible. Exiting...")
    driver.quit()
    exit()

driver.find_element(By.ID, 'user_email').send_keys('your_username')
driver.find_element(By.ID, 'user_password').send_keys('your_password')
driver.find_element(By.NAME, 'commit').click()

# Wait for the login to complete and redirect to the homepage
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'bc-logo')))
except TimeoutException:
    print("Login not completed or redirected to the homepage. Exiting...")
    driver.quit()
    exit()

# Navigate to the todolists page
driver.get('https://basecamp.com/4/todolists')

# Wait for the todolists page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "todolist_item")]')))
except TimeoutException:
    print("Todolists page not found or not loaded. Exiting...")
    driver.quit()
    exit()