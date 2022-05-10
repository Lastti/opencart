import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Chose browser to run')
    parser.addoption("--drivers", default=os.path.expanduser("~/drivers"))
    parser.addoption("--url", default='http://192.168.1.60:8081')


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('--browser')
    drivers = request.config.getoption("--drivers")
    main_url = request.config.getoption('--url')

    if browser_name == 'chrome':
        browser = webdriver.Chrome(executable_path=f'{drivers}/chromedriver')
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=f'{drivers}/geckodriver')
    elif browser_name == 'safari':
        browser = webdriver.Safari()
    else:
        raise ValueError("Browser doesn't supported")

    browser.maximize_window()
    browser.url = main_url
    request.addfinalizer(browser.quit)

    return browser
