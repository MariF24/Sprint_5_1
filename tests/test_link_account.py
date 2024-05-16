import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import StellaburgerLocators
class TestStellaburgerLinkAccount:

    def test_link_account_button(self, driver):
        login_account_button = driver.find_element(*StellaburgerLocators.LOGIN_ACCOUNT_BUTTON)
        login_account_button.click()

        driver.quit()
