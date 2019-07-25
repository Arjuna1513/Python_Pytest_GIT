import pytest
import unittest


class Ex1(unittest.TestCase):

    pytest.global_variable = 100

    @pytest.fixture(scope="class")
    def OneTimeSetUp(self):
        print("Runs before class")
        yield
        print("after class")

    def test_ex1(self):
        print("test 1")
        print(pytest.global_variable)
