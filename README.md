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

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    gtest/1.8.0@lasote/stable

    [options]
    gtest:shared=true # false
    gtest:include_pdbs=false # MSVC - include debug symbols
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
