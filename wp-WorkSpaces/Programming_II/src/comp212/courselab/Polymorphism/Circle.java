package comp212.courselab.Polymorphism;

public class Circle extends GeometricObject{

    private double radius;

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }

    @Override
    public double perimeter() {
        return Math.PI * 2 * radius;
    }

    public Circle(double radius, boolean isFilled, String color) {
        super(isFilled, color);
        this.type = "Circle";
        this.radius = radius;
    }
}
