from selenium.webdriver.common.by import By


class AdminLoginPageLocators:
    LOGIN_TITLE = (By.CLASS_NAME, 'panel-title')
    USERNAME_INPUT = (By.ID, 'input-username')
    PASSWORD_INPUT = (By.ID, 'input-password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
