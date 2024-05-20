import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaburgerLocators
from data import get_registration_data
class TestStellaburgerRegistration:

    def test_correct_registration_account(self, driver):
        name, email = get_registration_data()
        account_button = driver.find_element(*StellaburgerLocators.ACCOUNT_BUTTON)
        account_button.click()
        registration_link = driver.find_element(*StellaburgerLocators.REGISTRATION_LINK)
        registration_link.click()
        name_field = driver.find_element(*StellaburgerLocators.NAME_FIELD)
        name_field.send_keys(name)
        email_field = driver.find_element(*StellaburgerLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = driver.find_element(*StellaburgerLocators.PASSWORD_FIELD)
        password_field.send_keys('123456')
        registration_button = driver.find_element(*StellaburgerLocators.REGISTRATION_BUTTON)
        registration_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.LOGIN_BUTTON)))

        assert driver.find_element(*StellaburgerLocators.LOGIN_BUTTON).is_displayed()

    def test_incorrect_password_registration_account(self, driver):
        name, email = get_registration_data()
        account_button = driver.find_element(*StellaburgerLocators.ACCOUNT_BUTTON)
        account_button.click()
        registration_link = driver.find_element(*StellaburgerLocators.REGISTRATION_LINK)
        registration_link.click()
        name_field = driver.find_element(*StellaburgerLocators.NAME_FIELD)
        name_field.send_keys(name)
        email_field = driver.find_element(*StellaburgerLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = driver.find_element(*StellaburgerLocators.PASSWORD_FIELD)
        password_field.send_keys('12345')
        registration_button = driver.find_element(*StellaburgerLocators.REGISTRATION_BUTTON)
        registration_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.INCORRECT_PASSWORD_FIELD)))

        assert driver.find_element(*StellaburgerLocators.INCORRECT_PASSWORD_FIELD).is_displayed()

