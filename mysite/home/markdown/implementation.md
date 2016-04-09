<div class="page-header">
    <h2>Implementation</h2>
</div>

In a multi-module project might be a case when some feature needs to be implemented many ways. For example, `DbManger` needs a driver to work with a database implementation. It might be `sqlite`, `postgres` or any other. `DbManger` does a lot - supports JPQL, mappings, DAO and other features, but depends on a driver to be able to communicate with exact DB implementation. Let's see how `Jeta Implementation` can help:

    :::java
    class DbManger {
        DbDriver driver;

        public DbManger() {
            driver = MetaHelper.getImplementation(DbDriver.class);
            if(driver == null)
                throw new IllegalStateException("Db driver not defined");
        }
    }

    interface DbDriver {
        void connect();
        ResultSet query(String sql);
        // others...
    }

In the module, we need to use `DbManger`, we provide the implementation:

    :::java
    @Implementation(DbDriver.class)
    class SqliteDbDriver implements DbDriver {
        //...
    }

Furthermore, in the test module we can substitude the driver with a fake one:

    :::java
    @Implementation(DbDriver.class, priority = 100)
    class TestDbDriver implements DbDriver {
        //...
    }

###MetaHelper

Let's define the helper method:

    :::java
    public static <I> getImplementation(Class<I> of) {
        return new ImplementationController<I>(metasitory, of).getImplementation();
    }

In addition to `getImplementation()` method the controller provides `getImplementations()` if it's needed to get all the implementations and `hasImplementation()` to check if there is any.
