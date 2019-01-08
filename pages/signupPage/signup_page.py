from pages.basePage import BasePage


class SignupPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver = driver

    # LOCATORS
    _signup_link = "Sign Up"
    _email_input_autofocus = "input[autofocus='autofocus']#user_email"
    _email_input = "user_email"
    _password_input = "user_password"
    _confirm_password_input = "user_password_confirmation"
    _signup_button = "#new_user input[value='Sign up']"
    _signup_welcome_text = "//div[@class='alert-notice'][contains(text(), 'Welcome! You have signed up successfully.')]"

    # ACTIONS
    def click_signup_link(self):
        self.element_click(locator=self._signup_link, locator_type="link")

    def enter_email(self, email):
        self.send_keys(data=email, locator=self._email_input)

    def enter_password(self, password):
        self.send_keys(data=password, locator=self._password_input)

    def enter_confirm_password(self, confirm_password):
        self.send_keys(data=confirm_password, locator=self._confirm_password_input)

    def click_signup_button(self):
        self.element_click(locator=self._signup_button, locator_type='css')

    # CHAIN OF ACTIONS
    def signup(self, email=None, password=None, confirm_password=None):
        self.click_signup_link()
        self.enter_email(email=email)
        self.enter_password(password=password)
        self.enter_confirm_password(confirm_password=confirm_password)
        self.click_signup_button()

    # VALIDATIONS
    def validate_signup_successful_message(self):
        result = self.is_element_present(locator=self._signup_welcome_text, locator_type="xpath")
        self.capture_screenshot_on_failure(result, failure_message="Signup Confirmation message not found")
        return result

    def validate_autofocus_on_email(self):
        result = self.is_element_present(locator=self._email_input_autofocus, locator_type="css")
        self.capture_screenshot_on_failure(result, failure_message="Autofocus is not on Signup Email Field")
        return result
