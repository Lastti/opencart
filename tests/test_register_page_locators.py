from src.register_page import RegisterPage


def test_register_page_locators(browser):
    browser.get(browser.url)
    page = RegisterPage(browser)

    page.switch_to_register_page()
    page.visibility_of_element(RegisterPage.REGISTER_TITLE)
    page.visibility_of_element(RegisterPage.FIRSTNAME_INPUT)
    page.visibility_of_element(RegisterPage.LASTNAME_INPUT)
    page.visibility_of_element(RegisterPage.EMAIL_INPUT)
    page.visibility_of_element(RegisterPage.TEL_INPUT)
    page.visibility_of_element(RegisterPage.PASS_INPUT)
    page.visibility_of_element(RegisterPage.CONFIRM_PASS_INPUT)
    page.visibility_of_element(RegisterPage.CONTINUE_BUTTON)
