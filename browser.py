from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class Browser:
    """
    This class is wrapper around Selenium driver
    """
    # Exercise  # 1
    # Add to Browser 's initialization method an exception handling that will print out
    # the executable path to the driver is incorrect
    def __init__(self, url, browser_name=""):
        # decide which browser to open, can be extended
        try:
            if browser_name.lower() == "firefox":
                self.driver = webdriver.Firefox(executable_path='drivers/geckodriver')
            else:
                self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        except WebDriverException as err:
            print("Incorrect path to WebDriver:", err)
            raise

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # by default 10, but we can add this like a parameter

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()
