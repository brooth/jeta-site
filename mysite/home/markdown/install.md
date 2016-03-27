<div class="page-header">
  <h2>Installation</h2>
</div>

In this guide we'll see how to install `Jeta` into a project using `gradle` build system. Currently, `jCenter` repository is the way to provide the artifacts. It might be available on `maven` repository in a future release.

Add next lines to your `build.gradle`:

    :::groovy
    repositories {
        jcenter()
    }
    dependencies {
        apt 'org.brooth.androjeta:androjeta-apt:1.0'
        compile 'org.brooth.androjeta:androjeta:1.0'
    }


In order to use `apt`, you need to install an appropriate pluging as well. Follow to [grale apt plugins](https://plugins.gradle.org/search?term=apt) page to know about the options. For this example let's choose `net.ltgt.apt`:

    :::groovy
    buildscript {
        repositories {
            maven {
                url 'https://plugins.gradle.org/m2/'
            }
        }
        dependencies {
            classpath 'net.ltgt.gradle:gradle-apt-plugin:0.5'
        }
    }

    apply plugin: 'net.ltgt.apt'



### jeta.properties
As the next step it's recomended to create `jeta.properties` file to be able to config code generation behavior. This file should be located in the root package of the source set. Complete configuration guide is on [this page](/guide/config). At the installation stage to provide `metasitory.package` is enough:

    :::properties
    metasitory.package=com.example


`metasitory.package` has to be unique in any module. In this package the metasitory file is generated. Follow [this guide](/guide/at-runtime) to get information about what the metasitory is.

To allow `jeta.properties` be found by `Jeta` one extra step is needed. In case you put this file in the root package, you can provide the `sourcepath` by adding next snippet to the `build.gradle`:

    :::groovy
    compileJava {
        options.sourcepath = files('src/main/java')
    }

For a reason `gradle` doesn't provide it by itself. Another available option - `jetaProperties` apt argument. Some of the plugins support the providing of these arguments (`net.ltgt.apt` currenty doesn't)

    :::groovy
    apt {
        arguments {
                jetaProperties "$project.projectDir/src/main/java/jeta.properties"
        }
    }

<div class="alert alert-info" role="alert">
For android projects <a href="https://bitbucket.org/hvisser/android-apt">android-apt plugin by Hugo Visser</a> is recomended.
</div>

Complete `build.gradle`:

    :::groovy
    buildscript {
        repositories {
            maven {
                url 'https://plugins.gradle.org/m2/'
            }
        }
        dependencies {
            classpath 'net.ltgt.gradle:gradle-apt-plugin:0.5'
        }
    }

    apply plugin: 'net.ltgt.apt'

    repositories {
        jcenter()
    }

    compileJava {
        options.sourcepath = files('src/main/java')
    }

    dependencies {
        apt 'org.brooth.androjeta:androjeta-apt:1.0'
        compile 'org.brooth.androjeta:androjeta:1.0'
    }

At this point you can start using `Jeta`, but properly configured it's better way to go. Refer to the [next guide](/guider/config) to find details.

