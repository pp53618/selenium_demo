import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import random


def test_create_account_failed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, "reg_email").send_keys("testeroprogramowaniapython@gmail.com")
    driver.find_element(By.ID, "reg_password").send_keys("testeroprogramowaniapython")
    driver.find_element(By.NAME, "register").click()
    msg = 'An account is already registered with your email address. Please log in.'

    assert msg in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text


def test_create_account_passed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    wait = WebDriverWait(driver, 10)
    email = str(random.randint(0, 1000000)) + "testeroprogramowaniapython@gmail.com"
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.find_element(By.ID, "reg_password").send_keys("testeroprogramowaniapython")
    driver.find_element(By.NAME, "register").click()

    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    time.sleep(5)