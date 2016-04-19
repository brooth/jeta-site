<div class="page-header">
    <h2>Androjeta</h2>
</div>

In addition to a number of *Jeta*'s features, that are available on Android platform as well, *Androjeta* adds some extra. And of course, *Androjeta* follows the *Jeta*'s concepts - No reflection, compile-time validation and boilerplate-code elimination.

### `Java reflection` as a bad manner

Despite the fact that mobile phones might give odds to personal computers, it is a bad manner nowadays to use *Java Reflection* in android projects. At least the time, the manufacturers will offer the better batteries, the frameworks that build on *Java Reflection* are not rivals to the ones that built on `javax.annotation.processing` like *Jeta*.


### `onSaveInstanceState` issue

Every Android developer probably familiar with `onSaveInstanceState` callback and knows about what the nightmare it might be to keep an activity in a state. You can read details on [developer.android.com](http://developer.android.com/training/basics/activity-lifecycle/recreating.html). Even though this approach requires a lot of boilerplate code, there wasn't a tool that can give you a help with. Now *Androjeta* can:

    :::java
    @Retain
    String myVolatileString;

Go to [*Retain* guide](/guide/androjeta/retain.html) to find out how to make your life easier.

### FindView

*Androjeta* comes with an annotation that is going to be your favorite:

    :::java
    @FindView
    Button saveButton;

This feature eliminates `findViewById` usage. How is that possible? Explained in [this article](/guide/androjeta/findviews.html).


### Jeta collectors vs scan packages

You are not allow to scan packages on Android if you need to search for some classes. Nevertheless, `Jeta Collectors` do that job times faster, even if it were possible. Please, follow [this link](/guide/collector.html) to be aware of `Jeta Collectors` if you are not yet.


###P.S.
In fact, *Jeta* was born as the result of all these issues, Android developers face to every day. Follow  through the [guide](/guide.html) in order to be able to create stable Android apps with enjoyment.
