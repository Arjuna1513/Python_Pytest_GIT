import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class TestClass:

    def test_method1(self):
        print(self.resultVar)
        print()

    def test_method2(self):
        var1 = self.globalVar['pwd']
        var2 = "Arjuna@12345"
        assert var1, var2
        print(var1)