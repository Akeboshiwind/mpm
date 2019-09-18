from integration import core
import subprocess

class Brew(core.PackageManager):

    config_name = "brew"

    def list(self):
        # TODO: Deal with error here
        myOut = subprocess.Popen("brew leaves".split(),
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        stdout, _ = myOut.communicate()

        pkgs = stdout.decode("utf-8").split('\n')
        pkgs = set(filter(lambda p: p != '',pkgs))

        return pkgs

    def install(self, pkgs):
        if type(pkgs) is not list:
            pkgs = [pkgs]
        out = subprocess.call("brew install".split() + pkgs)
        return out == 0

    def uninstall(self, pkgs):
        if type(pkgs) is not list:
            pkgs = [pkgs]
        out = subprocess.call("brew uninstall".split() + pkgs)
        return out == 0

    def upgrade(self, pkgs=[]):
        if type(pkgs) is not list:
            pkgs = [pkgs]
        out = subprocess.call("brew upgrade".split() + pkgs)
        return out == 0

    def update(self):
        out = subprocess.call("brew update".split())
        return out == 0
