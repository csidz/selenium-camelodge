from pages.basePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver = driver

    # LOCATORS
    _edit_account_link_text = "My Account"
    _log_out_link_text = "Log out"

    # VALIDATIONS
    def validate_edit_account_link_present(self):
        result = self.is_element_present(locator=self._edit_account_link_text, locator_type="link")
        self.capture_screenshot_on_failure(result=result, failure_message="My Account link text not present")
        return result

    def validate_log_out_link_present(self):
        result = self.is_element_present(locator=self._log_out_link_text, locator_type="link")
        self.capture_screenshot_on_failure(result=result, failure_message="Log out link text not present")
        return result
