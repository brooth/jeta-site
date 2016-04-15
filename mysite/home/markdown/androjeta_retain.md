<div class="page-header">
    <h2>Retain</h2>
</div>

*Androjeta* lets you to avoid usage of one of the most annoying-boilerplate-required-thing on Android. No need anymore to use `onSaveInstanceState` callback to retain sensitive data. For those of you who are not familiar with this issue, here is the listing. In order to use fields for storing activity state, you have to take care of its recovery in case of Android has [destroyed](http://developer.android.com/training/basics/activity-lifecycle/recreating.html) this activity.

    :::java
    class SampleActivity extends Activity {
        private String data;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            if (savedInstanceState != null)
                data = bundle.getString("data");
        }

        @Override
        protected void onSaveInstanceState(Bundle outState) {
            super.onSaveInstanceState(outState);
            outState.putString("data", data);
        }
    }

Fortunately, `@Retain` annotation can do that for you:

    :::java
    class SampleActivity extends BaseActivity {
        @Retain
        String data;
    }

In the `BaseActivity` we need to call the helper methods though:

    :::java
     @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (savedInstanceState != null)
            MetaHelper.restoreRetains(this, savedInstanceState);
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        MetaHelper.saveRetains(this, outState);
    }

###MetaHelper

Let's define these two methods:

    :::java
    public static void saveRetains(Activity activity, Bundle bundle) {
        new RetainController(metasitory, activity).save(bundle);
    }

    public static void restoreRetains(Activity activity, Bundle bundle) {
        new RetainController(metasitory, activity).restore(bundle);
    }

