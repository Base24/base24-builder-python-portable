[![Github top language](https://img.shields.io/github/languages/top/Base24/base24-builder-python.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/[codacy-proj-id].svg?style=for-the-badge)](https://www.codacy.com/manual/Base24/base24-builder-python)
[![Repository size](https://img.shields.io/github/repo-size/Base24/base24-builder-python.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/Base24/base24-builder-python.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/Base24/base24-builder-python.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/Base24/base24-builder-python.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/Base24/base24-builder-python.svg?style=for-the-badge)](../../commits/master)

# base24-builder-python

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Portable version of base24-builder-python

Thank you to https://github.com/InspectorMustache/base16-builder-python (MIT)
for the original base16-builder

## Installation
As this project uses async/await syntax, the lowest supported Python version is 3.5.

1. copy dropin.py to template repository eg. base24-kdeplasma
2. run ```./dropin.py``` to download base24-builder-python-portable
3. then see Usage below:

## Usage
There are three modes of operation:

```bash
./base24.py update
./base24.py build
./base24.py inject
```


### Basic Usage

If you just want to build all base24 colorschemes and then pick out the ones you need, simply run:
```bash
./base24.py update
./base24.py build
```

Once the process is finished, you can find all colorschemes in a folder named output located in the current working directory.

For a more detailed explanation of the individual commands, read on.

### Update

Downloads all base24/ base16 schemes and templates to the current working directory.
The source files, i.e. the files pointing to the scheme and template repositories


will also be updated by default.  If you want to use your own versions of these
files (to exclude specific repositories, for example), you can prevent the builder
from updating the source files by using the `-c/--custom` option.

You can use `-v/--verbose` for more detailed output.

### Build

Builds base24 colorschemes for all schemes and templates.  This requires the directory structure and files created by the update operation to be present in the working directory.  This operation accepts four parameters:

- `-s/--scheme` restricts building to specific schemes

  Can be specified more than once.  Each argument must match a scheme.  Wildcards can be used but must be escaped properly so they are not expanded by the shell.

- `-o/--output` specifies a path where built colorschemes will be placed

  If this option is not specified, an "output" folder in the current working directory will be created and used.

- `-v/--verbose` increases verbosity

  With this option specified the builder prints out the name of each scheme as it's built.

Example:
```bash
./base24.py build -s atelier-heath-light -o /tmp/output
```

### Inject

This operation provides an easier way to quickly insert a specific colorscheme into one or more config files.  In order for the builder to locate the necessary files, this command relies on the folder structure created by the update command.  The command accepts two parameters:

- `-s/--scheme` specifies the scheme you wish to inject

  Refers to the scheme that should be inserted.  You can use wildcards and the same restrictions as with update apply.  A pattern that matches more than one scheme will cause an error.

- `-f/--file` specifies the file(s) into which you wish the scheme to be inserted

  Can be specified more than once.  Each argument must be specified as a path to a config file that features proper injection markers (see below).

You will need to prepare your configuration files so that the script knows where to insert the colorscheme.  This is done by including two lines in the file
```bash
# %%base24_template: TEMPLATE_NAME##SUBTEMPLATE_NAME %%

Everything in-between these two lines will be replaced with the colorscheme.

# %%base24_template_end%%
```

Both lines can feature arbitrary characters before the first two percentage signs.  This is so as to accomodate different commenting styles.  Both lines need to end exactly as demonstrated above, however.  "TEMPLATE_NAME" and "SUBTEMPLATE_NAME" are the exception to this.  Replace TEMPLATE_NAME with the name of the template you wish to insert, for example "gnome-terminal".  This must correspond to a folder in the templates directory.  Replace SUBTEMPLATE_NAME with the name of the subtemplate as it is defined at the top level of the template's config.yaml file (see `file.md <https://github.com/chriskempson/base16/blob/master/file.md>`_ for details), for example "default-256".  If you omit the subtemplate name (don't omit "##" though), "default" is assumed.





Specify the name of the scheme you wish to inject with the -s option.  Use the -f option for each file into which you want to inject the scheme.

As an example, here's the command I use to globally change the color scheme in all applications that support it:
```bash
./base24.py inject -s ocean -f ~/.gtkrc-2.0.mine -f ~/.config/dunst/dunstrc -f ~/.config/i3/config -f ~/.config/termite/config -f ~/.config/zathura/zathurarc
```

### Exit

The program exits with exit code 1 if it encountered a general error and with 2 if one or more build or update tasks produced a warning or an error.


## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.8.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.8
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.8 interpreter is selected (Ctrl+Shift+P > Python:Select Interpreter > Python 3.8)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```


## Changelog
See the [CHANGELOG](/CHANGELOG.md) for more information.


## Licence
MIT License
(See the [LICENSE](/LICENSE.md) for more information.)
