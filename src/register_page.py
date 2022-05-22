from selenium.webdriver.common.by import By


class RegisterPageLocators:
    REGISTER_TITLE = (By.CSS_SELECTOR, 'h1')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input.btn')
    FIRSTNAME_INPUT = (By.NAME, 'firstname')
    LASTNAME_INPUT = (By.NAME, 'lastname')
    EMAIL_INPUT = (By.NAME, 'email')
    TEL_INPUT = (By.NAME, 'telephone')
    PASS_INPUT = (By.NAME, 'password')
    CONFIRM_PASS_INPUT = (By.NAME, 'confirm')
