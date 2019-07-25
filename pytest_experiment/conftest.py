import pytest

@pytest.fixture(scope="class")
def oneTimeSetUp(request):
    result = "Arjuna"
    request.cls.resultVar = result
    dict1 = {'id':"Arjuna", 'pwd':"Arjuna@12345"}
    request.cls.globalVar = dict1
    yield


# @pytest.fixture(scope="class")
# def globalVariables(request):
#     dict1 = {'id':"Arjuna", 'pwd':"Arjuna@12345"}
#     request.cls.globalVar = dict1
#     yield