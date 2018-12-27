"""
Creates WebDriver instance based on browser
"""
from selenium import webdriver


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
        # Todo Chrome browser
        # Todo Browserless
        elif self.browser == 'safari':
            driver = webdriver.Safari(executable_path='/Applications/Safari.app/Contents/MacOS/Safari')
        else:
            driver = webdriver.Firefox()

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(url=self.base_url)
        return driver



