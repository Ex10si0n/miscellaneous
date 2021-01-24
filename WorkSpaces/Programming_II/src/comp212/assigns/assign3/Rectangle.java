package comp212.assigns.assign3;

public class Rectangle extends Shape implements MadeOfStraightLines{

    private double width;
    private double height;
    private final String type = "Rectangle";

    public Rectangle() {
        super();
        this.width = 1.0;
        this.height = 1.0;
    }
    public Rectangle(double width, double height) {
        super();
        this.width = width;
        this.height = height;
    }
    public double getWidth() {
        return width;
    }
    public void setWidth(double width) {
        this.width = width;
    }
    public double getHeight() {
        return height;
    }
    public void setHeight(double height) {
        this.height = height;
    }
    public String getType() {
        return this.type;
    }
    public boolean equals(Rectangle r) {
        if (this.height == r.height && this.width == r.width) return true;
        else return false;
    }

    @Override
    public double calculateArea() {
        return this.height * this.width;
    }
    @Override
    public double calculatePerimeter() {
        return (this.height + this.width) * 2;
    }
    @Override
    public String toString() {
        return "This is a " + this.type + " and has " + this.height +" height, " + this.width + " width.";
    }

    @Override
    public double LongestLine() {
        if (this.width >= this.height) return this.width;
        else return this.height;
    }
}

