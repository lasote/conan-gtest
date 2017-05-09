from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="gtest:shared", pure_c=False)
    filtered_builds = []
    for settings, options, env_vars, build_requires in builder.builds:
        if settings["compiler"] == "Visual Studio":
            pdbOptions = options.copy()
            pdbOptions.update({"gtest:include_pdbs": "True"})
            filtered_builds.append([settings, pdbOptions, env_vars, build_requires])
        
        filtered_builds.append([settings, options, env_vars, build_requires])

    builder.builds = filtered_builds
    builder.run()

