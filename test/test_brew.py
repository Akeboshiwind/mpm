from unittest import TestCase, skipIf
from integration import brew

import subprocess
from shutil import which



pkg1 = "afio"
pkg2 = "afflib"



@skipIf(which("brew") == None, "Brew not installed")
class TestBrewList(TestCase):

    def setUp(self):
        self.mgr = brew.Brew()

    def test_list_returns_some_packages(self):
        pkgs = self.mgr.list()
        self.assertGreater(len(pkgs), 0)



@skipIf(which("brew") == None, "Brew not installed")
class TestBrewInstall(TestCase):

    def setUp(self):
        self.mgr = brew.Brew()
        subprocess.call("brew uninstall".split() + [pkg1, pkg2],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)

    @classmethod
    def tearDownClass(cls):
        subprocess.call("brew uninstall".split() + [pkg1, pkg2],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)

    def test_install_a_package(self):
        out = self.mgr.install([pkg1])
        self.assertTrue(out)

    def test_install_multiple_packages(self):
        out = self.mgr.install([pkg1, pkg2])
        self.assertTrue(out)

    def test_install_fail_to_install(self):
        out = self.mgr.install(["not-a-real-pkg"])
        self.assertFalse(out)

    def test_install_a_package_twice(self):
        out = self.mgr.install([pkg1])
        self.assertTrue(out)

        out = self.mgr.install([pkg1])
        self.assertFalse(out)



@skipIf(which("brew") == None, "Brew not installed")
class TestBrewUninstall(TestCase):

    def setUp(self):
        self.mgr = brew.Brew()
        subprocess.call("brew install".split() + [pkg1, pkg2],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)

    @classmethod
    def tearDownClass(cls):
        subprocess.call("brew uninstall".split() + [pkg1, pkg2],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)

    def test_uninstall_a_package(self):
        out = self.mgr.uninstall([pkg1])
        self.assertTrue(out)

    def test_uninstall_multiple_packages(self):
        out = self.mgr.uninstall([pkg1, pkg2])
        self.assertTrue(out)

    def test_uninstall_fail_to_unintall(self):
        out = self.mgr.uninstall(["not-a-reap-pkg"])
        self.assertFalse(out)

    def test_uninstall_a_package_twice(self):
        out = self.mgr.uninstall([pkg1])
        self.assertTrue(out)

        out = self.mgr.uninstall([pkg1])
        self.assertFalse(out)



@skipIf(which("brew") == None, "Brew not installed")
class TestBrewUpdate(TestCase):

    def test_update(self):
        pass

if __name__ == '__main__':
    unittest.main()
