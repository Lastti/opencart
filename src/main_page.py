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

    def switch_currency_to(self, new_currency):
        """Switch to another currency from current"""
        currency_menu = self.browser.find_element(*MainPage.CURRENCY_BUTTON)
        currency_menu.click()
        desirable_currency = self.browser.find_element(By.NAME, new_currency)
        desirable_currency.click()
        actual_currency = self.browser.find_element(*MainPage.ACTUAL_CURRENCY)
        return actual_currency
