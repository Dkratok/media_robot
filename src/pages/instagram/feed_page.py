from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class PostLocators:
    post_xpath_container = (By.XPATH, "//article[1]")
    username_xpath_locator = (By.XPATH, post_xpath_container, "a[@class='sqdOP yWX7d     _8A5w5   ZIAjV ']")


class Post(BasePage):

    def open_inst_account(self):
        user_account_link = self.find_element(PostLocators.username_xpath_locator)
        user_account_link.click()
