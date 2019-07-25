import pytest
import unittest
import time

@pytest.mark.usefixtures("oneTimeSetUp")
class SampleTests1(unittest.TestCase):
    def test_method1(self):
        # time.sleep(10)
        self.driver.get("https://www.google.com")
        title = self.driver.title
        print(title)