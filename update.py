from integration import brew, brew_cask
import config

if __name__ == "__main__":

    # TODO: Parse arguments

    mgrs = [brew.Brew(), brew_cask.BrewCask()]
    for mgr in mgrs:

        pkgs = set()
        for c in mgr.getConfigs():
            pkgs = pkgs.union(set(config.parseConfig(c)))

        print("[" + mgr.config_name + "] update")
        mgr.update()

        print("[" + mgr.config_name + "] install new packages")
        new_pkgs = pkgs.difference(mgr.list())
        print(new_pkgs)
        mgr.install(list(new_pkgs))

        print("[" + mgr.config_name + "] uninstall old packages")
        old_pkgs = mgr.list().difference(pkgs)
        print(old_pkgs)
        mgr.uninstall(list(old_pkgs))

        print("[" + mgr.config_name + "] update packages")
        mgr.upgrade(list(pkgs))
