# Machina: Personal Assistant for Employee Benefits

## Dependency
The package has been tested on macOS and Linux so far. Below is the dependency of the project,
 - Python 3
 - Boost.Python library
 - C/C++ compiler

## Installation
### Mac OS X
#### 1. Install boost-python
The recommended method to intall `boost-python` is through `Homebrew`
```bash
$ brew install boost-python3
```
#### 2. Install Machina
```bash
$ python setup install
```
The command should build the binary file from c++ code, and the link it to python.

### Potential Installation Issues
#### 1. `pyconfig.h` not found
find include path for python
```bash
$ export CPLUS_INCLUDE_PATH
```
