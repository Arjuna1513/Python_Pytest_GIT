from selenium import webdriver
class WebdriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def get_driver(self):
        if self.browser == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
            return driver
        elif self.browser == "ie":
            driver = webdriver.Ie()
            return driver
        else:
            driver = webdriver.Chrome()
            return driver

