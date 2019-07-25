import unittest
import pytest

@pytest.mark.usefixtures("setUp")
class Class_1(unittest.TestCase):

    def test_class1Method1(self):
        print("Class1Method1")

    def test_class1Method2(self):
        print("Class1Method2")

# if __name__=="__main__":
#     unittest.main()