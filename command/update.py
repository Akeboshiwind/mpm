from integration import brew, brew_cask
from pkglist import parsePkgList
import utils

managers = {"brew": brew.Brew,
            "cask": brew_cask.BrewCask}

def command(args, cfg):
    manager_order = cfg['managers']['order'].splitlines()
    manager_order = [s for s in manager_order if s]

    pkg_path = utils.concatPaths(cfg['paths']['base_path'],
                                 cfg['paths']['pkg_path'])

    for integration in manager_order:

        manager = managers[integration](args.verbose)

        # Get a list of packages
        pkgs = set()
        for c in manager.getConfigs(pkg_path):
            pkgs = pkgs.union(set(parsePkgList(c)))

        # Update the manager
        print("[" + manager.config_name + "] update")

        if args.verbose >= 1 or args.dry_run:
            print(manager.config_name + " updated")

        if not(args.dry_run):
            manager.update()

        # Install new packages
        print("[" + manager.config_name + "] install new packages")

        # Compare with the list of full packages because some of the requested
        # packages might be dependencies on others, so .leaves() would be wrong
        new_pkgs = pkgs.difference(manager.list())

        if args.verbose >= 1 or args.dry_run:
            print("The following " + manager.config_name + " packages will be installed")
            print(list(new_pkgs))

        if not(args.dry_run):
            manager.install(list(new_pkgs))

        # Uninstall old packages
        print("[" + manager.config_name + "] uninstall old packages")

        # Compare with the packages that aren't dependencies (leaves) so that we
        # don't uninstall a required package
        old_pkgs = manager.leaves().difference(pkgs)

        if args.verbose >= 1 or args.dry_run:
            print("The following " + manager.config_name + " packages will be uninstalled")
            print(list(old_pkgs))

        if not(args.dry_run):
            manager.uninstall(list(old_pkgs))

        # Update installed packages
        print("[" + manager.config_name + "] update packages")

        if args.verbose >= 1 or args.dry_run:
            print("The following " + manager.config_name + " packages will be upgraded")
            print("TODO")

        if not(args.dry_run):
            manager.upgrade(list(pkgs))
