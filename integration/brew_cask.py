import re
from integration import core

class BrewCask(core.PackageManager):

    config_name = "cask"

    def list(self):
        return self.leaves()

    def leaves(self):
        out = self.run("brew cask ls --full-name".split())

        pkgs = out.stdout.split('\n')
        pkgs = set(filter(lambda p: p != '',pkgs))

        return pkgs

    def list_non_updatable(self):
        out = self.run("brew cask ls --versions --full-name".split())

        pkgs = out.stdout.split('\n')
        pkgs = filter(lambda p: p != '',pkgs)
        pkgs = map(lambda p: p.split(),pkgs)
        pkgs = filter(lambda p: p[1] == "latest",pkgs)
        pkgs = map(lambda p: p[0],pkgs)
        pkgs = set(pkgs)

        return pkgs

    def install(self, pkgs):
        if type(pkgs) is not list:
            pkgs = [pkgs]

        if len(pkgs) > 0:
            out = self.run("brew cask install".split() + pkgs)
            if out.returncode == 0:
                # Test to see if the package was already installed
                return re.search(r'.*already installed.*', out.stderr) == None
            else:
                return False
        else:
            return True

    def uninstall(self, pkgs):
        if type(pkgs) is not list:
            pkgs = [pkgs]

        if len(pkgs) > 0:
            out = self.run("brew cask uninstall".split() + pkgs)
            return out.returncode == 0
        else:
            return True

    def upgrade(self, pkgs=[]):
        if type(pkgs) is not list:
            pkgs = [pkgs]

        if len(pkgs) > 0:
            out = self.run("brew cask upgrade".split() + pkgs)
            return out.returncode == 0
        else:
            return True

    def update(self):
        # Cask updates though brew
        out = self.run("brew update".split())
        return out.returncode == 0
