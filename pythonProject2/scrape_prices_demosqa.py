import time
from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'http://demostore.supersqa.com/'
driver.get(url)
driver.maximize_window()
time.sleep(5)

all_products = driver.find_elements(By.CLASS_NAME, 'product')
print(f"Number of Products: {len(all_products)}")

list_of_products_and_price = []
for product in all_products:
    product_price = product.find_element(By.CSS_SELECTOR, 'span.amount')
    price = product_price.text

    product_title = product.find_element(By.CSS_SELECTOR, 'h2.woocommerce-loop-product__title')
    name = product_title.text


    list_of_products_and_price.append({'name': name, 'price': price})

    print(list_of_products_and_price)