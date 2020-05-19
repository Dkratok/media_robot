from selenium import webdriver
from src.utilities.yaml_actions import *


class DriverRun:
    def __init__(self):
        """Constructor"""
        ya = YamlActions('../../config.yaml')
        self.browser_type = ya.get_yaml_value_by_key('browser')

    def run_driver(self):
        if self.browser_type == "firefox":
            return webdriver.Firefox("../../selenium_drivers/geckodriver.exe")
        elif self.browser_type == "ie":
            return webdriver.Ie('../../selenium_drivers/IEDriverServer.exe')
        elif self.browser_type == "edge":
            return webdriver.Edge('../../selenium_drivers/msedgedriver.exe')
        else:
            return webdriver.Chrome('../../selenium_drivers/chromedriver')

