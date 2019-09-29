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

### Full example

Let's say you're using the above `config.ini` and have a set of packages you
want to install. You might create a couple of files like so:

```
# ~/.config/mpm/pkgs/brew/main
# Command line tools
bash
git
coreutils
jq
```

```
# ~/.config/mpm/pkgs/brew/python
# Command line
python3
pip3
```

```
# ~/.config/mpm/pkgs/cask/main
java
emacs
docker
```

```
# ~/.config/mpm/pkgs/cask/entertainment
spotify
minecraft
twitch
```

The current state of the `~/.config/mpm` directory should be:

```bash
$ tree ~/.config/mpm
/home/ake/.config/mpm
├── config.ini
└── pkgs
    ├── brew
    │   ├── main
    │   └── python
    └── cask
        ├── entertainment
        └── main

3 directories, 5 files
```

Let's see what would happen if we ran the update command:

```bash
$ mpm update --dry-run
[brew] update
brew updated
[brew] install new packages
The following brew packages will be installed
[bash, git, coreutils, jq, python3, pip3]
[brew] uninstall old packages
The following brew packages will be uninstalled
[vim]
[brew] update packages
The following brew packages will be upgraded
TODO
[cask] update
cask updated
[cask] install new packages
The following cask packages will be installed
[java, emacs, minecraft, twitch]
[cask] uninstall old packages
The following cask packages will be uninstalled
[]
[cask] update packages
The following cask packages will be upgraded
TODO
```

It looks like `vim` would be uninstalled if we ran update and the other packages
we listed will be installed.

If you decided you don't plan on using python on your system anymore you can
simply delete the `~/.config/mpm/pkgs/brew/python` file and then run the update
command.

## FAQ

### Why not just use Nix or Guix?

For two reasons:
1. They don't allow me to just list the packages I want to install in clearly
   marked files
2. They are much more than just package managers

Nix and Guix are great projects, but they bring a little too much to the table
for me. `mpm` aims to be flexible enough to run on different systems easily, but
without too much mental overhead.

### Why not just use a bash script?

Originally this was a bash script but it wasn't very portable and was quite
confusing to read, even after attempting to simplify it. You can see it
[here](https://github.com/Akeboshiwind/dotfiles/blob/e3114c4573b5430df20a33bd2a6480e857ec8a52/bin/bin/update).

This project has many improvements:
- Support for multiple integrations
- Portable
- Much simpler code
- Tests
