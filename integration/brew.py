import re, os
from integration import core

class Brew(core.PackageManager):

    config_name = "brew"

    def list(self):
        out = self.run("brew list --full-name".split())

        pkgs = out.stdout.split('\n')
        pkgs = set(filter(lambda p: p != '',pkgs))

        return pkgs

    def leaves(self):
        out = self.run("brew leaves".split())

        pkgs = out.stdout.split('\n')
        pkgs = set(filter(lambda p: p != '',pkgs))

        return pkgs

    def list_non_updatable(self):
        return set()

    def install(self, pkgs):
        if type(pkgs) is not list:
            pkgs = [pkgs]

        if len(pkgs) > 0:
            env = os.environ.copy()
            env["HOMEBREW_NO_AUTO_UPDATE"] = "1"
            out = self.run("brew install".split() + pkgs, env=env)

            if out.returncode == 0:
                # Test to see if the package was already installed
                return re.search(r'.*already installed.*', out.stderr) == None
            else:
                return False
        else:
            return False

    def uninstall(self, pkgs):
        if type(pkgs) is not list:
            pkgs = [pkgs]

        if len(pkgs) > 0:
            out = self.run("brew uninstall".split() + pkgs)
            return out.returncode == 0
        else:
            return True

    def upgrade(self, pkgs=[]):
        if type(pkgs) is not list:
            pkgs = [pkgs]

        if len(pkgs) > 0:
            out = self.run("brew upgrade".split() + pkgs)
            return out.returncode == 0
        else:
            return True

    def update(self):
        out = self.run("brew update".split())
        return out.returncode == 0
