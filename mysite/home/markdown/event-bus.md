<div class="page-header">
    <h2>Event bus</h2>
</div>

`Jeta` providers an implementation of [publish-subscribe pattern](https://en.wikipedia.org/wiki/Publish-subscribe_pattern). Besides basic features, it has a great achievement - no reflection is used. Excited? Let's go though it.

###Subscriber 

    :::java
    class Subscriber {
        private SubscriptionHandler handler;

        public Subscriber() {
            handler = MetaHelper.registerSubscriber(this);
        }

        @Subscribe
        protected void onMessage(Message msg) {
        }
    }
    

As the [observer's handler](/guide/observer), `SubscriptionHandler` gives you an ability to control subscription workflow. You can stop listening a message:

    :::java
    handler.unregister(Message.class);

or all of them:

    :::java
    handler.unregisterAll();

### Priority

It's allowed to order the handlers by priority. Handlers with higher priority will be invoked first:

    :::java
    @Subscribe(priority = 146)
    protected void onMessage(Message msg) {
    }

Handlers with the same priority are invoked randomly.

### Filters

You can use handler filters in order to reject unwanter messages:

    :::java
    @Subscribe(filters = { OddFilter.class })
    protected void onMessage(Message msg) {
    }

For the illustration, the print of `OddFilter` would be:

    :::java
    public class OddFilter implements Filter<Message> {
        public boolean accepts(Object master, String methodName, MyMessage msg) {
            return msg.id() % 2 != 0;
        }
    }

Two filters are available out of the box, by `id` and by `topic`. You can define them via `@Subscribe` annotation:

    :::java
    @Subscribe(id = {2, 4}, topic = {"two", "four"})
    protected void onMessage(Message msg) {
    }

<span class="label label-info">Note</span> To make `id` and `topic` filters possible, all the messages must implement `Message` interface or extend `BaseMessage` class. 


### MetaFilters

As it mentioned in the previous articles, `Jeta` is designed to detect errors at compile-time as far as possible. With plain filters this principle work with message types. Let's say we have a filter that work with a particular message type:

    :::java
    public class MyMessage extends BaseMessage {
    }

    public class MyFilter implements Filter<MyMessage> {
        public boolean accepts(Object master, String methodName, Message msg) {
            return true;
        }
    }

If we try to use this filter on a method that accepts not assigneble from `MyMessage` class as the event, the code won't be compiled. But `MetaHelper` allows you to write more complex checks, e.g. access to a nonprivate constant:

    :::java
    @MetaFilter(emitExpression = "$m.THE_NUMBER % 2 == 0")
    public interface EvenMetaFilter extends Filter {}


`$m` is replaced with the master class, that uses this filter. So, if the master doesn't have `THE_NUMBER` field, it will fail during compilation. You can also use `$e` to get access to the message instance.


### MetaHelper

You can either use Jeta's basic implementation of `EventBus` - `org.brooth.jeta.eventbus.BaseEventBus` or implement your own. Also, you can you a single instance of the bus or create many. Nevertheless, you must pass an instance of the bus to the controller. Let's create a helper method for:

    :::java
    public static SubscriptionHandler registerSubscriber(Object master) {
        return new SubscriberController<>(metasitory, master)
            .registerSubscriber(bus);
    }

You should definitely follow [this link](/guide/meta-helper) if you are still not familiar with `MetaHelper`.
