package comp212.courselab.Polymorphism;

public class PolymorphismDemo {

    public static void main(String[] args) {
        displayObject(new Triangle(3, 3, 3, true, "Red"));
        displayObject(new Circle(3, true, "Green"));
    }

    public static void displayObject(GeometricObject object) {
        System.out.println("Type: " + object.type());
        System.out.println("Color: " + object.color());
        System.out.println("Filled: " + object.isFilled());
        // Polymorphism
        System.out.println("Perimeter: " + object.perimeter());
        System.out.println("Area: " + object.area());
        System.out.println();
    }

}

