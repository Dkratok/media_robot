import unittest
from src.pages.instagram.login_page import InstagramLoginPage
from src.pages.instagram.login_dialogs import NotificationDialog
from src.core.driver_run import DriverRun


class BaseUIScript(unittest.TestCase):

    def setUp(self):
        driver_run = DriverRun()
        self.driver = driver_run.run_driver()
        self.driver.maximize_window()
        self.driver.get("https://instagram.com")
        instagramLoginPage = InstagramLoginPage(self.driver)
        instagramLoginPage.login()
        notificationsDialog = NotificationDialog(self.driver)
        notificationsDialog.notifications_skip()

    def test_script(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()