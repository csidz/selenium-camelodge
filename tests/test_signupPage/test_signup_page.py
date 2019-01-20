from pages.signupPage.signup_page import SignupPage
from pages.homePage.home_page import HomePage
from pages.usersPage.users_page import UsersPage
import pytest


@pytest.mark.usefixtures("one_time_setup", "set_up")
class TestSignupTests():
    @pytest.fixture(autouse=True)
    def classSetup(self, one_time_setup):
        self.signup_page = SignupPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.users_page = UsersPage(self.driver)

    def test_email_field_is_autofocused(self):
        self.signup_page.click_signup_link()
        autofocus_on_email = self.signup_page.validate_autofocus_on_email()
        assert autofocus_on_email

    def test_signup_different_password_confirm_password(self):
        self.signup_page.signup(email="${env.SIGNUP-EMAIL}", password="${env.SIGNUP-PASSWORD}", confirm_password="${env.SIGNUP-CONFIRM-PASSWORD-DIFFERENT}")
        users_page_title = self.users_page.validate_users_page_title()
        users_page_text = self.users_page.validate_users_page_text()
        pytest.assume(users_page_title)
        pytest.assume(users_page_text)

# Todo: User can signup even when signup_successful_message is not displayed. Based on signup_successful_message
#       we cannot fail the signup case. We should separate the validation of signup_successful_message and assign
#       low priority
    def test_signup_valid_creds(self):
        self.signup_page.clear_cookies()
        self.signup_page.signup(email="${env.SIGNUP-EMAIL}", password="${env.SIGNUP-PASSWORD}",
                                confirm_password="${env.SIGNUP-CONFIRM-PASSWORD-SAME}")
        signup_successful_message = self.signup_page.validate_signup_successful_message()
        my_account_link_text = self.home_page.validate_edit_account_link_present()
        pytest.assume(signup_successful_message)
        pytest.assume(my_account_link_text)

    # test_invalid_creds
    # test_signup_existing_user
