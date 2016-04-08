<div class="page-header">
    <h2>Dependency Injection</h2>
</div>

Dependency injection is the most powerful part of `Jeta` . Besides of the commontly used `DI` features, it offers some extra:

* Inject entities with parameters
* Extend the entities

###MetaHelper

Before we start, let's define a helper method we will be inject with:

    :::java
    public static void inject(Object master) {
        new InjectController(metasitory, master).inject(scope);
    }


Please, read [this article](/guide/meta-helper) first, if you have questions about `MetaHelper`.

<a name="MetaEntity"></a>
### MetaEntity

However, let's start with a simple case:

    :::java
    @MetaEntity
    class Producer {
    }

    class Consumer {
        @Inject
        Producer producer;

        public Consumer() {
            MetaHelper.inject(this);
        }
    }

Well, the simplest way to inject an entity - define this entity as `MetaEntity`. Each time the `inject(this)` method is invoked, a new instance of `Producer` is injected. If you need a single instance of an entity, you must set up next flag: `@MetaEntity(singleton=true)`. <span class="label label-info">Note</span> It makes a singleton per a `Scope`. Read below about the [scopes](#Scopes) .

In the snippet above, injector creates an instance of `Producer` via default constructor. It's allowed to create a static factory method and provide the instances via it:

    :::java
    @MetaEntity(staticConstructor = "newInstance")
    class Producer {
        public static Producer newInstance() {
            return new Producer();
        }
    }

<span class="label label-info">Note</span> You shouldn't distrust this approach. In case of misspelling, it fails at compile-time.

<br/>
Besides of straight injection, you can provide it via `Lazy`, `Provider` or inject its `class`:

    :::java
    @Inject
    Provider<Producer> producerProvider;
    @Inject
    Lazy<Producer> lazyProducer;
    @Inject
    Class<? extends Producer> producerClass;

<span class="label label-info">Note</span> `Lazy` class provides a single instance of a meta entity and initializes it on demand. `Provider` requests for a new instance each invocation. `Class<? extends >` is useful for a multi-module project where an entity can be [extended](#Extending) by another.

As it's mentioned, `Jeta DI` allows you to inject entities with parameters:

    :::java
    @MetaEntity
    class Producer {
        public Producer(String s, double d) {
        }
    }

    class Consumer {
        @Inject
        MetaFactory factory;
        @Factory
        interface MetaFactory {
            Producer getProducer(String s, double d);
        }

        public Consumer() {
            MetaHelper.inject(this);
            Producer p = factory.getProducer("abc", 0.75);
        }
    }

<span class="label label-info">Note</span> Ones you define a `MetaFactory`, you can use it for the all dependencies of a master, including entities without parameters, provided via `Lazy`, `Provider` and `Class`.


<div class="alert alert-success" role="alert">
Note that the injection expression must match to the entity construction, i.e. you can't inject an entity without meta factory if there is no empty constructor for, otherwise the code won't be compiled. This aspect makes <code>Jeta DI</code> more helpful for development, so, if the code is compiled it should work properly.
</div>


### MetaEntity Provider
In case you need a provider of an entity, e.g. to be able to inject thirdparty class, you must annotate this provider with `@MetaEntity(of=Producer.class)`:

    :::java
    @MetaEntity(of = Producer.class)
    class ProducerProvider {
        @Constructor
        public Producer get() {
            return new Producer();
        }
    }

<span class="label label-info">Note</span> In case of entity provider you must explicitly define factory methods via `@Constructor` annotation. Also, `staticConstructor` is used to create the provider, not entities. If it's needed to create entities via static factory method, just put `@Constructor` annotation on the static method.

    :::java
    @MetaEntity(of = Producer.class)
    class ProducerProvider {
        @Constructor
        public static Producer getProducer() {
            return new Producer();
        }
    }

<a name="Scopes"></a>
### Scopes

You can define as many scopes as it's needed. However, at lease one `Scope` must be created in order to inject module's meta entities. Well, it's important to understand that no one entity can't be provided outside a scope. In the other hand, one entity can belong to many scopes.
Actually, you must set a scope for a creating meta entity:

    :::java
    @MetaEntity(scope = MyScope.class)
    class Producer {
    }

but it's allowed to define a default scope. In this case, you can leave `scope` argument empty. To set a scope as default, it's needed to config your `jeta.properties`:

    :::properties
    inject.scope.default = com.extample.MyScope

Go to [configuration guide](/guide/config) if you have any questions about `jeta.properties`.

Let's create a scope and go through the details.

    :::java
    @Scope
    public class MyScope {
    }

In fact, this class does nothing, but it's used to create a `MetaScope`:

    :::java
    MetaScope<MyScope> myMetaScope =
        new MetaScopeController<>(metasitory, new MyScope()).get();

<span class="label label-info">Note</span> `MetaScope` is the major class of `Jeta DI`. It holds the  information about providers and is used to satisfy module dependencies. You pass a meta scope to `InjectController` in order to use injection:

    :::java
    new InjectController(metasitory, master).inject(myMetaScope);

<span class="label label-info">Note</span> Use `StaticInjectController` for static dependencies.

Nevertheless, there is a little trick that makes scopes useful. You can use it to pass data into the providers. Let's say we need an object `Application` in our meta entities. In this case, the better way is to use a scope for:

    :::java
    public class MyScope {
        private Application app;

        public MyScope(Application app) {
            this.app = app;
        }

        public Application getApplication() {
            return app;
        }
    }

    MetaScope<MyScope> myMetaScope =
        new MetaScopeController<>(metasitory, new MyScope(application)).get();


After that, you can access to `Application` instance in a meta entity:

    :::java
    @MetaEntity
    class Producer {
        private Application app;

        class Provider(MyScope __scope__) {
            this.app = __scope__.getApplication();
        }
    }

<span class="label label-warning">Pay attension</span> You must precisely name the parameter `__scope__` to be able to get access to the scope from a constructor.


### Module

`Module` is the entry point to the `DI` configuration of your project. In the foreground, it just defines the scopes you use, but in the background, it does more complex work.

    :::java
    @Module(scopes = { MyScope.class })
    class MyModule {
    }

<span class="label label-warning">Important</span> You must define exact one `@Module` for a module in which you want to use `Jeta DI`

### Aliases

`Jeta DI` brings the annotations to be able to inject right away. You can find these annotations in `org.brooth.jeta.inject` package. But, it's allowed to use thirdparty annotations as the aliases. It might be useful for the projects that already use other `DI` frameworks.

Let's say we want to use `javax.inject.Inject` to supply the dependencies. To do so, config your `jeta.properties`:

    :::properties
    inject.alias = javax.inject.Inject
    inject.alias.provider = javax.inject.Provider

The `inject.alias.provider` is used in case of injection through a provider:

    :::java
    @Inject
    Provider<Entity> entityProvider;

To let `InjectController` (StaticInjectController) now about `javax.inject.Inject` you also must pass this annotation to the constructor:

    :::java
    new InjectController(metasitory, master, javax.inject.Inject.class)
        .inject(myMetaScope);

otherwise the controllers won't find the masters that use there annotations.


### Hello, World!

For the illustration let's change our `Hello, World!` [example](/guide/code-generating#HelloWorldSample). Instead of providing `Hello, World!` via `@SayHello` annotation, we'll inject it.

First, we create a `Module` and `Scope`:

    :::java
    @Scope
    public class HelloWorldScope {}

    @Module(scopes = HelloWorldScope.class)
    interface HelloWorldModule {}

Next, create a `String` provider:

    :::java
    @MetaEntity(of = String.class, scope = HelloWorldScope.class)
    public class StringProvider {
        @Constructor
        public static String get() {
            return "Hello, World!";
        }
    }

Add the helper method:

    :::java
    public MetaScope<? extends HelloWorldScope> getMetaScope() {
        return new MetaScopeController<S>(metasitory, new HelloWorldScope()).get();
    }

    public static void inject(Object master) {
        MetaScope<HelloWorldScope> metaScope = getInstance().getMetaScope();
        new InjectController(metasitory, master).inject(metaScope);
    }


Finally, amend the sample:

    :::java
    public class HelloWorldSample {
        @Inject
        String str;

        public HelloWorldSample() {
            MetaHelper.inject(this);
        }
    }


<a name="Extending"></a>
### Extending

As it's noticed above, `Jeta DI` is about to extend meta entities easily. For example we will modify the `Hello, World!` example above. Instead of `Hello, World!` let's inject `Hello, Universe!`.

First, we define new scope and provider for:

    :::java
    @Scope(ext = HelloWorldScope.class)
    public class HelloUniverseScope extends HelloWorldScope {
    }

    @MetaEntity(of = String.class, scope = HelloUniverseScope.class)
    public class StringProviderExt {
        @Constructor
        public static String get() {
            return "Hello, Universe!";
        }
    }

Also, change the scope from `HelloWorldScope` to `HelloUniverseScope` in the helper:

    :::java
    public MetaScope<? extends HelloWorldScope> getMetaScope() {
        return new MetaScopeController<S>(metasitory, new HelloUniverseScope())
            .get();
    }

At this point, `Jeta DI` will inject `Hello, Universe!` into `str` as you expect. But, let's clarify what is happening in the listing above.

`@Scope(ext)` - allows you to use a scope as the scope it extends from. So, we can provide `Hello, World!` string using `MetaScope<HelloUniverseScope>` in our example as well. Nevertheless, the real benefit is that you can replace the providers from super scope with new ones. For this purpose we created `StringProviderExt` and pointed its scope to `HelloUniverseScope`.

Apart from direct extending, it's allowed to substitude the super entities as well. To illustrate that, let's extend our [`Producer`](#MetaEntity) entity:

    :::java
    @MetaEntity(ext = Producer.class)
    public class TestProducer extends Producer {
    }

Now, in addition for ability to inject `TestProducer`, you can substitude `Producer` dependencies with it.

<span class="label label-warning">Important</span> The scope of the extender meta entity must extend the scope of the extending entity as well. This means that for our `TestProducer` we must create a scope that extends [`MyScope`](#Scopes):

    :::java
    @Scope(ext = MyScope.class)
    public class MyTestScope {
    }

    @MetaEntity(ext = Producer.class, scope = MyTestScope.class)
    public class TestProducer extends Producer {
    }

Besides this article, it's recomended to go through [multi-modules projects](/guide/multi-modules) guide. It describes how to share the metacode between your modules.

