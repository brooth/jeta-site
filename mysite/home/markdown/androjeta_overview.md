
### Java Reflection as a bad manner

Despite the fact that mobile phones might give odds to personal computers, it is a bad manner nowadays to use java reflection in android projects. At least the time, the manufactors will offer better bataries, the libraries build on java reflection are not rivals to ones built on code generating like Jeta.


### onSaveInstanceState issue
No one library provides possibility to retain data while the activity is recreated, but Androjeta does:

    :::java
    @Retain
    String myVolatileString;


Go to [retain guide](/androjeta/retain) to find out how to make your live easier.


### Jeta collectors vs scan packages

Android doesn't allow to scan packages. In the other hand, jeta collectors do that job times faster even if it were possible.


In fact, Jeta was born as a result of the issues, android developers face to every day.
