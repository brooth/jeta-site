<div class="page-header">
    <h2>Event bus</h2>
</div>

`Jeta` has [publish-subscribe pattern](https://en.wikipedia.org/wiki/Publish-subscribe_pattern) implementation. In addition to basic features, it doesn't use reflection. Excited? Let's go though it.

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
    

As the [observer's handler](/guide/observer), `SubscriptionHandler` is used to control the workflow of subscription. You can stop listening a message:

    :::java
    handler.unregister(Message.class);

or all of them:

    :::java
    handler.unregisterAll();

### Priority

It's allowed to order the handler by priority. The handlers with higher priority will be invoked first:

    :::java
    @Subscribe(priority = 146)
    protected void onMessage(Message msg) {
    }


### Filters

You can add filters to the handlers in order to reject unwanter messages:

    :::java
    @Subscribe(filters = { OddFilter.class })
    protected void onMessage(Message msg) {
    }

For the illustration, let's print `OddFilter`:

    :::java
    public static class OddFilter implements Filter<Message> {
        public boolean accepts(Object master, String methodName, Message msg) {
            return msg.id() % 2 != 0;
        }
    }

Two filters are available out of the box, by `id` and by message `topic`. You can define them via `@Subscribe` annotation:

    :::java
    @Subscribe(id = {2, 4}, topic = {"two", "four"})
    protected void onMessage(Message msg) {
    }

<span class="label label-info">Note</span> To make `id` and `topic` filters possible, all the messages must implement `Message` interface or extend `BaseMessage` abstact class. 


### MetaFilters

As it mentioned in the previous articles, `Jeta` is designed to detect the errors at compile-time as far as possible.

todo: an exam that doesn't work with simple filters with generics.
