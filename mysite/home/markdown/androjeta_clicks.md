<div class="page-header">
    <h2>OnClick and OnLongClick</h2>
</div>

With `@OnClick` and `@OnLongClick` annotations you can use methods as `android.view.View.OnClickListener
` and `android.view.View.OnLongClickListener` respectively. Also, no need to implement any interfaces:

    :::java
    public class SampleActivity extends BaseActivity {
        @OnClick
        void onClickSaveButton() {
        }

        @OnLongClick
        void onLongClickSaveButton() {
        }
    }

As well as in case of [@FindView](/guide/androjeta/findviews), Androjeta composes the ID by default:

`<Activity name> (from lowercase) + "_" (underscore) + <method name without prefix "onClick" or "onLongClick" resp.>`

<span class="label label-info">Note</span> For sure no reasons to distrust this approach. In case of misspelling, the code won't be assembled.

Clearly, for this example, both `onClickSaveButton` and `onLongClickSaveButton` are bound to a view by id `R.id.sampleActivity_saveButton`.

<span class="label label-info">Note</span> In case of `OnLongClick` and `void` as the return type, Androjeta will return `true` by default. Change it to `boolean` otherwise.

You can also define IDs explicitly:

    :::java
    @OnClick(R.id.sampleActivity_saveButton)
    void onClickSaveButton() {
    }

or

    :::java
    @OnClick(name = "sampleActivity_saveButton")
    void onClickSaveButton() {
    }


`BaseActivity` would be:

    :::java
    class BaseActivity extends Activity {
        @Override
        public void setContentView(int layoutResID) {
            super.setContentView(layoutResID);
            MetaHelper.applyOnClicks(this);
        }
    }

###MetaHelper

The helper method would be:

    :::java
    public static void applyOnClicks(Activity activity) {
        new OnClickController(metasitory, activity).addListeners();
    }
