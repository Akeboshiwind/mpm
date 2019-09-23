import os
from configparser import ConfigParser
import utils

base_path = "~/.config/mpm"
config_file_path = utils.concatPaths(base_path, "config.ini")

default_config = {"paths": {"base_path": base_path,
                            "pkg_path": "pkgs"},
                  "managers": {"order": ""}}

def loadConfig(config_path):
    cfg = ConfigParser()

    # Load defaults
    cfg.read_dict(default_config)

    cfg.read(os.path.expanduser(config_path))

    return cfg
