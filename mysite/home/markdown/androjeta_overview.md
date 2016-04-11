<div class="page-header">
    <h2>Androjeta</h2>
</div>

### Java Reflection as a bad manner

Despite the fact that mobile phones might give odds to personal computers, it is a bad manner nowadays to use `java reflection` in android projects. At least the time, the manufacturers will offer the better batteries, the frameworks that build on `java reflection` are not rivals to ones that built on `javax.annotation.processing` like `Jeta`.


### `onSaveInstanceState` issue

Every Android developer probably familiar with `onSaveInstanceState` callback and knows about what nightmare it might be to keep an activity in a state. You can read details on [developer.android.com](http://developer.android.com/training/basics/activity-lifecycle/recreating.html). Even though this approach requires a lot of boilerplate code, there wasn't a library that can give you a help with. Now `Androjeta` can:

    :::java
    @Retain
    String myVolatileString;


Go to [retain guide](/androjeta/retain) to find out how to make your life easier.

### FindView

`Androjeta` comes with an annotation that is going to be your favorite:

    :::java
    @FindView
    Button saveButton;

This feature eliminates `findViewById` usage. How is that possible? Explained in [this article](/guide/findviews).


### Jeta collectors vs scan packages

Android doesn't allow you to scan java packages if you need to search for some classes. Nevertheless, `Jeta Collectors` do that job times faster, even if it were possible. Please, follow [this link](/guide/collector) to be aware of `Jeta Collectors` if you are not.


###P.S.
In fact, `Jeta` was born as a result of all these issues, Android developers face to every day. Follow to the [guide](/guide) in order to be able to create stable Android apps with enjoyment.
