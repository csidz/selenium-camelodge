from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.signupPage.signup_page import SignupPage
import unittest
import time


class SignupTests(unittest.TestCase):
    base_url = "https://camelodge.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(base_url)

    def test_signup_valid_creds(self):
        signup_page = SignupPage(self.driver)
        signup_page.signup(email='jack.suze@gmail.com', password='123456', confirm_password='123456')

        result = signup_page.validate_signup_successful()
        assert result

        self.driver.close()
        self.driver.quit()

    # test_email_field_is_autofocussed
    # test_invalid_creds
    # test_signup_different_password_confirm_password
    # test_signup_existing_user
