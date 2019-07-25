import pytest

@pytest.yield_fixture()
def setUp():
    print("Runs before every method")
    yield
    print("Runs after every method is run")

@pytest.fixture(scope="module")
def oncePerClass():
    print("Run once per class")
    yield
    print("Runs once after entire class is run")
