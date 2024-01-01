from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl

# Load the Excel sheet
excel_file = 'C:\\Users\\DELL\\Downloads\\jake&jino.xlsx'
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook.active

# Initialize WebDriver
driver = webdriver.Edge()

# Loop through the URLs and check for 404 errors
for row in sheet.iter_rows(min_row=2, values_only=True):  # Assuming URLs start from row 2
    url = row[0]
    driver.get(url)

    # Check for 404 response
    if "404" in driver.page_source:
        print(f"URL: {url} - 404 Page Found")
    else:
        print(f"URL: {url} - OK")

# Close the WebDriver
driver.quit()