import unittest
from src.pages.instagram.login_page import InstagramLoginPage
from src.pages.instagram.login_dialogs import NotificationDialog
from src.core.driver_run import DriverRun


class BaseUIScriptA(unittest.TestCase):

    def setUp(self):
        driver_run = DriverRun()
        driver = driver_run.run_driver()
        driver.maximize_window()
        driver.get("https://instagram.com")
        instagramLoginPage = InstagramLoginPage(driver)
        instagramLoginPage.login()
        notificationsDialog = NotificationDialog(driver)
        notificationsDialog.notifications_skip()

    def test_script(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def tearDown(self):
        """self.driver.close()"""


if __name__ == "__main__":
    unittest.main()