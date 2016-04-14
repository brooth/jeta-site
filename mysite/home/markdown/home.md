*Jeta* - is an Open Source framework, built on the top of `javax.annotation.processing`, that brings metaprogramming into *Java* project. It aims to reduce boilerplate code and increase errors detection at compile-time.

Metaprogramming is achieved by code generating which makes programs fast and stable at runtime. The main goal is to ensure that if the metacode is compiled it will work correctly. On the other hand, *Jeta* was designed to provide rapid code.

So if you are dissatisfied with `Java Reflection`, welcome to aboard :)

<div class="alert alert-success" role="alert">
For android developers, <a href="/guide/androjeta/overview">Androjeta</a> is the better way to go.
</div>

At a glance:
--------
*Jeta* provides a [number](/guide) of useful annotations that might help your to develop java programs quicker and safer. Let's take a look on a simple example:

### @Log
Whatever logging tool is used in your project, the loggers can be supplied into classes through `Log` annotation. By default, the logger has a name of the host (master) class:

    :::java
    class LogSample {
        @Log
        Logger logger;
    }

instead of:

    :::java
    class LogSample {
        private final Logger logger = LoggerFactory.getLogger(LogSample.class);
    }

The second approach instigates copy-paste. They often forget to replace the class, so loggers have incorrect names. In the first code snippet, no need to copy the logger code - it's easy to write, but even if you do the `logger` will have correct name.

Of course, this is a straightforward sample, but it illustrates what *Jeta* is all about - *less code, more stability*. Refer to the [user's guide](/guide) to find more features and how to create your own.

Installation (gradle):
----------------------

    :::groovy
    repositories {
        jcenter()
    }

    dependencies {
        apt 'org.brooth.jeta:jeta-apt:1.1'
        compile 'org.brooth.jeta:jeta:1.1'
    }

Complete Installation guide is on [this page](/guide/install)


License
-------

    Copyright 2016 Oleg Khalidov

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

