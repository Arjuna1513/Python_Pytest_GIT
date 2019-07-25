import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp")
class SampleTests(unittest.TestCase):
    def test_method1(self):
        self.driver.get("https://www.facebook.com")
        title = self.driver.title
        print(title)