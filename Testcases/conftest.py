import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "Firefox":
        driver = webdriver.Firefox()
    elif browser == "Edge":
        driver = webdriver.Edge()
    else:
        print("headless mode")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("headless")
        driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()
    return driver



