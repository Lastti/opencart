from src.admin_page import AdminPage

from src.test_data import ADM_LOGIN, ADM_PASS, ADMIN


def test_add_new_product(browser):
    browser.get(browser.url + ADMIN)
    page = AdminPage(browser)

    page.login_with_creds(ADM_LOGIN, ADM_PASS)
    page.switch_to_catalog()
    page.switch_to_products()
    page.add_new_item()
    page.visibility_of_element(AdminPage.SUCCESS_MESSAGE)
