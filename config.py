import os
from configparser import ConfigParser

default_config = {"paths": {"base_path": "~/.config/pkg-mgr",
                            "pkg_path": "pkgs"},
                  "managers": {"order": ""}}

def loadConfig(config_path):
    cfg = ConfigParser()

    cfg.read_dict(default_config)

    cfg.read(os.path.expanduser(config_path))

    return cfg
