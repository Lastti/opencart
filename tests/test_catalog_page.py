from src.base_func import visibility_of_element
from src.catalog_page import CatalogPageLocators


def test_catalog_page(browser):
    browser.get(browser.url + '/desktops')

    visibility_of_element(browser, CatalogPageLocators.CATALOG_SUBTITLE)
    visibility_of_element(browser, CatalogPageLocators.ACTIVE_ITEMS_LIST)
    visibility_of_element(browser, CatalogPageLocators.COMPARE_BUTTON)
    visibility_of_element(browser, CatalogPageLocators.INPUT_LIMIT)
    visibility_of_element(browser, CatalogPageLocators.INPUT_SORT)
