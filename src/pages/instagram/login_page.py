from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.utilities.yaml_actions import YamlActions


class LoginPageLocators:
    login_input_locator = (By.NAME, "username")
    password_input_locator = (By.NAME, "password")
    enter_button_locator = (By.XPATH, "//button[@type='submit']")


class InstagramLoginPage(BasePage):

    def login(self):
        yaml_actions = YamlActions("../../config.yaml");
        input_login = self.find_element(LoginPageLocators.login_input_locator)
        input_login.click()
        input_login.send_keys(yaml_actions.get_yaml_value_by_key("inst_login"))
        input_pw = self.find_element(LoginPageLocators.password_input_locator)
        input_pw.click()
        input_pw.send_keys(yaml_actions.get_yaml_value_by_key("inst_password"))
        enter_btn = self.find_element(LoginPageLocators.enter_button_locator)
        enter_btn.click()
