<div class="page-header">
	<h2>Dependency Injection</h2>
</div>

Depandency injection is the most powerfull part of `Jeta` . It allows that other `DI` frameworks do, plus two really useful features: 

* Inject entities with parameters
* Extend the entities

### MetaEntity

But let's start with a simple case:

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

So, the simplest way to inject an entity - define this entity as `MetaEntity`. Each time the `inject(this)` method is invoked, a new instance of `Producer` is injected. If you need a single instance of `Producer` you need to set up this flag: `@MetaEntity(singleton=true)`. <span class="label label-info">Note</span> It makes a singleton per a [`Scop`](#Scop).


Besides of straight injection, you can provide it via `Lazy`, `Provider` or inject its `class`:

    :::java
    @Inject
    Provider<Producer> producerProvider;
    @Inject
    Lazy<Producer> lazyProducer;
    @Inject
    Class<? extends Producer> producerClass;

<span class="label label-info">Note</span> `Lazy` class provides a single instance of a meta entity and initializes it on demand. `Provider` requests for a new instance each invocation.

### MetaEntity Provider
In case you need a provider of an entity, e.g. to be able to inject thirdparty class, you need to put `@MetaEntity(of=Producer.class)` on this provider:

    :::java
    @MetaEntity(of=Producer.class)
    class ProducerProvider {
        @Constructor
        public Producer get() {
            return new Producer();
        }
    }


