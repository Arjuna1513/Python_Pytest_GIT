import pytest
from selenium import webdriver

@pytest.yield_fixture(scope='class')
def oneTimeSetUp(browser, request):
    print("Runs setup once per class")
    if browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    if request is not None:
        request.cls.driver = driver
    yield driver

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.yield_fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')


