"""
Creates WebDriver instance based on browser
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


class WebDriverRoot():
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def get_webdriver_instance(self):
        if self.base_url is None:
            self.base_url = 'www.camelodge.com'

        if self.browser == 'firefox':
            driver = webdriver.Firefox()
        # Todo Edge browser
        # Todo Browserless
        elif self.browser == 'safari':
            driver = webdriver.Safari(executable_path='/Applications/Safari.app/Contents/MacOS/Safari')
        elif self.browser == 'chrome_headless':
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window_size=2560X1600")
            print(os.getcwd() + "/chromedriver")
            chrome_driver = os.getcwd() + "/chromedriver"
            driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
        elif self.browser == 'chrome':
            print(os.getcwd() + "/chromedriver")
            chrome_driver = os.getcwd() + "/chromedriver"
            driver = webdriver.Chrome(executable_path=chrome_driver)
        else:
            driver = webdriver.Firefox()

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(url=self.base_url)
        return driver



