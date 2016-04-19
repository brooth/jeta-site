<div class="page-header">
    <h2>Custom Processor</h2>
</div>

*Jeta* allows you to create custom annotation processor and you should take advantage of for sure. In this post, we'll create a processor for our [Hello, World sample](/guide/code-generating.html#HelloWorldSample).

First of all, we must create a separate module since a processor and all the corresponding code is needed at compile time only. Also, this module must be compiled into byte-code before in order to be passed to `javac` as the annotation processor.

There are no special requirements for this module. It is a plain `java` project. Assume we named it *HelloWorldSampleApt* and certainly used `gradle` to build:

    :::groovy
    apply plugin: 'java'

    repositories {
        jcenter()
    }

    dependencies {
        compile 'org.brooth.jeta:jeta-apt:1.1'
        // @SayHello annotation dependency
    }

<span class="label label-info">Note</span> `Apt` module depends on annotations it processes. In our case, we need to create a separate module for `@SayHello` annotation and add this module as the dependency for the `apt` module.

Next, we'll create the processor. Be aware that this processor must implement `org.brooth.jeta.apt.Processor` or simply extends `org.brooth.jeta.apt.processors.AbstractProcessor`.

Pay attension that *Jeta* uses `JavaPoet` framework to generate java source code. Please, go to [square/javapoet site](https://github.com/square/javapoet) on `GitHub`, before you'll write your first processor.

    :::java
    public class SayHelloProcessor extends AbstractProcessor {

        public SayHelloProcessor() {
            super(SayHello.class);
        }

        @Override
        public boolean process(Builder builder, RoundContext roundContext) {
            MetacodeContext context = roundContext.metacodeContext();
            ClassName masterClassName = ClassName.get(context.masterElement());
            builder.addSuperinterface(ParameterizedTypeName.get(
                    ClassName.get(HelloWorldMetacode.class), masterClassName));

            MethodSpec.Builder methodBuilder = MethodSpec.methodBuilder("setHelloWorld")
                    .addAnnotation(Override.class)
                    .addModifiers(Modifier.PUBLIC)
                    .returns(void.class)
                    .addParameter(masterClassName, "master");

            for (Element element : roundContext.elements()) {
                String fieldName = element.getSimpleName().toString();
                methodBuilder.addStatement("master.$L = \"Hello, World!\"", fieldName);
            }

            builder.addMethod(methodBuilder.build());
            return false;
        }
    }

Now, we need to add this module into `apt` classpath. Let's amend dependencies of HelloWorldSample.

    :::groovy
    dependencies {
        apt project(':HelloWorldSampleApt')
        apt 'org.brooth.jeta:jeta-apt:1.1'
        compile 'org.brooth.jeta:jeta:1.1'
    }

Also, say to `Jeta` use our processor. To do that we add the option into `jeta.processing`:

    :::properties
    processors.add = com.example.apt.SayHelloProcessor

You can find similar example on [GitHub](https://github.com/brooth/jeta-samples).
