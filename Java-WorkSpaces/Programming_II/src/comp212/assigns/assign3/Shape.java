package comp212.assigns.assign3;

public abstract class Shape implements Comparable<Shape> {

    private String color;
    private final String type;
    private boolean filled;

    // non-arg Constructor
    public Shape() {
        this.color = "white";
        this.type = "shape";
    }

    // constructor has two arguments
    public Shape(String color, boolean filled) {
        this();
        this.color = color;
        this.filled = filled;
    }

    // setters and getters
    public String getColor() {
        return color;
    }
    public void setColor(String color) {
        this.color = color;
    }
    public boolean isFilled() {
        return filled;
    }
    public void setFilled(boolean filled) {
        this.filled = filled;
    }
    public String getType() {
        return type;
    }

    // override toString method
    @Override
    public String toString() {
        return "\nThe "+ type +"has "+ color +" color and filled: " + filled;
    }

    @Override
    public int compareTo(Shape o) {
        if (this.calculateArea() - o.calculateArea() > 0) return 1;
        else if (this.calculateArea() - o.calculateArea() == 0) return 0;
        else return -1;
    }

    public abstract double calculateArea();
    public abstract double calculatePerimeter();

    public abstract double LongestLine();
}
