package comp212.assigns.assign3;

import static java.util.Arrays.sort;

public class Triangle extends Shape implements MadeOfStraightLines{

    private double[] sides;
    private final String type;

    public Triangle() {
        super();
        this.type = "triangle";
        this.sides = new double[]{0, 0, 0};
    }

    public Triangle(double[] sides) {
        super();
        this.type = "triangle";
        this.sides = sides;
    }

    public Triangle(double a, double b, double c) {
        super();
        this.type = "triangle";
        this.sides = new double[]{a, b, c};
    }

    public double[] getSides() {
        return this.sides;
    }

    public void setSides(double[] sides) {
        this.sides = sides;
    }

    public String getType() {
        return this.type;
    }

    public String toString() {
        return "This is a " + this.type + " and sides are " + this.sides[0] + ", " + this.sides[1] + ", " + this.sides[2] + ".";
    }

    @Override
    public double calculateArea() {
        double s = this.calculatePerimeter() / 2.0;
        return Math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]));
    }

    @Override
    public double calculatePerimeter() {
        return this.sides[0] + this.sides[1] + this.sides[2];
    }

    public boolean equals(Triangle t) {
        double[] cmpA, cmpB;
        cmpA = this.sides;
        cmpB = t.sides;
        sort(cmpA);
        sort(cmpB);
        if (cmpA[0] == cmpB[0] && cmpA[1] == cmpB[1] && cmpA[2] == cmpB[2]) return true;
        else return false;
    }

    @Override
    public double LongestLine() {
        double[] sortedSides = this.sides;
        sort(sortedSides);
        return sortedSides[2];
    }
}
