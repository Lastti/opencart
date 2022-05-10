from src.base_func import visibility_of_element
from src.main_page import MainPageLocators


def test_main_page(browser):
    browser.get(browser.url)

    visibility_of_element(browser, MainPageLocators.SEARCH_INPUT)
    visibility_of_element(browser, MainPageLocators.ITEM_IN_BASKET)
    visibility_of_element(browser, MainPageLocators.BASKET_BUTTON)
    visibility_of_element(browser, MainPageLocators.CURRENCY_BUTTON)
    visibility_of_element(browser, MainPageLocators.MENU)
    visibility_of_element(browser, MainPageLocators.PRODUCT)
