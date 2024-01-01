import time
from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def openBrowser():
    driver = webdriver.Chrome()
    return driver

def go_to_homepage(homepage):
    driver.get('http://demostore.supersqa.com/')
    driver.maximize_window()

def add_first_item_to_cart(item):
     find_item = driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[2]/main[1]/ul[1]/li[4]/a[2]")
     find_item.click()


def go_to_cart_page(driver):
    driver.get('http://demostore.supersqa.com/cart')


def coupon_code(driver, coupon):
    coupon_field = driver.find_element(By.XPATH, "//input[@id='coupon_code']")
    coupon_field.send_keys(coupon)
    apply_coupon = driver.find_element(By.XPATH, "//button[contains(text(),'Apply coupon')]")
    apply_coupon.click()

if __name__ == '__main__':
    driver = openBrowser()
    go_to_homepage(driver)
    add_first_item_to_cart(driver)
    go_to_cart_page(driver)
    coupon_code(driver, 'fakelove')
    time.sleep(3)

