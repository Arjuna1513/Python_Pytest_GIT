import pytest

@pytest.mark.run(order=1)
def test_method1(oncePerClass, setUp):
    print("Method 1")

@pytest.mark.run(order=4)
def test_method4(oncePerClass, setUp):
    print("Method 4")

@pytest.mark.run(order=5)
def test_method5(oncePerClass, setUp):
    print("Method 5")

@pytest.mark.run(order=6)
def test_method6(oncePerClass, setUp):
    print("Method 6")

@pytest.mark.run(order=2)
def test_method2(oncePerClass, setUp):
    print("Method 2")

@pytest.mark.run(order=3)
def test_method3(oncePerClass, setUp):
    print("Method 3")


"""
in case we do not specify ordering the tests will get executed in the same order
in which we have defined test methods.

If we want to specify the particular oder then we have to mention the order using
@pytest.mark.run(order=?)
"""