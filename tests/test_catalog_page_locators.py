from src.catalog_page import CatalogPage
from src.test_data import TestData


def test_catalog_page_locators(browser):
    browser.get(browser.url + TestData.PRODUCT_GROUP)
    page = CatalogPage(browser)

    page.visibility_of_element(CatalogPage.CATALOG_SUBTITLE)
    page.visibility_of_element(CatalogPage.ACTIVE_ITEMS_LIST)
    page.visibility_of_element(CatalogPage.COMPARE_BUTTON)
    page.visibility_of_element(CatalogPage.INPUT_LIMIT)
    page.visibility_of_element(CatalogPage.INPUT_SORT)
