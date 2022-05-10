from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def visibility_of_element(browser, locator):
    try:
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        browser.save_screenshot(f'{browser.session_id}.png')
        raise AssertionError(f'Element with locator: {locator} is not visible')
