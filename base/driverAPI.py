from selenium.webdriver.common.by import By
import utilities.customLogger as cl
from traceback import print_stack
import logging
from selenium.webdriver.common.keys import Keys


class SeleniumDriver():

    log = cl.custom_logger(log_level=logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "partial_link":
            return By.PARTIAL_LINK_TEXT
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "tag":
            return By.TAG_NAME
        else:
            self.log.info(msg=f'Locator type {locator_type} not correct or supported')
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type=locator_type)
            element = self.driver.find_element(by=by_type, value=locator)
            self.log.info(msg=f'Element with locator {locator} and locator type {locator_type} Found')
        except ValueError:
            self.log.info(f'Element with locator {locator} and locator type {locator_type} NOT Found')
        return element

    def element_click(self, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator=locator, locator_type=locator_type)
            element.click()
            self.log.info(msg=f'Clicked on the element with locator {locator} and locator type {locator_type}')
        except ValueError:
            self.log.info(f'Cannot click on the element with locator {locator} and locator type {locator_type}')
            print_stack()

    def send_keys(self, data, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator=locator, locator_type=locator_type)
            element.send_keys(data)
            self.log.info(f'Sent data on element with locator {locator} locator type {locator_type}')
        except ValueError:
            self.log.info(f'Cannot send data on element with locator {locator} locator type {locator_type}')
            print_stack()

    def is_element_present(self, locator="", locator_type="id"):
        try:
            element = self.get_element(locator=locator, locator_type=locator_type)
            print("element:-- ", element)
            if element:
                return True
        except ValueError:
            return False


    # getElementList
    # getUrlsList
    # getText
    # getHref
    # isElementPresent
    # isElementDisplayed
    # elementPresenceCheck
    # waitForElement
    # waitForElementPresence
    # webScroll
    # getCurrentWindowsHandle
    # getAllWindowsHandles
    # closeChildFocusBaseWindow
    # gettitle
    # getcurrentpageurl



















