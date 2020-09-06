from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser...")
    elif browser == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference('devtools.jsonview.enabled', False) # This is important to prevent JSON formatting
        driver = webdriver.Firefox(fp)
        print("Launching Firefox browser...")
    else:
        #Default browser needed in order to avoid errors when no parameter on CLI
        driver = webdriver.Chrome()
        print("Launching Chrome browser...")

    return driver


def pytest_addoption(parser): # This method gets the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request): # This method returns the Browser value to setup method
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata["Project Name"] = "Instacart Crawler"
    config._metadata["Tester"] = "Carlos"
