import allure

from src.admin_page import AdminPage
from src.test_data import TestData


@allure.epic('Admin Page')
@allure.title('Check admin page locators')
@allure.severity('Normal')
def test_admin_page_locators(browser):
    browser.get(browser.url + TestData.ADMIN)
    page = AdminPage(browser)

    page.visibility_of_element(AdminPage.LOGIN_TITLE)
    page.visibility_of_element(AdminPage.USERNAME_INPUT)
    page.visibility_of_element(AdminPage.LOGIN_TITLE)
    page.visibility_of_element(AdminPage.LOGIN_TITLE)
    page.visibility_of_element(AdminPage.LOGIN_TITLE)
