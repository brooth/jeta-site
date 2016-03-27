<div class="page-header">
  <h2>How it works at Runtime</h2>
</div>

<img src="/static/images/at_runtime.png" width="700px"/>

### Master and Metacode
`Master` - is java type which uses an annotation and being processed by `Jeta`. For each master, Jeta generates the `Metacode` class. It is located in the same package as its master and has a name as &lt;master name&gt; + "_Metacode".

### Metasitory
`Metasitory` is a short for `Meta Code Repository`. It holds the required information about generated code. During the annotation processing, `Metasitory Writer` creates a meta storage. This storage contains the information about the masters, their metacodes and annotations they use.

Currenlty `Jeta` provides `HashMapMetasitory` implementation. It uses `java.util.IdentityHashMap` for storing and querying the meta code. You can replace this implementation with any other. Follow to [this guide](/guide/custom-metasitory) for the complete instructions.

### Criteria
The `Criteria` provides a way for defining a quiry to a metasitory. In most cases, `Criteria` is used for querying metacode by its master. It's allowed to query for a single instance, that generated for a given master, or for all tree including the metacodes generated for sub-masters as well. It gives you the ability to invoke the controller ones in the super class, so in the sub-classes, metacode will be applied as well.


todo: describe the methods

### Controller
`Controller` searches for requited meta code and applies it to the `master`. Well, it's just a common case and some controllers do more complex work. It is not necessary to use a controller. You can create your own class to be able to invoke meta code in your way.

### Hello, World!
Let's continue to observe the `Hello, World!` example, from the [previous guide](/guide/code-generating), and find out how to apply the metacode to the sample class:

First of all, we need to declare the interface. It will be implemented by metacodes generated for `@HelloWorld` users (you might note for this interface in the previous article):

    :::java
    public interface HelloWorldMetacode<M> {
        void setHelloWorld(M master);
    }

And the controller:

    :::java
    public class HelloWorldController {
        protected Collection<HelloWorldMetacode> metacodes;

        public HelloWorldController(Metasitory metasitory, Object master) {
            Criteria criteria = new Criteria.Builder().masterEqDeep(master.getClass()).build();
            this.metacodes = (Collection<HelloWorldMetacode>) metasitory.search(criteria);
        }

        public void apply() {
            for (HelloWorldMetacode<Object> metacode : metacodes)
                metacode.setHelloWorld(master);
        }
    }

<span class="label label-info">Note</span> The controller searches the metacode by itself for the illustration.The better way to extend `MasterController` which does it for you.

The final step - we need to create new method in our `MetaHelper` class:

    :::java
    public static void setHelloWorld(Object master) {
        new HelloWorldController(getInstance().metasitory, master).apply();
    }

What the `MetaHelper` is for and how to organize it in your project is explained in [the next article](/guide/meta-helper)

