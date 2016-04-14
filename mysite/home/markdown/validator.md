<div class="page-header">
    <h2>Validators</h2>
</div>

*Jeta* provides validation framework. Let's find out why it's better than the rivals. For this example, let's assume we have an action that hires employees on a job.

    :::java
    public class HireAction {
        @Validate(NotBlank.class)
        String name;
        @Validate(NotEmpty.class)
        String[] degrees;

        public HireAction(String name, String... degrees) {
            this.name = name;
            this.degrees = degrees;
        }

        public void hire() {
            MetaHelper.validate(this);
            //...
        }

        public List<String> checkMePlease() {
            return MetaHelper.validateSafe(this);
        }
    }

Well, it is clear enough, but let's clarify. `NotBlank` validator checks a string is not blank, `NotEmpty` checks arrays, collections or a string is not emplty. `MetaHelper.validate()` will throw `ValidationException` in case of validation errors, `MetaHelper.validateSafe()` will return these errors in a list.

*Jeta* comes with predefined validators - `NotBlank`, `NotEmpty`, and `NotNull`. Nevertheless, you can create any you need. For the illustration let's print the listing of `NotNull` so you can write others similarly:

    :::java
    public class NotNull implements Validator<Object, Object> {
        private String fieldName;

        @Override
        public boolean validate(Object master, Object field, String fieldName) {
            this.fieldName = fieldName;
            return field != null;
        }

        @Override
        public String describeError() {
            return fieldName + " is null";
        }
    }


###MetaValidator

`MetaValidator` allows to to create more complex validators. Assume we need to access to master's fields, e.g. to check a sum of any. Of course we can create an interface, declare the methods for these fields, implement this interface. But it's simpler to use `MetaValidator` instead:

    :::java
    public class HireAction {
        @Validate(NotBlank.class)
        String name;
        @Validate(NotEmpty.class)
        String[] degrees;
        @Validate(AgeValidator.class)
        int age;
        @Validate(ExperienceValidator.class)
        int experience;

        public HireAction(String name, int age, int experience, String... degrees) {
            this.name = name;
            this.degrees = degrees;
            this.age = age;
            this.experience = experience;
        }

        public void hire() {
            MetaHelper.validate(this);
        }

        public List<String> checkMePlease() {
            return MetaHelper.validateSafe(this);
        }
    }

    @MetaValidator(
            emitExpression = "$f > 18",
            emitError = "Too young"
    )
    public interface AgeValidator extends Validator {}

    @MetaValidator(
            emitExpression = "$f <= $m.age - 18",
            emitError = "${$f} years of experience " +
                    "is too high for the age of ${$m.age}"
    )
    public interface ExperienceValidator extends Validator {}

As you probably noticed, `ExperienceValidator` uses `age` field for the check. Besides, if you use `AgeValidator` on a string field, it will fail during compilation. How does it work? `$f` is replaced with the field, it is applied to. `$m` refers to the master instance. In `${}` you can write any java code you need to. Before the compilation, *Jeta* will create java code by these strings, so in case of misspelling, it won't be assembled.

###ValidatorAlias

`ValidatorAlias` allows you create your custom annotations to validate with. You must define these through `jeta.properties`. Please, read [this](/guide/config) if you have questions about this properties file.

    :::properties
    validator.alias.com.example.NotYoung = com.example.AgeValidator
    validator.alias.com.example.NotCheater = com.example.ExperienceValidator

 <span class="label label-info">Note</span> Put `validator.alias.` prefix before the annotation in order to indicate *Jeta* about new alias.

For sure we need to create those annotations:

    :::java
    package com.example;

    public @interface NotYoung {
    }

<span/>

    :::java
    package com.example;

    public @interface NotCheater {
    }


Certainly *Jeta* provides aliases for its validators. Look up them in `org.brooth.jeta.validate.alias` package. Well, due to `ValidatorAlias` code looks cleaner:

    :::java
    public class HireAction {
        @NotBlank
        String name;
        @NotEmpty
        String[] degrees;
        @NotYoung
        int age;
        @NotCheater
        int experience;

        public HireAction(String name, int age, int experience, String... degrees) {
            this.name = name;
            this.degrees = degrees;
            this.age = age;
            this.experience = experience;
        }

        public void hire() {
            MetaHelper.validate(this);
        }

        public List<String> checkMePlease() {
            return MetaHelper.validateSafe(this);
        }
    }

<span class="label label-warning">Pay attension</span> Prior to version 2.0 the annotations must be already compiled into byte-code in order to use them as the aliases.

###MetaHelper

The validation helper methods would be:

    :::java
    public static void validate(Object master) throws ValidationException {
        new ValidationController(metasitory, master).validate();
    }

    public static List<String> validateSafe(Object master) {
        new ValidationController(metasitory, master).validateSafe();
    }

