from unittest import TestCase
from unittest.mock import patch, mock_open
from integration import core

class MyTestImpl(core.PackageManager):

    config_name = "test"

    def list(self):
        pass

    def leaves(self):
        pass

    def list_non_updatable(self):
        pass

    def install(self):
        pass

    def uninstall(self):
        pass

    def upgrade(self):
        pass

    def update(self):
        pass



class TestCore(TestCase):

    def test_can_instantiate(self):
        output = MyTestImpl(0)
