PROJECT(MyHello)
cmake_minimum_required(VERSION 3.0)

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

ADD_EXECUTABLE(mytest test.cpp)
TARGET_LINK_LIBRARIES(mytest ${CONAN_LIBS})
