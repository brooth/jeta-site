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

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_sample);
            MetaHelper.findViews(this);
        }
    }

How does it work? Well, by default Androjeta composes the ID as:

    :::
    <Activity name> (from lowercase) + "_" (underscore) + <field name>

As we expect, ror out example it would be "sampleActivity_textView".

<span class="label label-info">Note</span>You shouldn't distrust this approach. In case of misspelling, it fails at compile-time. On the other hand, it helps you to keep your code clean and in one style.

For sure, if it's needed, you can pass whatever ID you want:

    :::java
    class SampleActivity extends BaseActivity {
        @FindView(R.id.sampleActivity_textView)
        TextView textView;
    }

or, what important for `aar` modules, it's allowed to pass only ID name as a string:

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
