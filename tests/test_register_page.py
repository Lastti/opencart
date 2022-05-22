from src.base_func import visibility_of_element
from src.register_page import RegisterPageLocators


def test_register_page(browser):
    browser.get(browser.url + '/index.php?route=account/register')

    visibility_of_element(browser, RegisterPageLocators.REGISTER_TITLE)
    visibility_of_element(browser, RegisterPageLocators.FIRSTNAME_INPUT)
    visibility_of_element(browser, RegisterPageLocators.LASTNAME_INPUT)
    visibility_of_element(browser, RegisterPageLocators.EMAIL_INPUT)
    visibility_of_element(browser, RegisterPageLocators.TEL_INPUT)
    visibility_of_element(browser, RegisterPageLocators.PASS_INPUT)
    visibility_of_element(browser, RegisterPageLocators.CONFIRM_PASS_INPUT)
    visibility_of_element(browser, RegisterPageLocators.CONTINUE_BUTTON)
