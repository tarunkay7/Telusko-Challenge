## Reflection API

The Reflection API in Java allows you to inspect and manipulate the structure and behavior of classes, methods, and fields at runtime. It gives you the ability to obtain information about classes (like their name, fields, and methods) and perform actions such as creating instances, calling methods, and accessing or modifying fields dynamically, even if they are private.
You can use this information to understand and interact with the class in ways that wouldn't normally be possible at compile-time.

For example, with reflection, you can find out the names of all the methods in a class, invoke a specific method dynamically based on user input, or modify the value of a private field.

Reflection is often used in advanced scenarios, such as frameworks, libraries, or tools that need to work with classes dynamically. It provides flexibility and the ability to work with classes in a more dynamic and introspective manner. However, it's important to note that reflection should be used judiciously as it can introduce complexity and may have performance implications.


### I am implementing a basic usage of Reflection API Here

```java
import java.lang.reflect.Method;

public class ReflectionExample {
    public static void main(String[] args) throws Exception {
        Class<?> clazz = MyClass.class;

        Method[] methods = clazz.getDeclaredMethods();

        
        for (Method method : methods) {
            System.out.println("Method name: " + method.getName());
        }
    }
}

class MyClass {
    public void method1() {
        System.out.println("Method 1 called.");
    }

    public void method2(String message) {
        System.out.println("Method 2 called with message: " + message);
    }
}
```
we have a class called `MyClass` with two methods. The `ReflectionExample` class demonstrates how to use reflection to obtain the class object for `MyClass`. Then, it retrieves all the declared methods of the class using `getDeclaredMethods()` and iterates through them to print their names.

As part of assignment here are a few things that i have explored

Certainly! Here's a sample Java code that checks if a given class implements an interface:

```java
public class InterfaceCheckExample {
    public static void main(String[] args) {
        Class<?> classToCheck = MyClass.class;
        Class<?> interfaceToCheck = MyInterface.class;

        boolean isInterface = interfaceToCheck.isInterface();
        boolean implementsInterface = interfaceToCheck.isAssignableFrom(classToCheck);

        System.out.println("Interface to Check: " + interfaceToCheck.getSimpleName());
        System.out.println("Is an Interface? " + isInterface);
        System.out.println("Does " + classToCheck.getSimpleName() + " implement " +
                interfaceToCheck.getSimpleName() + "? " + implementsInterface);
    }
}

interface MyInterface {
    void someMethod();
}

class MyClass implements MyInterface {
    public void someMethod() {
        // Implementation of the interface method
    }
}
```

The code first assigns the class and interface to be checked. It then uses the `isInterface()` method to determine if the given interface is indeed an interface. Next, the `isAssignableFrom()` method is used to check if the class implements the interface.



