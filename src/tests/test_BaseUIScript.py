import unittest
from src.pages.instagram.feed_page import Post
from src.pages.instagram.login_page import InstagramLoginPage
from src.pages.instagram.login_dialogs import NotificationDialog
from src.core.driver_run import DriverRun


class BaseUIScript(unittest.TestCase):

    def setUp(self):
        driver_run = DriverRun()
        self.driver = driver_run.run_driver()
        self.driver.maximize_window()
        instagramLoginPage = InstagramLoginPage(self.driver)
        instagramLoginPage.login()
        notificationsDialog = NotificationDialog(self.driver)
        notificationsDialog.notifications_skip()

    """def test_a(self):
        post = Post(self.driver)
        post.open_inst_account()"""

    def tearDown(self):
        self.driver.close()


