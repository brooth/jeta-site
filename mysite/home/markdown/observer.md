<div class="page-header">
    <h2>Observer</h2>
</div>

Easy to use [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern) implementation.

###Observable

    :::java
    class Observable {
        @Subject
        Observers<Event> observers;

        public Observable() {
            MetaHelper.createObservable(this);
        }
    }

Through `observers` you can fire an event:

    :::java
    observers.notify(event);

remove all observers:

    :::java
    observers.clear();

or both:

    :::java
    observers.notifyAndClear(event);


###Observer

To create an *Observer*, add `@Observe` annotation to the method that accepts one parameter - `Event` class.

    :::java
    class Observer {
        private ObserverHandler handler;

        public Observer() {
            Observable observable = new Observable();
            handler = MetaHelper.registerObserver(this, observable);
        }

        @Observe(Observable.class)
        void onEvent(Event event) {
        }
    }

<span class="label label-info">Note</span> You must define the observables, i.e. the methods you are listening to.

The `handler` allows you to detach your class from *Observable*:

    :::java
    handler.unregisterAll(Observable.class);

Stop listening to a certain event:

    :::java
    handler.unregister(Event.class);

You can use one handler to control many *Observables*:

    :::java
    handler.add(MetaHelper.registerObserver(this, otherObservable));

And unregister all the listeners at once:

    :::java
    handler.unregisterAll();

###MetaHelper

In the examples above we use two helper methods. Their code would be:

    :::java
    public static void createObservable(Object master) {
        new ObservableController<>(metasitory, master).createObservable();
    }

    public static ObserverHandler registerObserver(Object observer, Object observable) {
        return new ObserverController<>(metasitory, observer).registerObserver(observable);
    }

Please, read [this article](/guide/meta-helper.html) if you have questions about *MetaHelper*.

You should also look at [*Event-Bus*](/guide/event-bus.html) features in addition to this guide.

