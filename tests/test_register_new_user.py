from src.register_page import RegisterPage
from src.test_data import FIRST_NAME, LAST_NAME, USER_PASS, TEL


def test_register_new_user(browser):
    browser.get(browser.url)
    page = RegisterPage(browser)

    page.switch_to_register_page()
    page.register_new_user(FIRST_NAME, LAST_NAME, TEL, USER_PASS)
    success_message = browser.find_element(*RegisterPage.SUCCESS_MESSAGE)
    expected_message = 'Your Account Has Been Created!'
    page.check_result_as_expected(success_message.text, expected_message)
