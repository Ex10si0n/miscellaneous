package comp212.courselab.Polymorphism;

public class Triangle extends GeometricObject{
    private double a;
    private double b;
    private double c;
    public double perimeter() {
        return this.a + this.b + this.c;
    }
    public double area() {
        double s = this.perimeter() / 2.0;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
    public Triangle(double a, double b, double c, boolean isFilled, String color) {
        super(isFilled, color);
        this.type = "Triangle";
        this.a = a;
        this.b = b;
        this.c = c;
    }
    public static void main(String[] args) {
        Triangle t = new Triangle(3, 4, 5, true, "blue");
        System.out.println(t.area());
    }
}
