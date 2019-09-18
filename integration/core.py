import abc
import os

class PackageManager(abc.ABC):
    """Describes the operations a package manager can perform"""

    # TODO: Move to a config class?
    #       - Load config at start with defaults?
    config_name = None

    def getConfigs(self, path):
        # TODO: Better handling of file paths
        base_path = os.path.expanduser(path + self.config_name)

        files = []
        for r, _, f in os.walk(base_path):
            for file in f:
                files.append(os.path.join(r, file))

        return files

    @abc.abstractmethod
    def list(self):
        """Lists the packages currently installed on the system"""
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
