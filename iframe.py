from browser import Browser
from UIElement import UIElement as Element
from selenium.common.exceptions import *


class IFrame(Element):
    """
    This class is wrapper around iframe
    """
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)

    def switch_to_frame(self):
        try:
            self.driver.switch_to.frame(self.get_element())
        except NoSuchElementException:
            print("Assigned iframe cannot be found and might not exist")

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
