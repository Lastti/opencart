import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.base_func import BasePage


class AdminPage(BasePage):
    LOGIN_TITLE = (By.CLASS_NAME, 'panel-title')
    USERNAME_INPUT = (By.ID, 'input-username')
    PASSWORD_INPUT = (By.ID, 'input-password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
    CATALOG = (By.PARTIAL_LINK_TEXT, "Catalog")
    PRODUCTS = (By.PARTIAL_LINK_TEXT, "Products")
    ADD_ICON = (By.CSS_SELECTOR, "i.fa.fa-plus")
    PRODUCT_NAME = (By.ID, 'input-name1')
    PRODUCT_TAG = (By.ID, 'input-meta-title1')
    DATA_MENU = (By.CSS_SELECTOR, '[href="#tab-data')
    PRODUCT_MODEL = (By.ID, 'input-model')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
    FILTER_BY_NAME = (By.ID, 'input-name')
    FILTER_SUBMIT = (By.ID, 'button-filter')
    CHECKBOX_INPUT = (By.CSS_SELECTOR, '[type="checkbox"][value]')
    RESULT_MESSAGE = (By.CSS_SELECTOR, '[colspan="8"]')

    def login_with_creds(self, login, password):
        """Login of the user with credentials"""
        login_input = self.browser.find_element(*AdminPage.USERNAME_INPUT)
        login_input.send_keys(login)
        password_input = self.browser.find_element(*AdminPage.PASSWORD_INPUT)
        password_input.send_keys(password)
        submit = self.browser.find_element(*AdminPage.SUBMIT_BUTTON)
        submit.click()

        WebDriverWait(self.browser, 5).until_not(EC.visibility_of_element_located(AdminPage.SUBMIT_BUTTON))

        admin_page = self.browser.current_url
        self.browser.get(admin_page)
        return self.browser

    def switch_to_catalog(self):
        """Switch to catalog page"""
        catalog = self.browser.find_element(*AdminPage.CATALOG)
        catalog.click()

    def switch_to_products(self):
        """Switch to product in catalog"""
        products = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(AdminPage.PRODUCTS))
        products.click()

    def add_new_item(self):
        """Adding new product item by admin"""
        test_data = random.randint(1, 100)

        add_icon = self.browser.find_element(*AdminPage.ADD_ICON)
        add_icon.click()

        product_name = f'New item{test_data}'
        product_name_input = self.browser.find_element(*AdminPage.PRODUCT_NAME)
        product_name_input.send_keys(product_name)

        meta_tag_input = self.browser.find_element(*AdminPage.PRODUCT_TAG)
        meta_tag_input.send_keys('New item tag')

        switch_to_data = self.browser.find_element(*AdminPage.DATA_MENU)
        switch_to_data.click()

        model_input = self.browser.find_element(*AdminPage.PRODUCT_MODEL)
        model_input.send_keys('New item model')

        submit_button = self.browser.find_element(*AdminPage.SUBMIT_BUTTON)
        submit_button.click()
        return product_name

    def filter_by_name(self, product_name):
        """Filtration by name of a product item"""
        filter_by_name = self.browser.find_element(*AdminPage.FILTER_BY_NAME)
        filter_by_name.send_keys(product_name)
        submit_filter = self.browser.find_element(*AdminPage.FILTER_SUBMIT)
        submit_filter.click()

    def check_item_after_filter(self):
        """Choose product item from filtration results"""
        checkbox = self.browser.find_element(*AdminPage.CHECKBOX_INPUT)
        checkbox.click()

    def delete_item(self):
        """Delete a product item"""
        delete_button = self.browser.find_element(By.CSS_SELECTOR, 'button.btn-danger')
        delete_button.click()
        alert = self.browser.switch_to.alert
        alert.accept()
