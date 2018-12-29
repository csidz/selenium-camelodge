from pages.signupPage.signup_page import SignupPage
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup", "set_up")
class SignupTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, one_time_setup):
        self.signup_page = SignupPage(self.driver)

    def test_signup_valid_creds(self):
        self.signup_page.signup(email='jack.suze@gmail.com', password='123456', confirm_password='123456')
        result = self.signup_page.validate_signup_successful()
        assert result

    # test_email_field_is_autofocussed
    # test_invalid_creds
    # test_signup_different_password_confirm_password
    # test_signup_existing_user
