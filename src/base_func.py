from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def visibility_of_element(self, locator):
        """Check an element is visible"""
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.browser.save_screenshot(f'{self.browser.session_id}.png')
            raise AssertionError(f'Element with locator: {locator} is not visible')
        return self.browser

    def element_is_not_visible(self, locator):
        """Check an element is not visible"""
        try:
            WebDriverWait(self.browser, 5).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.browser.save_screenshot(f'{self.browser.session_id}.png')
            raise AssertionError(f'Element with locator: {locator} is still visible')

    def check_result_as_expected(self, actual_res, expected_res):
        """Check the actual result is the same as expected"""
        assert actual_res == expected_res, f'Wrong result. Expected: {expected_res}, actual: {actual_res}'
