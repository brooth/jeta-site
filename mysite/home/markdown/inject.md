<div class="page-header">
    <h2>Dependency Injection</h2>
</div>

Depandency injection is the most powerfull part of `Jeta` . It allows that other `DI` frameworks do, plus two really useful features:

* Inject entities with parameters
* Extend the entities

But let's start with a simple case:

### MetaEntity

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

Well, the simplest way to inject an entity - define this entity as `MetaEntity`. Each time the `inject(this)` method is invoked, a new instance of `Producer` is injected. If you need a single instance of en entity, you must set up next flag to `true`: `@MetaEntity(singleton = true)`. <span class="label label-info">Note</span> It makes a singleton per a [`Scope`](#Scopes). Read below about the scopes.

In the snippet above, injector creates an instance of `Producer` via default constructor. It's allowed to create a static factory method and provide the instances via it:

    :::java
    @MetaEntity(staticConstructor = "newInstance")
    class Producer {
        public static Producer newInstance() {
            return new Producer();
        }
    }

<span class="label label-info">Note</span> You shouldn't distruct of this approach. In case of misspelling it fails at complile-time.

<br/>
Besides of straight injection, you can provide it via `Lazy`, `Provider` or inject its `class`:

    :::java
    @Inject
    Provider<Producer> producerProvider;
    @Inject
    Lazy<Producer> lazyProducer;
    @Inject
    Class<? extends Producer> producerClass;

<span class="label label-info">Note</span> `Lazy` class provides a single instance of a meta entity and initializes it on demand. `Provider` requests for a new instance each invocation.

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

### MetaEntity Provider
In case you need a provider of an entity, e.g. to be able to inject thirdparty class, you need to annotate this provider with `@MetaEntity(of = Producer.class)`:

    :::java
    @MetaEntity(of = Producer.class)
    class ProducerProvider {
        @Constructor
        public Producer get() {
            return new Producer();
        }
    }

<span class="label label-info">Note</span> In case of entity provider you must explicitly define factory methods via `@Constructor` annotation. In the other hand `staticConstructor` is used to create the provider, not entities. If it's needed to create entities with a provider via static factory method, just put `@Constructor` annotation on the static method.

    :::java
    @MetaEntity(of = Producer.class)
    class ProducerProvider {
        @Constructor
        public static Producer getProducer() {
            return new Producer();
        }
    }

### Scopes <a name="Scopes"></a>

You can define as many scopes as it's needed. But, at lease one `Scope` must be created in order to inject module's meta entities. Well, it's important to understant that no one entity can't be provided outside a scope. In other hand, one entity can belong to many scopes.
In fact, you need to set a scope for a created meta entity:

    :::java
    @MetaEntity(scope = MyScope.class)
    class Producer {
    }

, but it's allowed to define a default scope. In this case you can leave `scope` argument empty. To set a scope as default, you need to add next line into `jeta.properties`

    :::properties
    inject.scope.default = com.extample.MyScope

Go to [configuration guide](/guide/config) if you are confused about `jeta.properties`.

Let's create a scope and go thought some details of it.

    :::java
    @Scope
    public class MyScope {
    }

Actually, this class does noithiing, but it's used to create a `MetaScope`:

    :::java
    MetaScope<MyScope> myMetaScope =
        new MetaScopeController<>(metasitory, new MyScope()).get();

<span class="label label-info">Note</span> `MetaScope` is the major class of `Jeta DI`. It holds the  information about providers and is used to satisfy module dependencies. You must pass a meta scope to `InjectController` in order to inject meta entities into a master:

    :::java
    new InjectController(metasitory, master).inject(myMetaScope);

But, there is a little trick that makes scopes useful though. You can use it to pass data into the providers. Let's say we need an object `Application` in our meta entities. In this case the better way is to use a scope for:

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

Now you can access to `Application` object in a meta entity:

    :::java
    @MetaEntity
    class Producer {
        private Application app;

        class Provider(MyScope __scope__) {
            this.app = __scope__.getApplication();
        }
    }

<span class="label label-info">Note</span> You actually must name the parameter as `__scope__` in order to get access to the scope's instance.


### Module

`Module` is an entry point to the `DI` configuration of your project. In the foreground it's just defines the scopes you use, but in the background it does more complex work.

    :::java
    @Module(scopes = MyScope.class)
    class MyModule {
    }

<div class="alert alert-warning" role="alert">
Pay attension that you must define exact one <code>Module</code> for a module in which you use injection.
</div>

### Aliases

### Extending

As it's mentions above, `Jeta DI` is about to extend meta entities easily.


### Hello, World!


