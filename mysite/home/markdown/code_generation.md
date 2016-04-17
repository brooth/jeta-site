<div class="page-header">
  <h2>Code generating</h2>
</div>

### `javax.annotation.processing`

It is good to know: *Jeta* is not evaluating the annotations by using *Reflection API* at runtime. It generates all the necessary code at compile-time. It allows to emit metacode as it is handwritten. Also, unlike reflection, it is possible to check the code for errors before it is launched.


### How it works:
There is a bit of information on the Internet, but `javac` allows to do code generating. Moreover, it's available since   Java <span class="label label-info">1.5</span>. Before your java code is compiled, an [Annotation Processor](https://docs.oracle.com/javase/7/docs/api/javax/annotation/processing/Processor.html) will be launched, so you can scan and process all the annotations in your code.

<div class="alert alert-warning" role="alert">
    Currenty jeta is tested on Java 1.7. Older version might be supported in future releases.
</div>

<span class="label label-success">Thanks to</span> [JavaPoet by Square](https://github.com/square/javapoet) for the great framework that *Jeta* uses to generate source code.

### Hello, World!<a name="HelloWorldSample"></a>
Let's take a look at the example, in which an annotation `@SayHello` sets *"Hello, World!"* into a field.

    :::java
    public @interface SayHello {
    }

    public class HelloWorldSample {
        @SayHello
        String str;
    }

If *Jeta* had a processor for this example, the metacode would be:

    :::java
    public class HelloWorldSample_Metacode implements HelloWorldMetacode<HelloWorldSample> {
        @Override
        public void setHelloWorld(HelloWorldSample master) {
            master.str = "Hello, World!";
        }
    }

You can find sample code for the processor that generates above metacode on [this page](/guide/custom-processor). Also, there is a similar example on [GitHub](https://github.com/brooth/jeta-samples).

How `HelloWorldSample_Metacode` is applied to `HelloWorldSample` is explained in the [next article](/guide/at-runtime).
