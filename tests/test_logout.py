import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaburgerLocators
from data import EMAIL_DEFAULT, PASSWORD_DEFAULT
class TestStellaburgerLogout:
    def test_logout_true(self, driver):
        account_button = driver.find_element(*StellaburgerLocators.ACCOUNT_BUTTON)
        account_button.click()
        email_field = driver.find_element(*StellaburgerLocators.EMAIL_FIELD)
        email_field.send_keys(EMAIL_DEFAULT )
        password_field = driver.find_element(*StellaburgerLocators.PASSWORD_FIELD)
        password_field.send_keys(PASSWORD_DEFAULT)
        login_button = driver.find_element(*StellaburgerLocators.LOGIN_BUTTON)
        login_button.click()
        account_button = driver.find_element(*StellaburgerLocators.ACCOUNT_BUTTON)
        account_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.LOGOUT_BUTTON)))
        logout_button = driver.find_element(*StellaburgerLocators.LOGOUT_BUTTON)
        logout_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.LOGIN_BUTTON)))

        assert driver.find_element(*StellaburgerLocators.LOGIN_BUTTON).is_displayed()
