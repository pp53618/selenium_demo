import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import random
import pytest
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("testeroprogramowaniapython@gmail.com", "testeroprogramowaniapython")

        msg = 'An account is already registered with your email address. Please log in.'
        assert msg in my_account_page.get_error_msg()

        time.sleep(5)

    def test_create_account_passed(self):
        my_account_page = MyAccountPage(self.driver)
        email = str(random.randint(0, 1000000)) + "testeroprogramowaniapython@gmail.com"
        my_account_page.open_page()
        my_account_page.create_account(email, "testeroprogramowaniapython")

        assert my_account_page.is_logout_link_displayed()

        time.sleep(5)