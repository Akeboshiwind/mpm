import os, sys, argparse

from command import update, list
from config import loadConfig

if __name__ == "__main__":
    # Load Config
    config_file_path = "~/.config/pkg-mgr/config.ini"
    cfg = loadConfig(config_file_path)


    # Load arguments
    ## Top level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    ## Update subcommand
    parser_update = subparsers.add_parser("update", help="update packages (default)")
    parser_update.add_argument("--dry-run", help="Just list the packages, don't actually run any commands", action="store_true")
    parser_update.set_defaults(func=update.command)

    ## List subcommand
    parser_list = subparsers.add_parser("list", help="list packages")
    parser_list.add_argument("--dry-run", help="Just list the packages, don't actually run any commands", action="store_true")
    parser_list.set_defaults(func=list.command)


    # Default to the 'update' command
    if len(sys.argv) < 2:
        args = parser.parse_args(['update'])
    else:
        args = parser.parse_args(sys.argv[1:])


    args.func(args, cfg)
