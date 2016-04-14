<div class="page-header">
    <h2>Multi-Module Projects</h2>
</div>

Multi-module projects is the place where *Jeta* does its best. You can share metacode between modules, override behavior, substitute classes and so on. It also should be important for any project, since projects are frequently composed of at least couple of modules - main and test.

As it mentioned in ["dependency injection" article](/guide/inject), you are allowed to extend providers. To make that possible, you must create one code-base for all your modules. In this tutorial, we will stick the approach that we used in the previous guides - *MetaHelper*, which holds singleton instance of the metasitory.

Projects can include as many modules as it's needed and the helper methods can be used in any of these modules. However, for this guide we are using two - main and test.

To be able to add metacode from one module into another, e.g. from test to main, metasitory provides a method for:

    :::java
    public interface Metasitory {
        void add(Metasitory other);
    }


Nevertheless, `MapMetasitory` provides similar method that matches better for this case:

    :::java
    public class MapMetasitory implements Metasitory {
        public void loadContainer(String metaPackage) {...}
    }


The only thing we need to do - pass our test package name into this method during initialization. Something like:

    :::java
    public TestApp extends MainApp {
        protected void init() {
            super.init();
            MetaHelper.getMetasitory().loadContainer("com.example.test");
        }
    }

###DI Scopes

Let's walk through an example, in which we need to substitute an entity that is injected in main module. As it's described in [dependency injection guide](/guide/inject), we must create a scope and provider that extend corresponding classes from main module. With created scope you can provide different entities for old dependencies. There is one problem though. How to replace the scope with the test one? We can use `@Implementation` [feature](guide/implementation) for this:

    :::java
    @Scope
    @Implementation(AppScope.class)
    public class AppScope {
    }


By default, the implementation is provided by itself. In *MetaHelper*, instead of creating `AppScope` we're looking up its implementation.

    :::java
    public class MetaHelper {
        public static void inject(Object master) {
            AppScope scope =
                new ImplementationController<>(metasitory, AppScope.class)
                    .getImplementation());
            MetaScope<AppScope >metaScope =
                new MetaScopeController<>(metasitory, scope).get();
            new InjectController(metasitory, master).inject(metaScope);
        }
    }

Finally, in test module we set test scope as the implementation of main scope, but with higher priority:

    :::java
    @Scope
    @Implementation(value = AppScope.class, priority = 1)
    public class TestAppScope extends AppScope {
    }

After test metacode is added into main metasitory, main injection scope will be replaced with the test one.

