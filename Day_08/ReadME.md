# Simplifying Java Development with Switch Expressions, Var, Sealed Classes, Record Classes, Text Blocks, and String Templates

## Switch Expressions:

Switch expressions, introduced in Java 12, allow us to write more expressive code when dealing with multiple branching conditions. They can be used as expressions that return a value example:

```java
int dayOfWeek = 3;
String dayName = switch (dayOfWeek) {
    case 1 -> "Monday";
    case 2 -> "Tuesday";
    case 3 -> "Wednesday";
    case 4 -> "Thursday";
    case 5 -> "Friday";
    case 6, 7 -> "Weekend";
    default -> "Invalid day";
};
System.out.println("Today is " + dayName);
```

## Var:

The keyword ‘var’, introduced in Java 10, allows us to declare variables with type inference, reducing boilerplate code. It infers the type based on the assigned value, making the code more concise. Here's an example:

```java
var name = "John Doe";
var age = 25;
var isStudent = true;
System.out.println(name + " is " + age + " years old.");
```

## Sealed Classes:

Sealed classes, introduced in Java 15, provide a way to define a limited set of subclasses for a class. By explicitly declaring which subclasses are allowed, example:

```java
public sealed class Shape permits Circle, Rectangle, Triangle {
    //Common methods & fields
}

final class Circle extends Shape {
    //Circle specific implementation
}

final class Rectangle extends Shape {
    //Rectangle specific implementation
}

final class Triangle extends Shape {
    //Triangle specifcic implementation
}
```

## Record Classes:

Record classes, introduced in Java 14, offer a concise way to define classes that are primarily used for storing data. They automatically generate standard methods like equals(), hashCode(), and toString(). Example:

```java
record Person(String name, int age) {
    //Additional methods and fields
}

Person person = new Person("Alice", 30);
System.out.println(person);
```

## Text Blocks:

Text Blocks, introduced in Java 13, simplify the creation of multiline strings. They allow for easy formatting, including line breaks and indentation, enhancing code readability. Here is an example:

```java
String html = """
    <html>
        <body>
            <h1>Welcome</h1>
            <p>Hello, world!</p>
        </body>
    </html>
    """;
System.out.println(html);
```

## String Templates:

String Templates, introduced in Java 15, simplify string concatenation by allowing expressions to be directly embedded within a string literal. example:

```java
String name = "Alice";
int age = 30;
String message = String.format("My name is %s and I'm %d years old.", name, age);
System.out.println(message);
```
