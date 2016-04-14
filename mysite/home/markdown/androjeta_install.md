<div class="page-header">
    <h2>Installation</h2>
</div>


*Androjeta* installation is similar to the [installation](/guide/install) of *Jeta*. But here it's recommended to use [android-apt plugin by Hugo Visser](https://bitbucket.org/hvisser/android-apt) as the plugin. Here is the complete listing:

    :::groovy
    buildscript {
        repositories {
            mavenCentral()
        }

        dependencies {
            classpath 'com.neenbedankt.gradle.plugins:android-apt:+'
        }
    }

    apply plugin: 'android-apt'

    repositories {
        jcenter()
    }

    apt {
        arguments {
            jetaProperties "$project.projectDir/src/main/java/jeta.properties"
        }
    }

    dependencies {
        apt 'org.brooth.androjeta:androjeta-apt:1.1'
        compile 'org.brooth.androjeta:androjeta:1.1'
    }


Go to the [configuration guide](/guide/config) to know about what `apt-arguments` is for.

