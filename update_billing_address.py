import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import random


def test_update_billing_address():
    email = str(random.randint(0, 1000000)) + "testeroprogramowaniapython@gmail.com"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("testeroprogramowaniapython")
    driver.find_element(By.NAME, "register").click()
    driver.find_element(By.LINK_TEXT, "Addresses").click()
    driver.find_element(By.LINK_TEXT, "Edit").click()
    driver.find_element(By.ID, "billing_first_name").send_keys("John")
    driver.find_element(By.ID, "billing_last_name").send_keys("Doe")
    Select(driver.find_element(By.ID, "billing_country")).select_by_visible_text("Poland")
    driver.find_element(By.ID, "billing_address_1").send_keys("Kwiatowa 1")
    driver.find_element(By.ID, "billing_postcode").send_keys("00-001")
    driver.find_element(By.ID, "billing_city").send_keys("Warsaw")
    driver.find_element(By.ID, "billing_phone").send_keys("111111111")
    driver.find_element(By.XPATH, "//button[@value='Save address']").click()

    assert 'Address changed successfully' in driver.find_element(By.XPATH, "//div[@class='woocommerce-message']").text

    time.sleep(5)