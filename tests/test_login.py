import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaburgerLocators
from data import EMAIL_DEFAULT, PASSWORD_DEFAULT
class TestStellaburgerLogin:

    def test_login_account_button_main(self, driver):
        login_account_button = driver.find_element(*StellaburgerLocators.LOGIN_ACCOUNT_BUTTON)
        login_account_button.click()
        email_field = driver.find_element(*StellaburgerLocators.EMAIL_FIELD)
        email_field.send_keys(EMAIL_DEFAULT)
        password_field = driver.find_element(*StellaburgerLocators.PASSWORD_FIELD)
        password_field.send_keys(PASSWORD_DEFAULT)
        login_button = driver.find_element(*StellaburgerLocators.LOGIN_BUTTON)
        login_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.CHECKOUT_BUTTON)))

        assert driver.find_element(*StellaburgerLocators.CHECKOUT_BUTTON).is_displayed()


    def test_login_account_button(self, driver):
        account_button = driver.find_element(*StellaburgerLocators.ACCOUNT_BUTTON)
        account_button.click()
        email_field = driver.find_element(*StellaburgerLocators.EMAIL_FIELD)
        email_field.send_keys(EMAIL_DEFAULT)
        password_field = driver.find_element(*StellaburgerLocators.PASSWORD_FIELD)
        password_field.send_keys(PASSWORD_DEFAULT)
        login_button = driver.find_element(*StellaburgerLocators.LOGIN_BUTTON)
        login_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.CHECKOUT_BUTTON)))

        assert driver.find_element(*StellaburgerLocators.CHECKOUT_BUTTON).is_displayed()


    def test_login_registration_Link(self, driver):
        account_button = driver.find_element(*StellaburgerLocators.ACCOUNT_BUTTON)
        account_button.click()
        registration_link = driver.find_element(*StellaburgerLocators.REGISTRATION_LINK)
        registration_link.click()
        login_link = driver.find_element(*StellaburgerLocators.LOGIN_LINK)
        login_link.click()
        email_field = driver.find_element(*StellaburgerLocators.EMAIL_FIELD)
        email_field.send_keys(EMAIL_DEFAULT)
        password_field = driver.find_element(*StellaburgerLocators.PASSWORD_FIELD)
        password_field.send_keys(PASSWORD_DEFAULT)
        login_button = driver.find_element(*StellaburgerLocators.LOGIN_BUTTON)
        login_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.CHECKOUT_BUTTON)))

        assert driver.find_element(*StellaburgerLocators.CHECKOUT_BUTTON).is_displayed()

    def test_login_recovery_password_Link(self, driver):
        account_button = driver.find_element(*StellaburgerLocators.ACCOUNT_BUTTON)
        account_button.click()
        password_recovery_link = driver.find_element(*StellaburgerLocators.PASSWORD_RECOVERY_LINK)
        password_recovery_link.click()
        login_link = driver.find_element(*StellaburgerLocators.LOGIN_LINK)
        login_link.click()
        email_field = driver.find_element(*StellaburgerLocators.EMAIL_FIELD)
        email_field.send_keys(EMAIL_DEFAULT)
        password_field = driver.find_element(*StellaburgerLocators.PASSWORD_FIELD)
        password_field.send_keys(PASSWORD_DEFAULT)
        login_button = driver.find_element(*StellaburgerLocators.LOGIN_BUTTON)
        login_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.CHECKOUT_BUTTON)))

        assert driver.find_element(*StellaburgerLocators.CHECKOUT_BUTTON).is_displayed()
