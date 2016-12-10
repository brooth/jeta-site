<div class="page-header">
    <h2>FindView</h2>
</div>

`@FindView` allows you to bind UI-components from the layouts into your activities. You no longer have to use `findViewById()`, cast `View` to the actual class, pass the IDs from `R` file. *Androjeta* does it all for you by default.

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

`<lowercased activity name> + "_" (underscore) + <field name>`

So, for our example it will be *"sampleActivity_textView"*.

<span class="label label-info">Note</span> You shouldn't distrust this approach. In case of misspelling, it will fail at compile-time. Also, it helps you keep your code clean and in one style.

Here's the `BaseActivity`:

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

or, what is important for library modules (`aar` files), you can pass only ID as a string:

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

Please, read the article about [MetaHelper](/guide/meta-helper.html) if you haven't yet.
