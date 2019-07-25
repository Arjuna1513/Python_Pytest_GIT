import pytest
from selenium import webdriver
@pytest.yield_fixture(scope='class')
def oneTimeSetUp(browser, request):
    print("Runs once before the class execution starts")
    if browser == 'firefox':
        value = 100
    else:
        value = 200

    if request.cls is not None:
        request.cls.value = value
    yield value


def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.yield_fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')
