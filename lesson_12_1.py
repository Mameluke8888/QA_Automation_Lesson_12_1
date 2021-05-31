from browser import Browser
from UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from alert import Alert
from iframe import IFrame
import time

URL = "http://techskillacademy.net/practice/"

def test_simple_alert():
    browser = Browser(URL, "Firefox")
    alert_btn = Element(browser, By.XPATH, "//button[@onclick='openAlert()']")
    alert_btn.click()

    alert = Alert(browser.get_driver().switch_to.alert)
    time.sleep(2)
    alert.accept()
    time.sleep(2)

    browser.shutdown()

def test_confirmation_alert():
    browser = Browser(URL, "Firefox")
    confirm_btn = Element(browser, By.XPATH, "//button[@onclick='openConfirmationAlert()']")
    confirm_btn.click()

    alert = Alert(browser.get_driver().switch_to.alert)
    time.sleep(2)
    alert.dismiss()

    time.sleep(2)
    msg = Element(browser, By.ID, 'msg')
    assert msg.get_text() == "You pressed CANCEL!"

    confirm_btn.click()
    alert.accept()

    assert msg.get_text() == "You pressed OK!"

    browser.shutdown()


def test_prompt_alert():
    browser = Browser(URL, "Firefox")
    prompt_btn = Element(browser, By.XPATH, "//button[@onclick='openPrompt()']")

    prompt_btn.click()

    alert = Alert(browser.get_driver().switch_to.alert)

    time.sleep(2)
    name = "Svetlana"
    alert.send_keys(name)
    alert.accept()

    msg = "Hello {}! How are you today?".format(name)
    prompt_msg = Element(browser, By.ID, 'demo')
    assert prompt_msg.get_text() == msg

    browser.shutdown()


def test_iframe():
    browser = Browser(URL, "Firefox")
    iframe = IFrame(browser, By.TAG_NAME, 'iframe')
    iframe.switch_to_frame()

    time.sleep(2)
    Element(browser, By.CLASS_NAME, "logo__title").wait_until_visible()

    iframe.switch_to_default_content()
    browser.shutdown()


if __name__ == "__main__":
    # test_simple_alert()
    # test_confirmation_alert()
    # test_prompt_alert()
    test_iframe()



















