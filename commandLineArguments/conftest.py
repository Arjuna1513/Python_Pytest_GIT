import pytest

@pytest.yield_fixture(scope="module")
def oncePerClass(browser):
    print("Runs setUp once per class")
    # since we want to make use of the browser value returned by browser method use the method
    # name as as parameter
    if browser == 'firefox':
        print("User entered firefox")
    else:
        print("We will use chrome")
    yield
    print("Runs setUp once after entire class execution is done")

@pytest.yield_fixture()
def setUp():
    print("Runs setUp once before every method")
    yield
    print("Runs setUp once after every method")

# Let's define something that reads values from command prompt

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.yield_fixture(scope="session")
def browser(request):
    return request.config.getoption('--browser')
    # the name of the method doesn't have to be a browser for convenience we have given
    # request.config.getoption('--browser') will read the value provided and will return
    # the same to conftest