from functools import reduce
from integration import managers
import utils

def command(args, cfg):
    manager_order = cfg['managers']['order'].splitlines()
    manager_order = [s for s in manager_order if s]

    pkg_path = utils.concatPaths(cfg['paths']['base_path'],
                                 cfg['paths']['pkg_path'])

    rows = []
    for integration in manager_order:

        print("[" + integration + "]")
        manager = managers[integration](False)

        # Get listed packages
        pkgs_by_config = manager.getPackagesByConfig(pkg_path)

        all_pkgs = set(reduce(lambda a, b: a + b, pkgs_by_config.values()))

        # Get the packages to be *installed*

        # Compare with the list of full packages because some of the requested
        # packages might be dependencies on others, so .leaves() would be wrong
        new_pkgs = all_pkgs.difference(manager.list())


        # Get the packages to be *uninstalled*

        # Compare with the packages that aren't dependencies (leaves) so that we
        # don't uninstall a required package
        old_pkgs = manager.leaves().difference(all_pkgs)


        # Print new packages
        print(" [new]")
        no_pkgs=True
        for cfg_path in sorted(pkgs_by_config.keys()):

            pkgs = set(pkgs_by_config[cfg_path])
            new_pkgs = pkgs.intersection(new_pkgs)

            if len(new_pkgs) != 0:
                print("  [" + cfg_path +  "]")
                for pkg in new_pkgs:
                    print("   " + pkg)
                no_pkgs=False
        if no_pkgs:
            print("  (none)")


        print()
        # Print existing packages
        print(" [existing]")
        no_pkgs=True
        for cfg_path in sorted(pkgs_by_config.keys()):

            pkgs = set(pkgs_by_config[cfg_path])
            existing_pkgs = pkgs.difference(new_pkgs.union(old_pkgs))

            if len(existing_pkgs) != 0:
                print("  [" + cfg_path +  "]")
                for pkg in existing_pkgs:
                    print("   " + pkg)
                no_pkgs=False
        if no_pkgs:
            print("  (none)")


        print()
        # Print new packages
        print(" [old]")
        no_pkgs=True
        for cfg_path in sorted(pkgs_by_config.keys()):

            pkgs = set(pkgs_by_config[cfg_path])
            old_pkgs = pkgs.intersection(old_pkgs)

            if len(old_pkgs) != 0:
                print("  [" + cfg_path +  "]")
                for pkg in old_pkgs:
                    print("   " + pkg)
                no_pkgs=False
        if no_pkgs:
            print("  (none)")

        print()
