import os, sys, argparse

from command import update
from config import loadConfig, config_file_path

VERSION = '0.2.0'

if __name__ == "__main__":
    # Load Config
    cfg = loadConfig(config_file_path)


    # Load arguments
    ## Top level parser
    parser = argparse.ArgumentParser()

    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s '+VERSION)

    ## Subcommands
    subparsers = parser.add_subparsers()

    ### Update subcommand
    parser_update = subparsers.add_parser("update",
                                          help="update packages")
    parser_update.add_argument("--dry-run",
                               help="Just list the packages, don't actually run any commands",
                               action="store_true")
    parser_update.add_argument("--verbose", "-v",
                               action="count",
                               default=0,
                               help="The verbosity level")
    parser_update.add_argument("--update-all",
                               help="Include packages that we can't know if require an update",
                               action="store_true")
    parser_update.set_defaults(func=update.command)


    # Default to the 'update' command
    if len(sys.argv) < 2:
        args = parser.parse_args(['--help'])
    else:
        args = parser.parse_args(sys.argv[1:])


    args.func(args, cfg)
