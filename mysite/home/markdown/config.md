<div class="page-header">
<h2>Configuration</h2>
</div>

In order to configure `Jeta`, you need to create `jeta.properties` file in the root package of the source set. It's a plain java properties file, with `key=value` format.
By default, `Jeta` is not allowed to get the path to the source directory, so you need to provide it by yourself. There are two common ways to do that. First one is to declare `sourcepath` option in your `build.gradle`:

### `build.gradle`

    :::groovy
    compileJava {
        options.sourcepath = files('src/main/java')
    }

The other way is available via `apt` arguments. Note that you need a plugin that supports this feature. If not, there are some hacks that might help you, but you need to google for it. If it's allowed, add next lines to the `build.gradle`:

    :::groovy
    apt {
        arguments {
            jetaProperties "$project.projectDir/src/main/java/jeta.properties"
        }
    }

### `jeta.properties`
Let's go through the options that available to config code generating. As already mentioned, in the previous article, the most needed property is `metasitory.package`. It must be unique for any module, e.g. test module. This package you will need to provide to `MapMetasitory` constructor at runtime to be able to use this metasitory. The other options are described below as comments:

    :::properties
    # Source directory path. Absolute or relative to `jeta.properties` path
    # to the source folder. Define it in case `jeta.properties` is not in the root
    # of the source set. (`.` by default)
    sourcepath=.

    # Unique per module java package, where metasitory will be stored.
    # (`` by default, recommended to define)
    metasitory.package=com.example

    # Set this to `true` to skip code re-generating in case the master's source code
    # hasn't been changed since the previous run. Boosts up code processing.
    # (`false` by default)
    utd.enable=true

    # Delete metacode if its master not exists anymore
    # (`true` by default if `utd` feature is enabled)
    utd.cleanup=true

    # Absolute or relative to `jeta.properties` path, where `utd` data is stored
    # ('java.io.tmpdir' by default, recommended to define)
    utd.dir=../../../build/jeta-utd-files

    # Output debug information (false by default)
    debug=true

    # Output the time metacode built in (true by default)
    debug.built_time=true

    # Output `utd` statuses information:
    #  `+` - metacode created or rewritten
    #  `-` - metacode removed (if `utd.cleanup` enabled)
    #  `*` - master is up-to-date
    # (`true` by default if `debug` and `utd` are enabled)
    debug.utd_states=true

    # Custome annotation processors (comma separated)
    # go to http://jeta.brooth.org/guide/custom-processor
    processors.add=com.example.apt.MyCustomProcessor

    # Disable a processor by its annotation (comma separated, reg-exp allowed)
    processors.disable=^Meta.*$,^Log$

    # Metacode file header
    file.comment=\n Use is subject to license terms. \n

    # Default scope for dependency injection
    # go to http://jeta.brooth.org/guide/inject
    inject.scope.default = org.brooth.jeta.tests.inject.DefaultScope

    # org.brooth.jeta.inject.Inject annotation alias.
    inject.alias=javax.inject.Inject

    # org.brooth.jeta.Provider alias
    inject.alias.provider=javax.inject.Provider

    # Custom metasitory writer
    # go to http://jeta.brooth.org/guide/custom-metasitory
    metasitory.writer=org.brooth.jeta.apt.EchoMetasitoryWriter

