# mpm

`mpm` is a file-based *m*eta *p*ackage *m*anager.

The goals of this project are as follows:
- Have a set of files which describes the desired packages to be installed on the system
- Have an update command which:
  - Reads the current state of the system
  - Uninstalles packages that aren't listed
  - Installs packages that aren't installed

## Installation

Currently this project is in an alpha state while I test it. If you want to try it out head over to the 'Releases' tab and download the binary then place it in a `bin/` folder somewhere, e.g. `~/bin/`.

Or if you want to try an even more cutting edge version, clone the project locally, have python3 and make installed then run:
```bash
make install
```
Which will build the binary then install it in `~/bin/`.

## Config

`mpm` is configured with an .ini file at `~/.config/mpm/` described below:

```ini
[paths]
# The folder to store the package files in
pkg_path=pkgs

[managers]
# The order to execute the package managers in
# managers not listed are not executed.
# (A newline separated list, the indentation is important)
order=
    brew
    cask
```

`mpm` uses files to figure out what packages should be installed. If the default
`pkg_path` setting is used, these 'package list files' are stored a folder
respective to the package manager you want to install the packages with.

For example, for `brew` the package list files should be put in a folder
`~/.config/pkgs/brew/`.

Package list files are simply newline separated files listing the packages you
want installed on the system with two extra features:
- Blanks and extra whitespace are ignored
- Anything after and including a `#` is ignored as a comment

For example, the following is a valid package list file:
```
# Command line tools:
bash
coreutils
git
jq # Super useful

# Programming languages
## Python
python3
pip3
## Clojure
clojure
leiningen
java # Should switch to using asdf
```

## Usage

### Update

The update command performs 4 operations in the following order for each of the
specified managers in the config:

1. Update the package manager's listing of packages
2. Install packages that aren't currently installed on the system but are listed
3. Uninstall packages that are installed on the system but aren't listed
4. Update the installed packages

To run the update
```bash
mpm update
```

To show the packages that would be installed/uninstalled:
```bash
mpm update --dry-run
```

### General Advice

The recommended usage is to group together packages that are related into a
single file. For example, you could group together the packages you need for a
language you're developing with, of the packages you need for get an application
working how you like it.

E.g.
```
# pkgs/brew/zsh
# Main packages
zsh
zsh-syntax-highlighting

# Addons
fzf
```

```
# pkgs/brew/jupyter-clj
jupyter
clojure
runit
```

## TODO

- [ ] Documentation
  - [x] Name
  - [x] Readme
  - [x] Usage instructions
  - [ ] `man` page
  - [x] Config files
- [ ] Installation
  - [x] Makefile
  - [ ] Script release (and upload of binary)
  - [ ] Bash and Zsh completions
- [ ] Re-do testing
  - [ ] Simplify? (should run quickly, just verify that the commands work?)
  - [ ] Test output types of commands?
- [ ] Version fixing for packages
- [ ] Only update packages which have updates avaliable
- [ ] Install only command?
