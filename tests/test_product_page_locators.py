from src.product_page import ProductPage
from src.test_data import TestData


def test_product_page_locators(browser):
    browser.get(browser.url + TestData.PRODUCT)
    page = ProductPage(browser)

    page.visibility_of_element(ProductPage.PRODUCT_TITLE)
    page.visibility_of_element(ProductPage.PRODUCT_PRICE)
    page.visibility_of_element(ProductPage.ADD_TO_CART_BUTTON)
    page.visibility_of_element(ProductPage.DESCRIPTION)
    page.visibility_of_element(ProductPage.REVIEWS)
