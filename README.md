# pkg-mgr

A file-based meta package manager.

The goals of this project are as follows:
- Have a set of files which describes the desired packages to be installed on the system
- Have a single command which:
  - Reads the current state of the system
  - Uninstalles packages that aren't listed
  - Installs packages that aren't installed

