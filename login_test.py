import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_log_in_failed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("testeroprogramowaniapython@gmail.com")
    driver.find_element(By.ID, "password").send_keys("testeroprogramowaniapython123")
    driver.find_element(By.NAME, "login").click()

    assert "ERROR: Too many failed login attempts." in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text

def test_log_in_passed():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("testeroprogramowaniapython@gmail.com")
    driver.find_element(By.ID, "password").send_keys("testeroprogramowaniapython")
    driver.find_element(By.NAME, "login").click()

    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    time.sleep(5)