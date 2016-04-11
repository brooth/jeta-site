<div class="page-header">
    <h2>FindView</h2>
</div>

`@FindView` allows you to bind UI-components from layouts into activities. You no longer have to use `findViewById()`, cast `View` to the actual class, pass the IDs from `R` file. Androjeta does it all for you by default.


Let's go through this feature with an example. Assume we have a layout:

    :::xml
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:layout_width="match_parent"
        android:layout_height="wrap_content">

        <TextView
            android:id="@+id/sampleActivity_textView"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"/>
    </LinearLayout>


To bind the `TextView` into our Activity:

    :::java
    class SampleActivity extends BaseActivity {
        @FindView
        TextView textView;
    }

How does it work? Well, by default Androjeta composes the ID as:

`<Activity name> (from lowercase) + "_" (underscore) + <field name>`

As we expect, for out example it would be "sampleActivity_textView".

<span class="label label-info">Note</span>You shouldn't distrust this approach. In case of misspelling, it fails at compile-time. On the other hand, it helps you to keep your code clean and in one style.

Here is the `BaseActivity`:

    :::java
    class BaseActivity extends Activity {
        @Override
        public void setContentView(int layoutResID) {
            super.setContentView(layoutResID);
            MetaHelper.findViews(this);
        }
    }

For sure, you can pass whatever `R.id` you want:

    :::java
    class SampleActivity extends BaseActivity {
        @FindView(R.id.sampleActivity_textView)
        TextView textView;
    }

or, what important for library modules (`aar`), it's allowed to pass only ID name as a string:

    :::java
    class SampleActivity extends BaseActivity {
        @FindView(name = "sampleActivity_textView")
        TextView textView;
    }

###MetaHelper

Well, to bind the components we should define a helper method for:

    :::java
    public static void findViews(Activity activity) {
        new FindViewController(metasitory, activity).findViews();
    }

Please, read the article about [MetaHelper](/guide/meta-helper) if you didn't yet.
