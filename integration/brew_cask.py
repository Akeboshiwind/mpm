from integration import core
import subprocess

class BrewCask(core.PackageManager):

    config_name = "cask"

    def list(self):
        myOut = subprocess.Popen("brew cask ls --full-name".split(),
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        stdout, _ = myOut.communicate()

        pkgs = stdout.decode("utf-8").split('\n')
        pkgs = set(filter(lambda p: p != '',pkgs))

        return pkgs

    def install(self, pkgs):
        if type(pkgs) is not list:
            pkgs = [pkgs]
        out = subprocess.call("brew cask install".split() + pkgs,
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)
        return out == 0

    def uninstall(self, pkgs):
        if type(pkgs) is not list:
            pkgs = [pkgs]
        out = subprocess.call("brew cask uninstall".split() + pkgs,
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)
        return out == 0

    def upgrade(self, pkgs=[]):
        if type(pkgs) is not list:
            pkgs = [pkgs]
        out = subprocess.call("brew cask upgrade".split() + pkgs,
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)

    def update(self):
        out = subprocess.call("brew cask update".split(),
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)
        return out == 0
