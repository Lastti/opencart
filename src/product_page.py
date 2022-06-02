from selenium.webdriver.common.by import By

from src.base_func import BasePage


class ProductPage(BasePage):
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'li>h2')
    ADD_TO_CART_BUTTON = (By.ID, 'button-cart')
    DESCRIPTION = (By.LINK_TEXT, 'Description')
    SPECIFICATION = (By.LINK_TEXT, 'Specification')
    REVIEWS = (By.LINK_TEXT, 'Reviews (0)')
