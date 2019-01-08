from pages.basePage import BasePage


# User is redirected to this page when
# 1. password, confirm password do not match on signup
# 2. signup with existing user
class UsersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver = driver

    # LOCATORS
    _user_page_title = "The change you wanted was rejected (422)"
    _user_page_text = "The change you wanted was rejected.\n"\
                      "Maybe you tried to change something you didn't have access to.\n"\
                      "If you are the application owner check the logs for more information."

    def validate_users_page_title(self):
        result = self.validate_page_title(title_to_validate=self._user_page_title)
        self.capture_screenshot_on_failure(result, failure_message="Users page title does not match")
        return result

    def validate_users_page_text(self):
        result = self.validate_page_text(text_to_validate=self._user_page_text)
        self.capture_screenshot_on_failure(result, failure_message="Users page text does not match")
        return result
