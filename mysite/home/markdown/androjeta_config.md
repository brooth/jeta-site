<div class="page-header">
    <h2>Configuration</h2>
</div>

In addition to the [*Jeta* properties](/guide/config) you need to define your project's `applicationId` in order to use [@FindView](/guide/androjeta/findviews), [@OnClick](/guide/androjeta/clicks) or [@OnLongClick](/guide/androjeta/clicks). Well, if you haven't read [how to config Jeta](/guide/config) yet, you shoult do it first.

To define module's `applicationId` add this line into your `jeta.properties`:

    :::properties
    application.package = <your applicationId here>

