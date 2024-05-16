import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import StellaburgerLocators
class TestStellaburgerLinkAccountTo:

    def test_link_account_button_to_constructor_button(self, driver):
        login_account_button = driver.find_element(*StellaburgerLocators.LOGIN_ACCOUNT_BUTTON)
        login_account_button.click()

        constructor_button = driver.find_element(*StellaburgerLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        driver.quit()



    def test_link_account_to_constructor_to_logo(self, driver):
        login_account_button = driver.find_element(*StellaburgerLocators.LOGIN_ACCOUNT_BUTTON)
        login_account_button.click()

        constructor_button = driver.find_element(*StellaburgerLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        logo_field = driver.find_element(*StellaburgerLocators.LOGO_FIELD)
        logo_field.click()


        driver.quit()