import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class Test_ClassDemo():

    @pytest.fixture(autouse=True)
    def setUpClass(self, oneTimeSetUp):
        print(self.value)

    def test_methodA(self):
        print(self.value)

# Make sure that in pytest the class name should start with Test always and methods
#  should start with test

# @pytest.mark.usefixtures("oneTimeSetUp")
# class TestClassDemo():
#
#
#     @pytest.fixture(autouse=True)
#     def setUp(self, oneTimeSetUp):
#         print(self.value)
#
#
#     def test_methodA(self):
#         print(self.value)
#
#
#
#     def test_methodB(self):
#         print("Running method B")