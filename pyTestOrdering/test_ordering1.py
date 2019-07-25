import pytest

@pytest.mark.run(order=1)
def test_method1(oncePerClass, setUp):
    print("test_ordering1 Method 1")

@pytest.mark.run(order=4)
def test_method4(oncePerClass, setUp):
    print("test_ordering1 Method 4")

@pytest.mark.run(order=5)
def test_method5(oncePerClass, setUp):
    print("test_ordering1 Method 5")

@pytest.mark.run(order=6)
def test_method6(oncePerClass, setUp):
    print("test_ordering1 Method 6")

@pytest.mark.run(order=2)
def test_method2(oncePerClass, setUp):
    print("test_ordering1 Method 2")

@pytest.mark.run(order=3)
def test_method3(oncePerClass, setUp):
    print("test_ordering1 Method 3")


"""
in case we do not specify ordering the tests will get executed in the same order
in which we have defined test methods.

If we want to specify the particular oder then we have to mention the order using
@pytest.mark.run(order=?)
"""


"""
CAUTION : If we have two .py files with test methods on both .py files with same ordering
then when we run, 1 method from 1st module is run and then the same method(ordering) from another
.py file will be run and in this case class level method will also be run every-time for
each method because control is moving back and forth for every method.
"""