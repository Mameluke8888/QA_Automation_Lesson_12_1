from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class Alert:
    """
    This class is wrapper around Selenium alerts
    """
    def __init__(self, alert):
        self._alert = alert

    def accept(self):
        try:
            self._alert.accept()
        except AttributeError:
            print("Assigned object is not an Alert")

    def dismiss(self):
        try:
            self._alert.dismiss()
        except AttributeError:
            print("Assigned object is not an Alert")

    def send_keys(self, text):
        try:
            self._alert.send_keys(text)
        except AttributeError:
            print("Assigned object is not an Alert")

    def get_text(self):
        try:
            return self._alert.text
        except AttributeError:
            print("Assigned object is not an Alert")
