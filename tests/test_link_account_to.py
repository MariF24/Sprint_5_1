import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaburgerLocators
class TestStellaburgerLinkAccountTo:

    def test_link_account_button(self, driver):
        login_account_button = driver.find_element(*StellaburgerLocators.LOGIN_ACCOUNT_BUTTON)
        login_account_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.LOGIN_BUTTON)))
        assert driver.find_element(*StellaburgerLocators.LOGIN_BUTTON).is_displayed()

    def test_link_account_button_to_constructor_button(self, driver):
        login_account_button = driver.find_element(*StellaburgerLocators.LOGIN_ACCOUNT_BUTTON)
        login_account_button.click()
        constructor_button = driver.find_element(*StellaburgerLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.LOGIN_ACCOUNT_BUTTON)))
        assert driver.find_element(*StellaburgerLocators.LOGIN_ACCOUNT_BUTTON).is_displayed()



    def test_link_account_to_constructor_to_logo(self, driver):
        login_account_button = driver.find_element(*StellaburgerLocators.LOGIN_ACCOUNT_BUTTON)
        login_account_button.click()
        constructor_button = driver.find_element(*StellaburgerLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.LOGIN_ACCOUNT_BUTTON)))
        logo_field = driver.find_element(*StellaburgerLocators.LOGO_FIELD)
        logo_field.click()

        assert driver.find_element(*StellaburgerLocators.LOGIN_ACCOUNT_BUTTON).is_displayed()

