from src.admin_page import AdminPage
from src.test_data import TestData


def test_delete_new_product(browser):
    browser.get(browser.url + TestData.ADMIN)
    page = AdminPage(browser)

    page.login_with_creds(TestData.ADM_LOGIN, TestData.ADM_PASS)
    page.switch_to_catalog()
    page.switch_to_products()
    product_name = page.add_new_item()
    page.filter_by_name(product_name)
    page.check_item_after_filter()
    page.delete_item()
    page.visibility_of_element(AdminPage.SUCCESS_MESSAGE)

    result = browser.find_element(*AdminPage.RESULT_MESSAGE)
    expected_res = 'No results!'
    page.check_result_as_expected(result.text, expected_res)
