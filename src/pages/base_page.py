from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def find_element_in_container(self, xpath_container, xpath_locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located((By.XPATH(""))),
                                                      message=f"Can't find elements by locator {xpath_locator} in {xpath_container}")

    def go_to_site(self, base_url):
        return self.driver.get(base_url)
