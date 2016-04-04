<div class="page-header">
	<h2>Logger Provider</h2>
</div>

In this tutirial, we will go through the logger provider feature that `Jeta` has. It's not the most complex part of the library but it is useful and time saver though.

So, whatever logging framework is used in your project, now you can supply it with `@Log` annotation. To be able to do so, you need to define a `NamedLoggerProvider`:

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

As the next step you can pass it to `LogController`, but let's create a helper method in our `MetaHelper`:

    :::java
    public static void createLogger(Object master) {
        new LogController(getInstance().metasitory, master)
            .createLoggers(MyLoggerProvider.getInstance();
    }

If you are not familiar with `MetaHelper` you better to go thought [this guide](/guide/meta-helper) first.

Now you are ready to provide the logger in your classes via `@Log` annotation. 
<span class="label label-info">Note</span> By default the name of the logger equals master's simple name. In case you need another one, you must define it as the annotation's argument - `@Log("MyName")`.

### Hello, World!
Let's log out `Hello, World!` message from the [sample](/guide/code-generating#HelloWorldSample):

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

The output is about to be:

    :::bash
    > Info[HelloWorldSample]: Hello, World! 

