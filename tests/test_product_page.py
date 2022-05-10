from src.base_func import visibility_of_element
from src.product_page import ProductPageLocators


def test_product_page(browser):
    browser.get(browser.url + '/macbook')

    visibility_of_element(browser, ProductPageLocators.PRODUCT_TITLE)
    visibility_of_element(browser, ProductPageLocators.PRODUCT_PRICE)
    visibility_of_element(browser, ProductPageLocators.ADD_TO_CART_BUTTON)
    visibility_of_element(browser, ProductPageLocators.DESCRIPTION)
    visibility_of_element(browser, ProductPageLocators.SPECIFICATION)
    visibility_of_element(browser, ProductPageLocators.REVIEWS)
