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

Well, the simplest way to inject an entity - define this entity as `MetaEntity`. Each time the `inject(this)` method is invoked, a new instance of `Producer` is injected. If you need a single instance of en entity, you must set up next flag to `true`: `@MetaEntity(singleton = true)`. <span class="label label-info">Note</span> It makes a singleton per a [`Scope`](#Scope). Read below about the scopes.

<br/>

In the snippet above, injector creates an instance of `Producer` via default constructor. It's allowed to create a static factory method and provide the instances via it:

    :::java
    @MetaEntity(staticConstructor = "newInstance")
    class Producer {
        public static Producer newInstance() {
            return new Producer();
        }
    }

<div class="alert alert-info" role="alert">
You shouldn't distruct of this approach. In case of misspelling it fails at complile-time.
</div>

Besides of straight injection, you can provide it via `Lazy`, `Provider` or inject its `class`:

    :::java
    @Inject
    Provider<Producer> producerProvider;
    @Inject
    Lazy<Producer> lazyProducer;
    @Inject
    Class<? extends Producer> producerClass;

<span class="label label-info">Note</span> `Lazy` class provides a single instance of a meta entity and initializes it on demand. `Provider` requests for a new instance each invocation.

<br/>

### MetaEntity Provider
In case you need a provider of an entity, e.g. to be able to inject thirdparty class, you need to put `@MetaEntity(of=Producer.class)` on it:

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
        public static Producer newInstance() {
            return new Producer();
        }
    }

### Scopes <a name="Scopes"/>

