import pytest

# @pytest.fixture()
# def setUp():
#     print("Runs before every method")
#     print()

@pytest.fixture()
def setUp():
    print("Runs before every method")
    print()
    yield
    print("Runs after every method")

def test_method3(setUp):
    print("Pytest method 3")

def test_method4(setUp):
    print("Pytest method 4")

"""
To define any method that needs to be run before every method, define it as fixture
(@pytest.fixture())
and then use the name of that method as a parameter in method.
"""

"""
and in case if u want any code to execute after every method we have something called 
yieldFixture() i.e. instead of using pytest.fixture use pytest.yieldfixture()
so in this method anything written above yield keyword will be run before every method and 
code written after yield keyword will be executed after every method
"""

"""
If we change directory to the package in terminal and if we enter py.test -v -s
then all the modules present in that package will be executed 
 if we want only one module to get executed then provide the name of the module as 
 shown here : py.test -v -s test_PyTest_ex2.py
"""

"""
If the pytest version is above 2.10 then we don't have to use pytest.yield_fixture(),
pytest.fixture() is enough it will support yield.
"""