import datetime
import random

import allure
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
    DELETE_BUTTON = (By.CSS_SELECTOR, 'button.btn-danger')

    @allure.step('User authorization at the admin page')
    def login_with_creds(self, login, password):
        """Login of the user with credentials"""
        with allure.step('Enter login data'):
            login_input = AdminPage.find_element_by(self, AdminPage.USERNAME_INPUT)
            login_input.send_keys(login)

        with allure.step('Enter password data'):
            password_input = AdminPage.find_element_by(self, AdminPage.PASSWORD_INPUT)
            password_input.send_keys(password)

        with allure.step('Click submit button'):
            submit = AdminPage.find_element_by(self, AdminPage.SUBMIT_BUTTON)
            submit.click()

        WebDriverWait(self.browser, 5).until_not(EC.visibility_of_element_located(AdminPage.SUBMIT_BUTTON))

        admin_page = self.browser.current_url
        self.browser.get(admin_page)
        self.logger.info(
            'User authorization with login {}, password {} successful at {}'.format(login, password,
                                                                                    datetime.datetime.now()))
        return self.browser

    @allure.step('Switch to the catalog page')
    def switch_to_catalog(self):
        """Switch to catalog page"""
        catalog = AdminPage.find_element_by(self, AdminPage.CATALOG)
        catalog.click()
        self.logger.info('Switched to the catalog page')

    @allure.step('Switch to product in catalog')
    def switch_to_products(self):
        """Switch to product in catalog"""
        products = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(AdminPage.PRODUCTS))
        products.click()
        self.logger.info('Switched to product in catalog')

    @allure.step('Adding of a new item')
    def add_new_item(self):
        """Adding new product item by admin"""
        test_data = random.randint(1, 100)

        with allure.step('Click add icon button'):
            add_icon = AdminPage.find_element_by(self, AdminPage.ADD_ICON)
            add_icon.click()

        with allure.step('Enter product name data'):
            product_name = f'New item{test_data}'
            product_name_input = AdminPage.find_element_by(self, AdminPage.PRODUCT_NAME)
            product_name_input.send_keys(product_name)

        with allure.step('Enter meta tag data'):
            meta_tag_input = AdminPage.find_element_by(self, AdminPage.PRODUCT_TAG)
            meta_tag_input.send_keys('New item tag')

        with allure.step('Click to Data menu'):
            switch_to_data = AdminPage.find_element_by(self, AdminPage.DATA_MENU)
            switch_to_data.click()

        with allure.step('Enter item model data'):
            model_input = AdminPage.find_element_by(self, AdminPage.PRODUCT_MODEL)
            model_input.send_keys('New item model')

        with allure.step('Click submit button'):
            submit_button = AdminPage.find_element_by(self, AdminPage.SUBMIT_BUTTON)
            submit_button.click()

        self.logger.info('New product item: {} added at {}'.format(product_name, datetime.datetime.now()))
        return product_name

    @allure.step('Filtration by name of a product item')
    def filter_by_name(self, product_name):
        """Filtration by name of a product item"""
        with allure.step('Enter product name data into filter field'):
            filter_by_name = AdminPage.find_element_by(self, AdminPage.FILTER_BY_NAME)
            filter_by_name.send_keys(product_name)

        with allure.step('Click submit filtration button'):
            submit_filter = AdminPage.find_element_by(self, AdminPage.FILTER_SUBMIT)
            submit_filter.click()
        self.logger.info('Products filtered by product name: {}'.format(product_name))

    @allure.step('Choosing product item from filtration results"')
    def check_item_after_filter(self):
        """Choose product item from filtration results"""
        with allure.step('Click item checkbox'):
            checkbox = AdminPage.find_element_by(self, AdminPage.CHECKBOX_INPUT)
            checkbox.click()
        self.logger.info('Product item selected')

    @allure.step('Deleting of a product item')
    def delete_item(self):
        """Delete a product item"""
        with allure.step('Click delete button'):
            delete_button = AdminPage.find_element_by(self, AdminPage.DELETE_BUTTON)
            delete_button.click()

        alert = self.browser.switch_to.alert
        alert.accept()
        self.logger.info('Product item was deleted at {}'.format(datetime.datetime.now()))
