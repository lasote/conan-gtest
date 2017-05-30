from conans import ConanFile, tools, CMake
from conans.util import files
import os



class GTestConan(ConanFile):
    name = "gtest"
    version = "1.8.0"
    ZIP_FOLDER_NAME = "googletest-release-%s" % version
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "include_pdbs": [True, False], "cygwin_msvc": [True, False],
               "no_gmock": [True, False], "no_main": [True, False], "fpic": [True, False]}
    default_options = ("shared=True", "include_pdbs=False", "cygwin_msvc=False",
                       "no_gmock=False", "no_main=False", "fpic=False")
    exports = "CMakeLists.txt"
    url="http://github.com/lasote/conan-gtest"
    license="https://github.com/google/googletest/blob/master/googletest/LICENSE"

    def config_options(self):
        if self.settings.compiler != "Visual Studio":
            try:  # It might have already been removed if required by more than 1 package
                del self.options.include_pdbs
            except Exception:
                pass

    def source(self):
        zip_name = "release-%s.zip" % self.version
        url = "https://github.com/google/googletest/archive/%s" % zip_name
        tools.download(url, zip_name)
        tools.unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        files.mkdir("_build")
        with tools.chdir("_build"):
            cmake = CMake(self)
            cmake.definitions["gtest_force_shared_crt"] = "ON"
            if self.options.shared:
                cmake.definitions["BUILD_SHARED_LIBS"] = "1"
            if self.options.fpic:
                cmake.definitions["CMAKE_POSITION_INDEPENDENT_CODE"] = "ON"

            cmake.definitions["BUILD_GTEST"] = "ON" if self.options.no_gmock else "OFF"
            cmake.definitions["BUILD_GMOCK"] = "OFF" if self.options.no_gmock else "ON"

            cmake.configure(build_dir=".")
            cmake.build(build_dir=".")

    def package(self):
        # Copying headers
        self.copy(pattern="*.h", dst="include", src="%s/googletest/include" % self.ZIP_FOLDER_NAME, keep_path=True)
        if not self.options.no_gmock:
            self.copy(pattern="*.h", dst="include", src="%s/googlemock/include" % self.ZIP_FOLDER_NAME, keep_path=True)

        # Copying static and dynamic libs
        self.copy(pattern="*.a", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src=".", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dylib*", dst="lib", src=".", keep_path=False)

        # Copying debug symbols
        if self.settings.compiler == "Visual Studio" and self.options.include_pdbs:
            self.copy(pattern="*.pdb", dst="lib", src=".", keep_path=False)

    def package_info(self):
        # See https://github.com/google/googletest/issues/1015 for which
        # libraries should be used when gtest/gmock are built with CMake.
        if self.options.no_gmock:
            if self.options.no_main:
                self.cpp_info.libs = ["gtest"]
            else:
                self.cpp_info.libs = ["gtest", "gtest_main"]
        else:
            if self.options.no_main:
                self.cpp_info.libs = ["gmock"]
            else:
                self.cpp_info.libs = ["gmock_main"]

        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")

        if self.options.shared:
            self.cpp_info.defines.append("GTEST_LINKED_AS_SHARED_LIBRARY=1")
