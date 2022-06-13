import datetime
import logging
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="firefox",
        choices=["chrome", "firefox", "opera", "safari"]
    )
    parser.addoption("--drivers", default=os.path.expanduser("~/drivers"))
    parser.addoption("--url", default='http://192.168.1.60:8081')
    parser.addoption("--executor", default="192.168.1.60")
    parser.addoption('--log_level', action='store', default='DEBUG')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    drivers = request.config.getoption("--drivers")
    main_url = request.config.getoption('--url')
    executor = request.config.getoption("--executor")
    log_level = request.config.getoption('--log_level')

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f'logs/{request.node.name}.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info('===> Test {} started at {}'.format(request.node.name, datetime.datetime.now()))

    options = Options()

    if executor == 'local':
        if browser_name == 'chrome':
            browser = webdriver.Chrome(executable_path=f'{drivers}/chromedriver')
        elif browser_name == 'opera':
            options.add_experimental_option('w3c', True)
            browser = webdriver.Opera(executable_path=f'{drivers}/operadriver', options=options)
        elif browser_name == 'firefox':
            browser = webdriver.Firefox(executable_path=f'{drivers}/geckodriver')
        elif browser_name == 'safari':
            browser = webdriver.Safari()
        else:
            raise ValueError("Browser doesn't supported")
    else:
        caps = {"browserName": browser_name,
                'name': 'Anna'}
        if browser_name == 'opera':
            options.add_experimental_option('w3c', True)

        browser = webdriver.Remote(
            command_executor=f"http://{executor}:4444/wd/hub",
            desired_capabilities=caps, options=options
        )

    browser.log_level = log_level
    browser.logger = logger

    browser.maximize_window()
    browser.url = main_url

    def fin():
        browser.quit()
        logger.info('===> Test {} finished at {}'.format(request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    return browser
