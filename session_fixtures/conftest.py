import pytest

@pytest.fixture(scope="class", autouse=True)
def setUp():
    print("Once per session")
    yield
    print("Once after session")