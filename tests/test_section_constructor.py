import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import StellaburgerLocators
class TestStellaburgerConsructor:

    def test_link_to_fillings(self, driver):
        section_fillings = driver.find_element(*StellaburgerLocators.SECTION_FILLINGS)
        section_fillings.click()

        assert driver.find_element(*StellaburgerLocators.SECTION_ACTIVE).text == 'Начинки'

    def test_link_to_sauces(self, driver):
        section_sauces = driver.find_element(*StellaburgerLocators.SECTION_SAUCES)
        section_sauces.click()

        assert driver.find_element(*StellaburgerLocators.SECTION_ACTIVE).text == 'Соусы'


    def test_link_to_buns(self, driver):
        # первый вариант теста для проверки перехода к разделу Булок, так как этот раздел по умолчанию открыт
        driver.find_element(*StellaburgerLocators.SECTION_BUNS)

        assert driver.find_element(*StellaburgerLocators.SECTION_ACTIVE).text == 'Булки'

    def test_link_fillings_to_buns(self, driver):
        # второй вариант теста для проверки перехода к разделу Булок с предварительным переходом в др. раздел, чтобы подтвердить переход из раздела в раздел кликом
        section_fillings = driver.find_element(*StellaburgerLocators.SECTION_FILLINGS)
        section_fillings.click()
        section_buns = driver.find_element(*StellaburgerLocators.SECTION_BUNS)
        section_buns.click()

        assert driver.find_element(*StellaburgerLocators.SECTION_ACTIVE).text == 'Булки'







