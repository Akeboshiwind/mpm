# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.0] - 2010-02-03
### Added
- List command

## [0.4.0] - 2019-12-24
### Added
- Support for Nix

### Changed
- Stop cask auto updating homebrew
- Stop and exit the `update` command if any of the stages fail

### Fixed
- Print the 'updated' message after the manager has updated
- Fix a bug where false would be returned if no packages were installed


## [0.3.0] - 2019-12-22
### Added
- A better README with motivation, FAQ, etc
- A `--update-all` option to update all packages with the `update` command

### Changed
- Run `--help` instead of the `version` subcommand if no arguments are set
- Restructure the tests
- Streamline the config loading code to be a bit clearer

### Fixed
- Disable brew auto-update on `brew install` (we already do that at the start)
- Don't update brew cask packages that have version set to `:latest`


## [0.2.0] - 2019-09-24
### Added
- Verbosity to update command

### Changed
- Fix cask using the wrong update command


## [0.1.0] - 2019-09-23
### Added
- Update command
- Brew integration
- Brew cask integration
- CLI

[0.5.0]: https://github.com/akeboshiwind/mpm/compare/0.4.0...0.5.0
[0.4.0]: https://github.com/akeboshiwind/mpm/compare/0.3.0...0.4.0
[0.3.0]: https://github.com/akeboshiwind/mpm/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/akeboshiwind/mpm/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/akeboshiwind/mpm/releases/tag/0.1.0
