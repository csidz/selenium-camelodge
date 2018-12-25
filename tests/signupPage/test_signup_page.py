from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.signupPage.signup_page import SignupPage
import unittest
import time


class SignupTests(unittest.TestCase):

    def test_signup_valid_creds(self):
        base_url = "https://camelodge.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        signup_page = SignupPage(driver)

        signup_page.signup(email='jack.suze@gmail.com', password='123456', confirm_password='123456')

        welcome_message_sign_up = driver.find_element(By.XPATH, "//div[@class='alert-notice'][contains(text(), 'Welcome! You have signed up successfully.')]")
        if welcome_message_sign_up:
            print("Sign up is successful")
        else:
            print("Sign up failed")

        driver.close()
        driver.quit()

    # test_email_field_is_autofocussed
    # test_invalid_creds
    # test_signup_different_password_confirm_password
    # test_signup_existing_user
