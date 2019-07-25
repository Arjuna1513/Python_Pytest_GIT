import pytest
import unittest
class Sample(unittest.TestCase):
    # @pytest.mark.sanity
    def test_method1(self):
        print("Hello world")

    def test_method2(self):
        print("Hello world")