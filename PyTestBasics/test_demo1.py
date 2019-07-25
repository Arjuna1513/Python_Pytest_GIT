# import pytest

def test_method1(setUpPerModule,setUp):
    print("Pytest conf method 1")

def test_method2(setUpPerModule, setUp):
    print("Pytest conf method 2")

"""
If we have 10 modules and if want same setUp() for all then we have to keep 10 setUp() in each 
module.

To avoid that we can have conftest.py file and we can place setUp() in this and 
in command prompt change directory to project-->package and enter the below command
py.test -v -s moduleName1 moduleName2 then all the tests from both the modules will run.

IMP NOTE --> the name of the config file should be conftest.py only, u cannot give some other name.

We should pass the name of the module level test name as parameter to every test methods.
"""
