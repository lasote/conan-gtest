[![Build Status](https://travis-ci.org/lasote/conan-gtest.svg)](https://travis-ci.org/lasote/conan-gtest)


# conan-gtest

[Conan.io](https://conan.io) package for Google test library

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/gtest/1.8.0/lasote/stable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload gtest/1.8.0@lasote/stable --all

## Reuse the packages

### Basic setup

    $ conan install gtest/1.8.0@lasote/stable

### Project setup

If you handle multiple dependencies in your project, it would be better to add a *conanfile.txt*

    [requires]
    gtest/1.8.0@lasote/stable

    [options]
    gtest:shared=False
    gtest:include_pdbs=false # MSVC - include debug symbols
    gtest:no_gmock=True # don't include Google Mock
    gtest:no_main=True # don't link with main() provided by gtest/gmock

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files `conanbuildinfo.txt` and `conanbuildinfo.cmake` with all the necessary paths and variables
needed to link with the other dependencies.

### Ubuntu 16.04 support

On Ubuntu and using `clang`, we have found that linking with this package may cause
the "undefined reference" issue if not linked to `libstdc++11` (see also
[#23](https://github.com/lasote/conan-gtest/issues/23)).

This is the recommended build command:

    $ conan install .. -s compiler=clang -s compiler.version=3.6 \
        -s compiler.libcxx=libstdc++11 --build=missing

Also, make sure to use the `gtest:shared=False` option, as shown above.
