import pytest

@pytest.fixture()
def setUp():
    print("Runs before every method")
    print()
    yield
    print("Runs after every method")

@pytest.fixture(scope="module")
def setUpPerModule():
    print("Runs once before every module starts")
    yield
    print("Runs once after every module ends")

"""
Here the scope="module" should be set else this method will run for every method just like setUp
after creating module level method just like above we should give the name of this method
for every test methods as parameter...
"""