import unittest
from src.tests.test_BaseUIScript import BaseUIScript
from src.pages.instagram.feed_page import Post


class GetPostsScript(BaseUIScript):

    def test_a(self):
        post = Post(self.driver)
        post.open_inst_account()


if __name__ == "__main__":
    unittest.main()
