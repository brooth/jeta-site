<div class="page-header">
    <h2>Logger Provider</h2>
</div>

In this tutorial, we will go through the logger providing feature. It's not the most complex framework's part but it is useful and time saver, though. It's allowed to use `@Log` with any logging tool. To do that you need to define a `NamedLoggerProvider`:

    :::java
    import org.brooth.jeta.log.NamedLoggerProvider;

    public class MyLoggerProvider implements NamedLoggerProvider<MyLogger> {
        private static MyLoggerProvider instance = new MyLoggerProvider();

        public static MyLoggerProvider getInstance() {
            return instance;
        }

        public MyLogger get(String name) {
            MyLogger logger = new MyLogger();
            logger.setName(name);
            return logger;
        }
    }

###MetaHelper

The second step you should pass it to `LogController`, but let's create a helper method in our *MetaHelper*:

    :::java
    public static void createLogger(Object master) {
        new LogController(metasitory, master).createLoggers(MyLoggerProvider.getInstance();
    }

If you are not familiar with *MetaHelper* you better to go thought [this guide](/guide/meta-helper) first.

Now, you're ready to supply the loggers in your classes through `@Log` annotation. <span class="label label-info">Note</span> By default the name of the logger equals master's simple name. If you need you can define different one via the annotation's argument - `@Log("MyName")`.

### Hello, World!
Let's output `Hello, World!` message from [*HelloWorld*](/guide/code-generating#HelloWorldSample) sample.

    :::java
    public class HelloWorldSample {
        @Log
        MyLogger logger;
        @SayHello
        String str;

        public HelloWorldSample() {
            MetaHelper.createLoggers(this);
            MetaHelper.setHelloWorld(this);

            logger.info(str);
        }
    }

The result would be like:

    :::bash
    > Info[HelloWorldSample]: Hello, World!

