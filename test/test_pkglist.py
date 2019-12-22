from unittest import TestCase
from unittest.mock import patch, mock_open
import pkglist

class TestRemoveComments(TestCase):

    def test_no_comment(self):
        line = "pkg"
        output = pkglist.removeComments(line)
        self.assertEqual(output, line)

    def test_just_comment(self):
        line = "# my comment"
        output = pkglist.removeComments(line)
        self.assertEqual(output, "")

    def test_double_comment(self):
        line = "# my comment # and another"
        output = pkglist.removeComments(line)
        self.assertEqual(output, "")

    def test_pkg_and_comment(self):
        line = "pkg # my comment"
        output = pkglist.removeComments(line)
        self.assertEqual(output, "pkg")

class TestParseConfig(TestCase):

    def test_single_package(self):
        test_file = "pkg"
        expected = ["pkg"]

        with patch('builtins.open', mock_open(read_data=test_file)):
            output = pkglist.parsePkgList("foo")
            self.assertEqual(output, expected)

    def test_multiple_packages(self):
        test_file = "pkg\npkg2\npkg3"
        expected = ["pkg", "pkg2", "pkg3"]

        with patch('builtins.open', mock_open(read_data=test_file)):
            output = pkglist.parsePkgList("foo")
            self.assertEqual(output, expected)

    def test_single_package_with_comment(self):
        test_file = "pkg # test comment"
        expected = ["pkg"]

        with patch('builtins.open', mock_open(read_data=test_file)):
            output = pkglist.parsePkgList("foo")
            self.assertEqual(output, expected)

    def test_blank_line(self):
        test_file = "pkg\n\npkg2"
        expected = ["pkg", "pkg2"]

        with patch('builtins.open', mock_open(read_data=test_file)):
            output = pkglist.parsePkgList("foo")
            self.assertEqual(output, expected)

    def test_multiple_packages_multiple_comments(self):
        test_file = "pkg # test comment\npkg2 #with another comment\n# no package, just comment"
        expected = ["pkg", "pkg2"]

        with patch('builtins.open', mock_open(read_data=test_file)):
            output = pkglist.parsePkgList("foo")
            self.assertEqual(output, expected)

    def test_extra_spaces(self):
        test_file = "   pkg   \n  pkg2"
        expected = ["pkg", "pkg2"]

        with patch('builtins.open', mock_open(read_data=test_file)):
            output = pkglist.parsePkgList("foo")
            self.assertEqual(output, expected)

    def test_just_comment(self):
        test_file = "# test comment"
        expected = []

        with patch('builtins.open', mock_open(read_data=test_file)):
            output = pkglist.parsePkgList("foo")
            self.assertEqual(output, expected)
