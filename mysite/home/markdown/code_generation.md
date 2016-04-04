<div class="page-header">
  <h2>Code generating</h2>
</div>

### `javax.annotation.processing`

It's important to understand: `Jeta` is not evaluating the annotations by using reflection API at runtime but generates all the necessary code at compile-time. It allows to emit metacode as it's handwritten. Also, unlike reflection, it is possible to check the code for errors before it is being launched.


### How it works:
There is a little information on the internet, but `javac` allows to do that. Moreover, it's available since   Java <span class="label label-info">1.5</span>. Before all your java code is being compiled, an [Annotation Processor](https://docs.oracle.com/javase/7/docs/api/javax/annotation/processing/Processor.html) can be invoked to scan and process all the annotations in your code.

<div class="alert alert-warning" role="alert">
    Currenty jeta is tested on Java 1.7. Older version might be supported in future releases.
</div>

<span class="label label-success">Thanks to</span> [JavaPoet by Square](https://github.com/square/javapoet) for the great framework, which `Jeta` uses to generate source code.

### Hello, World!<a name="HelloWorldSample"></a>
Let's go through details with an example, in which an annotation `@HelloWorld` sets "Hello, World!" value into a `String` field.

    :::java
    public @interface SayHello {
    }

    public class HelloWorldSample {
        @SayHello
        String str;
    }

Assume if `Jeta` had a processor for this example, the metacode would be:

    :::java
    public class HelloWorldSample_Metacode implements HelloWorldMetacode<HelloWorldSample> {
        @Override
        public void setHelloWorld(HelloWorldSample master) {
            master.str = "Hello, World!";
        }
    }

Similar example can be found on [GitHub](https://github.com/brooth/jeta-samples)

How to write a custom annotation processor, can be found in [this guide](/guide/custom-processor)

How `HelloWorldSample_Metacode` is applied to `HelloWorldSample` is explained in [next article](/guide/at-runtime)


