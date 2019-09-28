# mpm

`mpm` is a file-based **m**eta **p**ackage **m**anager.

Use files with lists of packages to know **exactly** what's installed on your
system

## Motivation

Have you ever installed a package just to try it out then forget to uninstall it
later on, leaving it there to clutter up your system?

Have you taken hours to figure out the **exact** list of packages needed for a
program to work, then realise you can't remember what you even installed?

What about deciding to move to a different OS and forgotten what packages you
even had installed in the first place, then taken hours to figure it out?

Or have you decided to 'clean up' your installed packages only to be faced with
a wall of packages all of which might be important or relied on by some corner
of your system?

This kind of 'clutter' makes your system feel much more brittle. If you don't
even know what you've got installed or why, you won't be able to replicate it
later if something goes wrong.

`mpm` solves these problems by making what packages are installed on your system
**explicit**.

It does this by giving you a folder with files in it, each file is just a list
of packages you want installed on your system. By running `mpm update`, packages
in the list are installed and updated, packages that aren't are uninstalled.
It's as simple as that.

Now you know exactly what's installed on your system, but how can you tell why a
package is installed? Just add a comment explaining why! Grouping together
related packages into an individual file is quite useful too.

## Installation

Currently this project is in an alpha state while I test it. If you want to try
it out head over to the 'Releases' tab and download the binary then place it in
a `bin/` folder somewhere, e.g. `~/bin/`.

Or if you want to try an even more cutting edge version, clone the project
locally, have python3 and make installed then run:
```bash
make install
```
Which will build the binary then install it in `~/bin/`.

## Application Config

`mpm` is configured with an .ini file at `~/.config/mpm/config.ini` described
below:

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

## Package List Files

The `~/.config/mpm/pkgs` directory contains a folder for each package manager,
each of these directories can contain many 'Package List Files'.

When `mpm` is run, it looks through each of these files and builds up a list of
packages that you want installed. These files are simply text files that contain
a newline separated list of package names with two extra features:
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
