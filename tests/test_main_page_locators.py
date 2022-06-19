import allure

from src.main_page import MainPage


@allure.epic('Main Page')
@allure.title('Check main page locators')
@allure.severity('Normal')
def test_main_page_locators(browser):
    browser.get(browser.url)
    page = MainPage(browser)

    page.visibility_of_element(MainPage.SEARCH_INPUT)
    page.visibility_of_element(MainPage.ITEM_IN_BASKET)
    page.visibility_of_element(MainPage.BASKET_BUTTON)
    page.visibility_of_element(MainPage.CURRENCY_BUTTON)
    page.visibility_of_element(MainPage.MENU)
