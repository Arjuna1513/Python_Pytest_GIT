import pytest


@pytest.mark.usefixtures("setUp")
class Test_Module:

    def test_class_test(self):
        print("test class")


def test_outclass(setUp):
    print("outside the class")