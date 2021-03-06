from selenium.webdriver.common.by import By

from src.base_func import BasePage


class CatalogPage(BasePage):
    CATALOG_SUBTITLE = (By.LINK_TEXT, 'Desktops')
    INPUT_SORT = (By.CSS_SELECTOR, "[for='input-sort']")
    INPUT_LIMIT = (By.CSS_SELECTOR, "[for='input-limit']")
    COMPARE_BUTTON = (By.ID, 'compare-total')
    ACTIVE_ITEMS_LIST = (By.CSS_SELECTOR, '.list-group-item.active')
