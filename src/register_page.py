import random

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

    def switch_to_register_page(self):
        """Switch to registration page"""
        menu = self.browser.find_element(*RegisterPage.MENU)
        menu.click()
        register = self.browser.find_element(*RegisterPage.REGISTER)
        register.click()
        register_page = self.browser.current_url
        self.browser.get(register_page)
        return self.browser

    def register_new_user(self, first_name, last_name, tel, password):
        """Registration of a new user"""
        test_data = random.randint(1, 100)

        first_name_input = self.browser.find_element(*RegisterPage.FIRSTNAME_INPUT)
        first_name_input.send_keys(f'{first_name}{test_data}')

        last_name_input = self.browser.find_element(*RegisterPage.LASTNAME_INPUT)
        last_name_input.send_keys(last_name)

        email_input = self.browser.find_element(*RegisterPage.EMAIL_INPUT)
        email_input.send_keys(f'{self.browser.session_id}{test_data}@mail.ru')

        telephone_input = self.browser.find_element(*RegisterPage.TEL_INPUT)
        telephone_input.send_keys(tel)

        password_input = self.browser.find_element(*RegisterPage.PASS_INPUT)
        password_input.send_keys(password)

        confirm_password_input = self.browser.find_element(*RegisterPage.CONFIRM_PASS_INPUT)
        confirm_password_input.send_keys(password)

        policy_agree = self.browser.find_element(*RegisterPage.POLICY_CHECKBOX)
        policy_agree.click()

        continue_button = self.browser.find_element(*RegisterPage.SUBMIT)
        continue_button.click()

        success_page = self.browser.current_url
        self.browser.get(success_page)
        return self.browser
