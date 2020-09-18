## Object-Oriented Overview
### Class
```java
public class SimpleLocation {

  // Member/instance variables
  public double latitude;
  public double longitude;

  // Class variables
  public static String copyright;

  // Constructor
  public SimpleLocation(double lat, double lon) {
    this.latitude = lat;
    this.longitude = lon;
  }

  // Overloading Constructor Method
  public SimpleLocation() {
    this.latitude = 0;
    this.longitude = 0;
  }

  public void showLocation() {
    System.out.print("latitude: " + this.latitude);
    System.out.print("longitude: " + this.longitude);
  }

  public double distance(SimpleLocation others) {...}
}
```

### Instantiate
```java
// Instantiate in Main
SimpleLocation ipm = new SimpleLocation(22.19, 113.55);
```

### Calling Object
```java
// callingObject.MethodName(others, ...)
ipm.distance(borderGate)
```

### Overloading
Over loading methods can make programs clearer and more readable.
Mehods that perform the same function with different types of
parameters should be given the same name.

## Memory Models
### Primitive Type vs. Object Type
```java
int var1 = 46;
SimpleLocation location = new SimpleLocation();
```
var1     [46]
location [  ] -> Object Heap(@56 -> [SimpleLocation Object]) [location]
ipm      [  ] -> Object Heap(@55 -> [SimpleLocation Object]) [ipm]
```java
ipm = location
```
location [  ] -> Object Heap(@55 -> [SimpleLocation Object]) [ipm]
ipm      [  ] -> Object Heap(@55 -> [SimpleLocation Object]) [ipm]

### Public vs. Private
Encapsulation(封装) Mechanism
```java
public class SimpleLocation {
  // Cannoy access private variables by callingObject
  private double latitude;
  private double longitude;

  // Getter
  public double getLatitude() {
    // Can return private variables
    return this.latitude;
  }

  // Setter
  public double setLatitude(double lat) {
    this.latitude = lat;
  }
}
```

### UML Notation
```
+----------------+
| SimpleLocation |
+----------------+
| latitude       |
| longitude      |
| setLatitude()  |
+----------------+
```

### Classes from Java Library
```java
import java.util.Random;

[Main] {
  Random randGen = new Random(376482);
  for (int i = 0; i < 10; i++) {
    System.out.print(randGen.nextInt(1000) + " ");
  }
}
```

### Static Variables, Constants, Methods
```java
public class Dog {
  public String name;
  public static dog_numbers; // static variable
  final double PI = Math.acos(-1);
  ...
  public InstanceMethod() {...}
  public static StaticMethod() {...} // Dog.StaticMethod() e.g. Math.cos(x)
}
```


