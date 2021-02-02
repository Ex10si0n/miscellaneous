package aspires.relationship.abstraction;

public abstract class Shape {
    /*
    * Abstract Method:
    */
    public abstract double getArea();
    public abstract double getPerimeter();

    public String getName() {
        return this.getClass().getSimpleName();
    }

    public void showInfo() {
        System.out.println(getName() + " Information");
        System.out.println("Area: " + getArea());
        System.out.println("Perimeter: " + getPerimeter());
    }

}
