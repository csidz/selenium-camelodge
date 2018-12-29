"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""

from base.driverAPI import DriverAPI
from traceback import print_stack
from utilities.util import Util


class BasePage(DriverAPI):
    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def validate_page_title(self, title_to_validate):
        """
         Verify the page Title

         Parameters:
             title_to_validate: Title on the page that needs to be verified
         """
        try:
            actual_title = self.getTitle()
            return self.util.verify_text_contains(actual_text=actual_title, expected_text=title_to_validate)
        except ValueError:
            self.log.error("Failed to get page title")
            print_stack()
            return False


