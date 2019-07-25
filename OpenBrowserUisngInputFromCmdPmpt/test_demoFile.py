import pytest
from selenium import webdriver
import time
@pytest.mark.usefixtures("oneTimeSetUp")
class Test_OpenBrowser:
    @pytest.fixture(autouse=True)
    def setUp(self): # it works even without "oneTimeSetUp" placing as a parameter for this method.
        self.driver.get("https://www.amazon.in")
        self.driver.maximize_window()
        print(self.driver)
        time.sleep(5)
        print(self.driver)

    def test_method1(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Category')]").click()
        time.sleep(5)
        print(self.driver)



"""
To generate html report just use --
html=C:\Users\mallikar\Desktop\htmlReport.html to genreate file in specific location.
if u want the file to be generated in the current project directory just use 
--html=fileName.html


"""