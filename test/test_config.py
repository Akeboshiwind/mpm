from unittest import TestCase
from unittest.mock import patch, mock_open
import config

class TestLoadConfig(TestCase):

    def test_read_default_config(self):
        test_file = ""
        expected = config.default_config

        with patch('builtins.open', mock_open(read_data=test_file)):
            output = config.loadConfig("foo")
            self.assertEqual(output._sections, expected)
            self.assertEqual(output["managers"]["order"], "")

    def test_alternate_manager_order(self):
        test_file = """[managers]
order=
    brew
    cask"""
        expected = config.default_config

        with patch('builtins.open', mock_open(read_data=test_file)):
            output = config.loadConfig("foo")
            self.assertEqual(output["managers"]["order"], "\nbrew\ncask")
