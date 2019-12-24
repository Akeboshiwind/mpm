from unittest import TestCase, skipIf
from integration import nix

import subprocess
from shutil import which



pkg1 = "hello"
pkg2 = "vim"



@skipIf(which("nix-env") == None, "Nix not installed")
class TestNixList(TestCase):

    def setUp(self):
        self.mgr = nix.Nix(0)

    def test_list_returns_some_packages(self):
        pkgs = self.mgr.list()
        self.assertGreater(len(pkgs), 0)



@skipIf(which("nix-env") == None, "Nix not installed")
class TestNixInstall(TestCase):

    def setUp(self):
        self.mgr = nix.Nix(0)
        subprocess.run("nix-env --uninstall".split() + [pkg1], capture_output=True)
        subprocess.run("nix-env --uninstall".split() + [pkg2], capture_output=True)

    @classmethod
    def tearDownClass(cls):
        subprocess.run("nix-env --uninstall".split() + [pkg1], capture_output=True)
        subprocess.run("nix-env --uninstall".split() + [pkg2], capture_output=True)

    def test_install_a_package(self):
        out = self.mgr.install([pkg1])
        self.assertTrue(out)

    def test_install_no_packages(self):
        out = self.mgr.install([])
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



@skipIf(which("nix-env") == None, "Nix not installed")
class TestNixUninstall(TestCase):

    def setUp(self):
        self.mgr = nix.Nix(0)
        subprocess.run("nix-env --install".split() + [pkg1], capture_output=True)
        subprocess.run("nix-env --install".split() + [pkg2], capture_output=True)

    @classmethod
    def tearDownClass(cls):
        subprocess.run("nix-env --uninstall".split() + [pkg1], capture_output=True)
        subprocess.run("nix-env --uninstall".split() + [pkg2], capture_output=True)

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



@skipIf(which("nix-env") == None, "Nix not installed")
class TestNixUpdate(TestCase):

    def test_update(self):
        pass

if __name__ == '__main__':
    unittest.main()
