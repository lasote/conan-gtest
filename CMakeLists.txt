PROJECT(conangtest)

MESSAGE("Conan Gtest Wrapped CMake")
cmake_minimum_required(VERSION 2.8.12)
include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

if(WIN32)
   if(MSVC_VERSION)
       if(MSVC_VERSION GREATER_EQUAL 1910)
        add_definitions(-DGTEST_LANG_CXX11=1)
       endif()
   endif()
endif()

add_subdirectory("googletest-release-1.8.0")
