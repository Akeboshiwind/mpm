import os
from configparser import ConfigParser

default_config = {"paths": {"base_path": "~/.config/mpm",
                            "pkg_path": "pkgs"},
                  "managers": {"order": ""}}

def loadConfig(config_path):
    cfg = ConfigParser()

    # Load defaults
    cfg.read_dict(default_config)

    cfg.read(os.path.expanduser(config_path))

    return cfg
