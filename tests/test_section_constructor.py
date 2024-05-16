import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellaburgerLocators
class TestStellaburgerConsructor:
    def test_link_to_sauces(self, driver):
        section_sauces = driver.find_element(*StellaburgerLocators.SECTION_SAUCES)
        section_sauces.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.ITEM_SAUCE)))

        driver.quit()

    def test_link_to_fillings(self, driver):
        section_fillings = driver.find_element(*StellaburgerLocators.SECTION_FILLINGS)
        section_fillings.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.ITEM_FILLING)))

        driver.quit()


    def test_link_fillings_to_buns(self, driver):
        section_fillings = driver.find_element(*StellaburgerLocators.SECTION_FILLINGS)
        section_fillings.click()
        section_buns = driver.find_element(*StellaburgerLocators.SECTION_BUNS)
        section_buns.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellaburgerLocators.ITEM_BUN)))

        driver.quit()