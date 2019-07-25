import unittest
import pytest

@pytest.mark.usefixtures("setUp")
class Class_2(unittest.TestCase):

    def test_class2Method1(self):
        print("Class2Method1")

    def test_class2Method2(self):
        print("Class2Method2")

# if __name__=="__main__":
#     unittest.main()