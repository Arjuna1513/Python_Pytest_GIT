import pytest

# @pytest.fixture()
# def setUp():
#     print("Runs before every method")
#     print()

@pytest.yield_fixture()
def setUp():
    print("Runs before every method")
    print()
    yield
    print("Runs after every method")

def test_method1(setUp):
    print("Pytest method 1")

def test_method2(setUp):
    print("Pytest method 2")

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
different ways of running modules/methods:
py.test -v -s  --> It will run all the modules present in the current package
py.test -v -s moduleName --> will run all the methods of the given module
py.test -v -s moduleName.py::methodName --> executes only the given method from given module.
py.test -v -s moduleName1.py::methodName moduleName2.py::methodName --> will run the given
method name from moduleName1.py and given method from moduleName2.py so totally two methods are run here.

"""