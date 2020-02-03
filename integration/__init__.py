from integration import brew, brew_cask, nix

managers = {"brew": brew.Brew,
            "cask": brew_cask.BrewCask,
            "nix": nix.Nix}
