# Machina: Personal Assistant for Employee Benefits

## Dependency
 - Python 3
 - Boost.Python library
 - C/C++ compiler

## Installation

### Potential Installation Issues
#### 1. `pyconfig.h` not found
find include path for python
```bash
$ export CPLUS_INCLUDE_PATH
```
#### 2. `-lboost_python` not found
find `libboost_python.o`
ln -s for python3
