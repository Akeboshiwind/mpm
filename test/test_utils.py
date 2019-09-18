from unittest import TestCase
import utils

class TestConcatPaths(TestCase):

    def test_no_trailing_or_leading_slashes(self):
        self.assertEqual(utils.concatPaths("/test/pth",
                                           "rest/of/path"),
                         "/test/pth/rest/of/path")

    def test_trailing_slash(self):
        self.assertEqual(utils.concatPaths("/test/pth/",
                                           "rest/of/path"),
                         "/test/pth/rest/of/path")

    def test_leading_slash(self):
        self.assertEqual(utils.concatPaths("/test/pth",
                                           "/rest/of/path"),
                         "/test/pth/rest/of/path")

    def test_trailing_and_leading_slash(self):
        self.assertEqual(utils.concatPaths("/test/pth/",
                                           "/rest/of/path"),
                         "/test/pth/rest/of/path")
