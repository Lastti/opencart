import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step('Find element')
    def find_element_by(self, locator):
        try:
            element = self.browser.find_element(*locator)
        except NoSuchElementException as e:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name='screenshot_image',
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.error('Element with locator: {} was not found'.format(locator))
            raise AssertionError(e.msg)

        self.logger.info('Element with locator: {} was found'.format(locator))
        return element

    @allure.step('Checking visibility of an element')
    def visibility_of_element(self, locator):
        """Check an element is visible"""
        try:
            element = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name=f'{self.browser.session_id}.png',
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.error('Element with locator: {} was not found'.format(locator))
            raise AssertionError(f'Element with locator: {locator} is not visible')

        self.logger.info('Element with locator: {} was found'.format(locator))
        return element

    @allure.step('Checking invisibility of an element')
    def element_is_not_visible(self, locator):
        """Check an element is not visible"""
        try:
            WebDriverWait(self.browser, 5).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as(),
                name=f'{self.browser.session_id}.png',
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.error('Element with locator: {} is wrongly displayed'.format(locator))
            raise AssertionError(f'Element with locator: {locator} is wrongly displayed')

        self.logger.info('Element with locator: {} proved as not visible'.format(locator))

    @allure.step('Comparison actual result with expected')
    def check_result_as_expected(self, actual_res, expected_res):
        """Check the actual result is the same as expected"""
        try:
            assert actual_res == expected_res
        except Exception:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name='screenshot_image',
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.error('Result of comparison "{}" with "{}" is not successful'.format(actual_res, expected_res))
            raise AssertionError(f'Wrong result. Expected: {expected_res}, actual: {actual_res}')

        self.logger.info('Result of comparison {} with {} is successful'.format(actual_res, expected_res))
