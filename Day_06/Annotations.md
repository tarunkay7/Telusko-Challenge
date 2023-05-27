# Annotations
Annotations in Java provide a way to add metadata, instructions, or markers to your code that can be processed at compile-time or runtime

Annotations can be used for a variety of purposes, such as:

1. Documentation: Annotations can serve as documentation by providing additional information about the code. For example, the `@Deprecated` annotation marks a deprecated element to indicate that it should no longer be used.

2. Compile-time checks: Annotations enable compile-time checks and validation. For example, the `@Override` annotation ensures that a method is intended to override a superclass method, helping to catch accidental mistakes.

3. Runtime behavior: Annotations can modify the runtime behavior of classes or methods. Frameworks like Spring and JPA use annotations extensively to configure and control the behavior of the application.

4. Code generation: Annotations can be used to generate code or resources during the build process. Tools like Lombok use annotations to automatically generate getter and setter methods, reducing boilerplate code.

Now this is a simple implementation of the code

```java
import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface MyAnnotation {
    String value();
}

public class AnnotationExample {
    @MyAnnotation("Hello, Annotation!")
    public void myMethod() {
        // Method implementation
    }

    public static void main(String[] args) throws Exception {
        AnnotationExample example = new AnnotationExample();
        Class<?> clazz = example.getClass();
        Method method = clazz.getMethod("myMethod");

        if (method.isAnnotationPresent(MyAnnotation.class)) {
            MyAnnotation annotation = method.getAnnotation(MyAnnotation.class);
            System.out.println(annotation.value());
        }
    }
}
```

I define a custom annotation called `MyAnnotation` using the `@interface` syntax. The annotation is then applied to the `myMethod()` method in the `AnnotationExample` class.

At runtime, the `main` method reflects on the class and checks if the `myMethod()` method has the `MyAnnotation` present. If the annotation is present, it retrieves the annotation instance and prints its value.

Restriction levels, or retention policies, determine how long the annotations are retained and available. Java provides three retention policies:

1. `RetentionPolicy.SOURCE`: Annotations are retained only during the source file compilation and are not available at runtime.

2. `RetentionPolicy.CLASS`: Annotations are retained in the compiled bytecode but are not accessible at runtime. This is the default retention policy if not specified.

3. `RetentionPolicy.RUNTIME`: Annotations are retained in the compiled bytecode and are available for reflection and processing at runtime.

The `@Retention(RetentionPolicy.RUNTIME)` annotation is used to specify that the `MyAnnotation` should be available at runtime.
