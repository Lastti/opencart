from src.admin_login_page import AdminLoginPageLocators
from src.base_func import visibility_of_element


def test_admin_login_page(browser):
    browser.get(browser.url + '/admin')

    visibility_of_element(browser, AdminLoginPageLocators.LOGIN_TITLE)
    visibility_of_element(browser, AdminLoginPageLocators.USERNAME_INPUT)
    visibility_of_element(browser, AdminLoginPageLocators.PASSWORD_INPUT)
    visibility_of_element(browser, AdminLoginPageLocators.FORGOTTEN_PASSWORD)
    visibility_of_element(browser, AdminLoginPageLocators.SUBMIT_BUTTON)
