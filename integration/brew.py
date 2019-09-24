import subprocess

from integration import core

class Brew(core.PackageManager):

    config_name = "brew"

    def list(self):
        myOut = self.Popen("brew list --full-name".split(),
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
        stdout, _ = myOut.communicate()

        pkgs = stdout.decode("utf-8").split('\n')
        pkgs = set(filter(lambda p: p != '',pkgs))

        return pkgs

    def leaves(self):
        myOut = self.Popen("brew leaves".split(),
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
        stdout, _ = myOut.communicate()

        pkgs = stdout.decode("utf-8").split('\n')
        pkgs = set(filter(lambda p: p != '',pkgs))

        return pkgs

    def install(self, pkgs):
        if type(pkgs) is not list:
            pkgs = [pkgs]

        if len(pkgs) > 0:
            out = self.call("brew install".split() + pkgs)
            return out == 0
        else:
            return True

    def uninstall(self, pkgs):
        if type(pkgs) is not list:
            pkgs = [pkgs]

        if len(pkgs) > 0:
            out = self.call("brew uninstall".split() + pkgs)
            return out == 0
        else:
            return True

    def upgrade(self, pkgs=[]):
        if type(pkgs) is not list:
            pkgs = [pkgs]

        if len(pkgs) > 0:
            out = self.call("brew upgrade".split() + pkgs)
            return out == 0
        else:
            return True

    def update(self):
        out = self.call("brew update".split())
        return out == 0
