__author__ = 'pavelkosicin'

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.navigation import NavigationHelper
from fixture.validation import ValidationHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.navigation = NavigationHelper(self)
        self.validation = ValidationHelper(self)

    def destroy(self):
        self.wd.quit()
