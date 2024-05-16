import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaburgerLocators
class TestStellaburgerLogout:
    def test_logout_true(self, driver):
        login_account_button = driver.find_element(*StellaburgerLocators.LOGIN_ACCOUNT_BUTTON)
        login_account_button.click()
        email_field_login = driver.find_element(*StellaburgerLocators.EMAIL_FIELD_LOGIN)
        email_field_login.send_keys('m89067536142@yandex.ru')
        password_field_login = driver.find_element(*StellaburgerLocators.PASSWORD_FIELD_LOGIN)
        password_field_login.send_keys('123456')
        login_button = driver.find_element(*StellaburgerLocators.LOGIN_BUTTON)
        login_button.click()
        login_account_button = driver.find_element(*StellaburgerLocators.LOGIN_ACCOUNT_BUTTON)
        login_account_button.click()
        logout_button = driver.find_element(*StellaburgerLocators.LOGOUT_BUTTON)
        logout_button.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.LOGIN_BUTTON)))

        driver.quit()
