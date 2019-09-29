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
Or have you decided to "clean up" your installed packages only to be faced with
a wall of packages all of which might be important or relied on by some corner
of your system?

This kind of **clutter** makes your system feel much more **brittle**. If you
don't even know what you've got installed or why, you won't be able to replicate
it later if something goes wrong.

`mpm` solves these problems by allowing you to specify what packages you want
installed in static files, this makes what packages are installed on your system
**explicit**.

## Installation

Currently this project is in an alpha state while I test it. If you want to try
it out head over to the "Releases" tab and download the binary then place it in
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
# ~/.config/mpm/config.ini
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
each of these directories can contain many "Package List Files".

When `mpm` is run, it looks through each of these files and builds up a list of
packages that you want installed. These files are simply text files that contain
a newline separated list of package names with two extra features:
- Blanks and extra whitespace are ignored
- Anything after and including a `#` is ignored as a comment

For example, the following is a valid package list file:
```
# ~/.config/mpm/brew/main
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

To show the packages that would be installed/uninstalled:
```bash
mpm update --dry-run
```

To run the update
```bash
mpm update
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

## FAQ

### Why not just use Nix or Guix?

Nix and Guix are great projects, but they bring a little too much to the table
for me. What this project sets out to achieve is to make the existing systems I
already use slightly better rather than replace them entirely. This makes this
smaller system much more flexible and portable.

### Why not just use a bash script?

Originally this was a bash script but it wasn't very portable and was quite
confusing to read, even after attempting to simplify it. You can see it
[here](https://github.com/Akeboshiwind/dotfiles/blob/e3114c4573b5430df20a33bd2a6480e857ec8a52/bin/bin/update).

This project has many improvements:
- Multiple integrations
- Tests
- Portable
- Much simpler code
