from selenium.webdriver.common.by import By
from selenium import webdriver
from src.pages.base_page import BasePage


class NotifDialogLocators:
    dialog_locator = (By.CSS_SELECTOR, ".piCib")
    switch_on_button_locator = (By.CSS_SELECTOR, ".IiDR")
    not_now_button_locator = (By.CSS_SELECTOR, ".HoLwm")


class NotificationDialog(BasePage):

    def notifications_skip(self):
        notification_dialog = self.find_element(NotifDialogLocators.dialog_locator)
        if notification_dialog.is_displayed():
            self.find_element(NotifDialogLocators.not_now_button_locator).click()


class SaveCredsDialogLocators:
    dialog_locator = (By.CSS_SELECTOR, ".piCib")
    switch_on_button_locator = (By.CSS_SELECTOR, ".IiDR")
    not_now_button_locator = (By.CSS_SELECTOR, ".HoLwm")


"""class SaveCredsDialog(BasePage):

    def save_creds_skip(self):
        save_creds_dialog = self.find_element(SaveCredsDialogLocators.dialog_locator)
        if save_creds_dialog .is_displayed():
            self.find_element(SaveCredsDialogLocators.not_now_button_locator).click()"""
