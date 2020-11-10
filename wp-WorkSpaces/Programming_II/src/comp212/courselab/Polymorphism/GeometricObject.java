package comp212.courselab.Polymorphism;

public abstract class GeometricObject {
    private boolean filled;
    private String color;
    public String type;
    public GeometricObject(boolean isFilled, String color) {
        this.filled = isFilled;
        this.color = color;
    }
    public GeometricObject() {}
    public abstract double area();
    public abstract double perimeter();
    public String color() {
        return this.color;
    }
    public boolean isFilled() {
        return this.filled;
    }
    public String type() { return this.type; }
}
