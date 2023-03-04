import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestLogIn:


    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("testeroprogramowaniapython@gmail.com", "testeroprogramowaniapython123")

        assert "ERROR: Incorrect username or password." in my_account_page.get_error_msg()

    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("testeroprogramowaniapython@gmail.com", "testeroprogramowaniapython")

        assert my_account_page.is_logout_link_displayed()

        time.sleep(5)