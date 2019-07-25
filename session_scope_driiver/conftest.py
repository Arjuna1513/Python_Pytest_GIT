import pytest
from selenium import webdriver
from session_scope_driiver.webdriver_factory import WebdriverFactory

@pytest.fixture(scope="session")
def oneTimeSetUp(request, browser_name):
    wdf = WebdriverFactory(browser_name)
    driver = wdf.get_driver()
    driver.maximize_window()
    # driver.get("https://www.google.com")
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver", driver)
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")