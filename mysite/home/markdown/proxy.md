<div class="page-header">
    <h2>Proxy</h2>
</div>

`Jeta Proxy` helps you to create [proxy objects](https://en.wikipedia.org/wiki/Proxy_pattern) easily. Let's illustrate it with an example.

Assume we have an interface `Ping` that we use to test `ping` to a server. It constants a method `execute` that returns the time of its work - the ping time.

    :::java
    interface Ping {
        void setUri(String uri);
        int execute();
    }

There is a real implementation of and it works well. Now we need to create a proxy class to be able to wrap any `Proxy` implementation and substitute some logic, e.g. divide on 2 the actual time of the `ping`.


The main aspect of `Jeta Proxy` is that you need to create an abstract class and implement only method you need to override:

    :::java
    public abstract class FixTheTruth implements Ping, AbstractProxy<Ping> {
        @Override
        public int execute() {
            return real().execute() / 2;
        }
    }

Be aware that you can access to the real `Ping` instance via `real()` method. So, in this example, we invoke real implementation and divide its result on two. To wrap an object we will use *MetaHelper* for:


    :::java
    public ProxyTest {
        @Proxy(FixTheTruth.class)
        Ping ping;

        public PingTest(Ping ping) {
            this.ping = ping;
        }

        public void test() {
            MetaHelper.createProxy(this, ping);
            System.out.println(String.format("ping '%s'...", ping.getUri()));
            System.out.println(String.format("done in %dms", ping.execute()));
        }
    }


###MetaHelper

The helper method for `Proxy` feature would be:

    :::java
    public static void createProxy(Object master, Object real) {
        new ProxyController(getInstance().metasitory, master).createProxy(real);
    }

Please, follow [this link](/guide/meta-helper) if you have questions about *MetaHelper*.
