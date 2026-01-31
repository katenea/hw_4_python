import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    driver_options = Options()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.timeout = 10
    return browser