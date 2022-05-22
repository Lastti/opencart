from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_INPUT = (By.NAME, 'search')
    ITEM_IN_BASKET = (By.ID, 'cart-total')
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-inverse')
    CURRENCY_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-link.dropdown-toggle')
    MENU = (By.CSS_SELECTOR, '.navbar-collapse')
    PRODUCT = (By.CSS_SELECTOR, '.product-layout')
