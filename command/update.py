import sys
from integration import managers
import utils

def command(args, cfg):
    manager_order = cfg['managers']['order'].splitlines()
    manager_order = [s for s in manager_order if s]

    pkg_path = utils.concatPaths(cfg['paths']['base_path'],
                                 cfg['paths']['pkg_path'])

    for integration in manager_order:

        manager = managers[integration](args.verbose)

        # Get a list of packages
        pkgs = manager.getPackages(pkg_path)

        # Update the manager
        print("[" + manager.config_name + "] update")

        if not(args.dry_run):
            if not manager.update():
                print(manager.config_name + " failed to update")
                sys.exit(1)

        if args.verbose >= 1 or args.dry_run:
            print(manager.config_name + " updated")

        # Install new packages
        print("[" + manager.config_name + "] install new packages")

        # Compare with the list of full packages because some of the requested
        # packages might be dependencies on others, so .leaves() would be wrong
        new_pkgs = pkgs.difference(manager.list())

        if args.verbose >= 1 or args.dry_run:
            print("The following " + manager.config_name + " packages will be installed")
            print(list(new_pkgs))

        if not(args.dry_run):
            if not manager.install(list(new_pkgs)):
                print("Failed to install packages for " + manager.config_name)
                sys.exit(1)

        # Uninstall old packages
        print("[" + manager.config_name + "] uninstall old packages")

        # Compare with the packages that aren't dependencies (leaves) so that we
        # don't uninstall a required package
        old_pkgs = manager.leaves().difference(pkgs)

        if args.verbose >= 1 or args.dry_run:
            print("The following " + manager.config_name + " packages will be uninstalled")
            print(list(old_pkgs))

        if not(args.dry_run):
            if not manager.uninstall(list(old_pkgs)):
                print("Failed to uninstall packages for " + manager.config_name)
                sys.exit(1)

        # Update installed packages
        print("[" + manager.config_name + "] update packages")

        if not args.update_all:
            # Don't update packages we can't know have latest versions
            non_updatable_pkgs = manager.list_non_updatable()
            updatable_pkgs = pkgs.difference(non_updatable_pkgs)
        else:
            updatable_pkgs = pkgs


        if args.verbose >= 1 or args.dry_run:
            print("The following " + manager.config_name + " packages will be upgraded")
            print(list(updatable_pkgs))

        if not(args.dry_run):
            if not manager.upgrade(list(updatable_pkgs)):
                print("Failed to upgrade packages for " + manager.config_name)
                sys.exit(1)
