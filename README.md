# Machina: Personal Assistant for Employee Benefits

## Dependency
The package has been tested on macOS and Linux so far. Below is the dependency of the project,
 - Python 3
 - Boost.Python library
 - C/C++ compiler

## Installation
### 1. Install boost-python
#### Mac OS X
The recommended method to intall `boost-python` is through `Homebrew`
```bash
$ brew install boost-python3
```

### Potential Installation Issues
#### 1. `pyconfig.h` not found
find include path for python
```bash
$ export CPLUS_INCLUDE_PATH
```
