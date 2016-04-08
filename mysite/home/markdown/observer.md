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

Now you can fire an event:

    :::java
    observers.notify(event);

remove all observers:

    :::java
    observers.clear();

or both:

    :::java
    observers.notifyAndClear(event);

list the observers:

    :::java
    List<EventObserver<Event>> list = observers.getAll();


###Observer

To create an `Observer`:

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

The `handler` allows you to detatch your class from `observable`:

    :::java
    handler.unregisterAll(Observable.class);

Stop listening certain event:

    :::java
    handler.unregister(Event.class);


You can use one handler for all `observables`:

    :::java
    handler.add(MetaHelper.registerObserver(this, otherObservable));

It's allowed to unregister from all the observables at ones:

    :::java
    handler.unregisterAll();

###MetaHelper

Please, the the article about [MetaHelper](/guide/meta-helper) if you have questions about next listing.
In the examples above we use two helper methods. Their code would be:

    :::java
    public static void createObservable(Object master) {
        new ObservableController<>(getInstance().metasitory, master)
            .createObservable();
    }

    public static ObserverHandler registerObserver(Object observer, Object observable) {
        return new ObserverController<>(getInstance().metasitory, observer)
            .registerObserver(observable);
    }


You should also become acquainted with [event-bus feature](/guide/event-bus) in addition to this guide.

