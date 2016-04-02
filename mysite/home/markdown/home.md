`Jeta` - is an Open Source framework, built on the top of `javax.annotation.processing`, that brings metaprogramming into your Java project. It aims to reduce boilerplate and increase errors detection at compile-time.

Metaprogramming is achieved by code generating which makes programs fast and stable at runtime. The main goal is to ensure that if the metacode is compiled it will work correctly. On the other hand, `Jeta` was designed to provide rapid code.

So if you are dissatisfied with `Java Reflection`, welcome to aboard :)

<div class="alert alert-success" role="alert">
For android developers, <a href="https://github.com/brooth/androjeta">Androjeta</a> is the better way to go.
</div>

At a glance:
--------
`Jeta` provides a number of useful annotations that might help your to develop java programs quicker and safer. Let's take a look on a simple example:

### @Log
Named loggers can be supplied into your classes using `Log` annotation. By default, the logger has a name of the host (master) class:

    :::java
    class LogSample {
        @Log
        Logger logger;
    }

instead of:

    :::java
    class LogSample {
        private static final Logger logger = LoggerFactory.getLogger(LogSample.class);
    }

The second approach instigates copy-paste. It's often forgotten to replace the class name, so loggers might have incorrect names. The first code snippet doesn't cause any issues and `logger` has a name `LogSample` as you expect.

Refer to the [user's guide](/guide) to find more features.

Installation (gradle):
----------------------

    :::groovy
    repositories {
        jcenter()
    }

    dependencies {
        apt 'org.brooth.jeta:jeta-apt:1.0'
        compile 'org.brooth.jeta:jeta:1.0'
    }

<span class="label label-info">Note</span> Jeta is an annotation processing tool, so you need an `apt` plugin either:
[gradle apt plugins](https://plugins.gradle.org/search?term=apt)

License
-------

    Copyright 2015 Oleg Khalidov

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

