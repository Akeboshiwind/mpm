import abc
import os
import utils

class PackageManager(abc.ABC):
    """Describes the operations a package manager can perform"""

    # TODO: Move to a config class?
    #       - Load config at start with defaults?
    config_name = None
    verbosity = 0

    def __init__(self, verbosity):
        self.verbosity = verbosity

    def getConfigs(self, path):
        base_path = utils.concatPaths(path, self.config_name)
        base_path = os.path.expanduser(base_path)

        files = []
        for r, _, f in os.walk(base_path):
            for file in f:
                files.append(os.path.join(r, file))

        return files

    @abc.abstractmethod
    def list(self):
        """Lists all the packages currently installed through the integration"""
        pass

    @abc.abstractmethod
    def leaves(self):
        """Lists the packages currently installed through the integration that aren't dependencies of any other package"""
        pass

    @abc.abstractmethod
    def install(self, pkgs):
        """Installs a list of packages"""
        pass

    @abc.abstractmethod
    def uninstall(self, pkgs):
        """Uninstalls a list of packages"""
        pass

    @abc.abstractmethod
    def upgrade(self, pkgs=[]):
        """Upgrade a list of packages, or if no list is given all installed packages"""
        pass

    @abc.abstractmethod
    def update(self):
        """Updates the package manager's list of available packages and versions"""
        pass
