from src.main_page import MainPage


def test_change_currency(browser):
    browser.get(browser.url)
    page = MainPage(browser)

    expected_currency = '€'
    currency = page.switch_currency_to('EUR')
    page.check_result_as_expected(currency.text, expected_currency)

