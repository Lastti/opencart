import allure
from selenium.webdriver.common.by import By

from src.base_func import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.NAME, 'search')
    ITEM_IN_BASKET = (By.ID, 'cart-total')
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-inverse')
    CURRENCY_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-link.dropdown-toggle')
    ACTUAL_CURRENCY = (By.CSS_SELECTOR, 'strong')
    MENU = (By.CSS_SELECTOR, '.navbar-collapse')
    PRODUCT = (By.CSS_SELECTOR, '.product-layout')

    @allure.step('Switching to another currency')
    def switch_currency_to(self, new_currency):
        """Switch to another currency from current"""
        with allure.step('Click currency menu button'):
            currency_menu = MainPage.find_element_by(self, MainPage.CURRENCY_BUTTON)
            currency_menu.click()

        new_currency_loc = (By.NAME, new_currency)
        with allure.step('Click desirable currency button'):
            desirable_currency = MainPage.find_element_by(self, new_currency_loc)
            desirable_currency.click()

        with allure.step('Find actual currency'):
            actual_currency = MainPage.find_element_by(self, MainPage.ACTUAL_CURRENCY)
        self.logger.info('Successfully switched to {} currency'.format(new_currency))
        return actual_currency
