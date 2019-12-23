import re, json
from integration import core

class Nix(core.PackageManager):

    config_name = "nix"

    def list(self):
        out = self.run("nix-env --query --installed --json".split())

        # Filter out 'nix' and 'nss-cacert'?
        pkgs = json.loads(out.stdout).values()
        pkgs = set(map(lambda p: p['pname'], pkgs))

        return pkgs

    def leaves(self):
        out = self.run("nix-env --query --installed --json".split())

        # Filter out 'nix' and 'nss-cacert'?
        pkgs = json.loads(out.stdout).values()
        pkgs = set(map(lambda p: p['pname'], pkgs))

        return pkgs

    def list_non_updatable(self):
        return set()

    def install(self, pkgs):
        if type(pkgs) is not list:
            pkgs = [pkgs]

        if len(pkgs) > 0:
            out = self.run("nix-env --install".split() + pkgs, env=env)

            return out.returncode == 0
        else:
            return False

    def uninstall(self, pkgs):
        if type(pkgs) is not list:
            pkgs = [pkgs]

        if len(pkgs) > 0:
            out = self.run("nix-env --uninstall".split() + pkgs)
            return out.returncode == 0
        else:
            return True

    def upgrade(self, pkgs=[]):
        if type(pkgs) is not list:
            pkgs = [pkgs]

        if len(pkgs) > 0:
            out = self.run("nix-env --upgrade".split() + pkgs)
            return out.returncode == 0
        else:
            return True

    def update(self):
        out = self.run("nix-channel --update".split())
        return out.returncode == 0
