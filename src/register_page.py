import datetime
import random

import allure
from selenium.webdriver.common.by import By

from src.base_func import BasePage


class RegisterPage(BasePage):
    REGISTER_TITLE = (By.CSS_SELECTOR, 'h1')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input.btn')
    FIRSTNAME_INPUT = (By.ID, 'input-firstname')
    LASTNAME_INPUT = (By.ID, 'input-lastname')
    EMAIL_INPUT = (By.ID, 'input-email')
    TEL_INPUT = (By.ID, 'input-telephone')
    PASS_INPUT = (By.ID, 'input-password')
    CONFIRM_PASS_INPUT = (By.ID, 'input-confirm')

    MENU = (By.CSS_SELECTOR, '[title="My Account"]')
    REGISTER = (By.PARTIAL_LINK_TEXT, 'Register')
    POLICY_CHECKBOX = (By.CSS_SELECTOR, "[name='agree']")
    SUBMIT = (By.CSS_SELECTOR, '[type="submit"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'h1')

    @allure.step('Switch to the registration page')
    def switch_to_register_page(self):
        """Switch to registration page"""
        with allure.step('Click menu button'):
            menu = RegisterPage.find_element_by(self, RegisterPage.MENU)
            menu.click()

        with allure.step('Click button for registration'):
            register = RegisterPage.find_element_by(self, RegisterPage.REGISTER)
            register.click()

        register_page = self.browser.current_url
        self.browser.get(register_page)
        self.logger.info('Switched to registration page')

        return self.browser

    @allure.step('Registration of a new user')
    def register_new_user(self, first_name, last_name, tel, password):
        """Registration of a new user"""
        test_data = random.randint(1, 100)
        with allure.step('Enter first name data'):
            first_name_input = RegisterPage.find_element_by(self, RegisterPage.FIRSTNAME_INPUT)
            first_name_input.send_keys(f'{first_name}{test_data}')

        with allure.step('Enter last name data'):
            last_name_input = RegisterPage.find_element_by(self, RegisterPage.LASTNAME_INPUT)
            last_name_input.send_keys(last_name)

        with allure.step('Enter email data'):
            email_input = RegisterPage.find_element_by(self, RegisterPage.EMAIL_INPUT)
            email_input.send_keys(f'{self.browser.session_id}{test_data}@mail.ru')

        with allure.step('Enter telephone data'):
            telephone_input = RegisterPage.find_element_by(self, RegisterPage.TEL_INPUT)
            telephone_input.send_keys(tel)

        with allure.step('Enter password'):
            password_input = RegisterPage.find_element_by(self, RegisterPage.PASS_INPUT)
            password_input.send_keys(password)

        with allure.step('Confirm password'):
            confirm_password_input = RegisterPage.find_element_by(self, RegisterPage.CONFIRM_PASS_INPUT)
            confirm_password_input.send_keys(password)

        with allure.step('Mark policy as agreed'):
            policy_agree = RegisterPage.find_element_by(self, RegisterPage.POLICY_CHECKBOX)
            policy_agree.click()

        with allure.step('Click continue button'):
            continue_button = RegisterPage.find_element_by(self, RegisterPage.SUBMIT)
            continue_button.click()

            success_page = self.browser.current_url
            self.browser.get(success_page)
            self.logger.info(
                'New user {} {} is registered at {}'.format(first_name, last_name, datetime.datetime.now()))

            return self.browser
