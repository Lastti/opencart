import allure

from src.main_page import MainPage


@allure.epic('Main Page')
@allure.title('Check currency changing')
@allure.severity('Normal')
def test_change_currency(browser):
    browser.get(browser.url)
    page = MainPage(browser)

    expected_currency = '€'
    currency = page.switch_currency_to('EUR')
    page.check_result_as_expected(currency.text, expected_currency)
