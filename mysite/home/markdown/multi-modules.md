<div class="page-header">
    <h2>Multi-Module Projects</h2>
</div>

Multi-Module projects is the place where `Jeta` does its best. You can share metacode between modules, override behavior, substitute classes and so on. It also should be important for any project, since projects frequently include at least two modules - main and test.


As you probably know from [injection article](/guide/inject), it's allowed to extend dependency providers easily. But, to make that possible, you need to have one code-base for the all your modules. For this tutorial we will stick the approach that we use all the guides - `MetaHelper` which holds singleton instance of the metasitory. This helper class can be used in any module, however, for the illustration we will use two - main and test.


To be able to add metacode from one module into another, e.g. from test to main, metasitory provides a method for:

    :::java
    public interface Metasitory {
        void add(Metasitory other);
    }


Nevertheless, `MapMetasitory` provides similar method that is matched better for this case:

    :::java
    public class MapMetasitory implements Metasitory {

        public void loadContainer(String metaPackage) {...}
    }


Well, the only thing we need to do - pass our test package name into this method during initialization. Something like:

    :::java
    public TestApp extends MainApp {
        protected void init() {
            super.init();
            MetaHelper.getMetasitory().loadContainer("com.example.test");
        }
    }

###DI Scopes

Let's go through an example, in which we need to substitute an entity that is injected in main module. As it's described in [dependency injection guide](/guide/inject), we must create a scope and provider that extend the ones from the main module. But how to replace the scope with the test one? We can use `@Implementation` [feature](guide/implementation) for:

    :::java
    @Scope
    @Implementation(AppScope.class)
    public class AppScope {
    }


In `MetaHelper`, instead of creating `AppScope` we search for its implementation. Which is itself by default.

    :::java
    public class MetaHelper {
        public static void inject(Object master) {
            AppScope scope =
                new ImplementationController<>(metasitory, AppScope.class)
                    .getImplementation().get();
            MetaScope<AppScope >metaScope =
                new MetaScopeController<>(metasitory, scope).get();
            new InjectController(metasitory, master).inject(metaScope);
        }
    }

Finally, in test module we set test scope as the implementation of main scope:

    :::java
    @Scope
    @Implementation(value = AppScope.class, priority = 1)
    public class TestAppScope extends AppScope {
    }
