<div class="page-header">
    <h2>Validators</h2>
</div>

`Jeta` provides validation framework. Let's find out why it's better than rivals. As the example we will use an action that hires an employe on a job.

    :::java
    public class HireAction {
        @Validate(NotBlank.class)
        protected String name;
        @Validate(NotEmpty.class)
        protected String[] degrees;

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

`Jeta` comes with predefined validators - `NotBlank`, `NotEmpty` and `NotNull`. Nevertheless you can create any you need. For the illustration let's print the lisning of `NotNull` so you can write others similarly:

    :::java
    public class NotNull implements Validator {
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

If we try to use `NotBlank` validator on a `Double` field, the code will be compiled well but the validator will throw `IllegalArgumentException` at runtime. This behavior is predictable but not follows the `Jeta` conception. So, if you need validators that can be applied on matched fields only you should use `MetaValidator` instead.

    :::java
    public class HireAction {
        @Validate(NotBlank.class)
        public String name;
        @Validate(NotEmpty.class)
        public String[] degrees;
        @Validate(AgeValidator.class)
        public int age;
        @Validate(ExperienceValidator.class)
        public int experience;

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

If case you use `AgeValidator` of a string field, it will fail during compilation. How it works? `$f` is replaced with the field it is applied to. `$m` refers to the master instance. In `${}` you can write any java code you need to. Before the compilation, `Jeta` will create java code by these strings, so, in case of misspelling it won't be assembled.

###ValidatorAlias

`ValidatorAlias` allows you create your custom annotations to validate with:

    :::java
    @ValidatorAlias(AgeValidator.class)
    public @interface NotYoung {
    }

    @ValidatorAlias(ExperienceValidator.class)
    public @interface NotCheater {
    }

    public class HireAction {
        @NotBlank
        public String name;
        @NotEmpty
        public String[] degrees;
        @NotYoung
        public int age;
        @NotCheater
        public int experience;

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

Of caurse `Jeta` provides aliases for its validators. Look up these in `org.brooth.jeta.validate.alias` package.

###MetaHelper

The validation helper methods would be:

    :::java
    public static void validate(Object master) throws ValidationException {
        new ValidationController(metasitory, master).validate();
    }

    public static List<String> validateSafe(Object master) {
        new ValidationController(metasitory, master).validateSafe();
    }

