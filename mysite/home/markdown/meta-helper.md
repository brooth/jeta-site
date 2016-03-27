<div class="page-header">
  <h2>Meta Helper</h2>
</div>

`MetaHelper` is not a class provided by `Jeta`. It's just a way to organize meta code invocation in your project. If you are not comfortable with static helpers you shouldn't use it in your project.

`MetaHelper` is about to provide an entry point to metacode. It holds a singleton of the metasitory and passes it to the controllers.

    :::java
    public class MetaHelper {
        private static final MetaHelper instance = new MetaHelper("com.example");
        private final Metasitory metasitory;

        private MetaHelper(String metaPackage) {
            metasitory = new MapMetasitory(metaPackage);
        }
    }


 You should define the static helpers on demand. Let's add one that creates loggers for elements annotated with `@Log`:

    :::java
    public class MetaHelper {
        private final NamedLoggerProvider<Logger> loggerProvider;

        private MetaHelper(String metaPackage) {
            loggerProvider = new NamedLoggerProvider<Logger>() {
                public Logger get(String name) {
                    return new Logger(name);
                }
            };
        }

        public static void createLoggers(Object master) {
            new LogController(instance.metasitory, master)
                .createLoggers(instance.loggerProvider);
        }
    }

Ones your defined `createLoggers()`, you can provide loggers into your classes:

    :::java
    public class MyBaseClass {
        public MyBaseClass() {
            MetaHelper.createLoggers(this);
        }
    }

 <span class="label label-info">Note</span> `LogController` supports deep metacode invocation. This means that all the extended from `MyBaseClass` classes will get their loggers as well.

    :::java
    public class MyCompleteClass extends MyBaseClass {
        @Log
        Logger logger;

        public MyCompleteClass() {
            logger.info("it works!");
        }
    }


### Hello, World!
Let's complete our `HelloWorld` example from the [previous guide](/guide/at-runtime). Its `MetaHelper` is about to be:

    :::java
    public class MetaHelper {
        private static final MetaHelper instance = new MetaHelper("com.example");
        private final Metasitory metasitory;

        private MetaHelper(String metaPackage) {
            metasitory = new MapMetasitory(metaPackage);
        }

        public static void setHelloWorld(Object master) {
            new HelloWorldController(instance.metasitory, master).apply();
        }
    }


