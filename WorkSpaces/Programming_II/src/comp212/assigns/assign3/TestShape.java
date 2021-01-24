package comp212.assigns.assign3;

import java.util.ArrayList;

public class TestShape {
    public static Shape minShape(Shape[] a) {
        double minArea = a[0].calculateArea();
        int minId = 0;
        for (int i = 1; i < a.length; i++) {
            double iArea = a[i].calculateArea();
            if (iArea < minArea) {
                minArea = iArea;
                minId = i;
            }
        }
        return a[minId];
    }

    public static void main(String[] args) {
        Rectangle r1 = new Rectangle(3, 5);
        Rectangle r2 = new Rectangle(2, 8);
        Triangle t1 = new Triangle(3, 4, 5);
        Triangle t2 = new Triangle(4, 4, 4);
        Shape[] shapeSet = {r1, r2, t1, t2};
        System.out.println(minShape(shapeSet).toString());
        Rectangle r3 = new Rectangle(9, 9);
        ArrayList<Shape> shapeArr = new ArrayList<Shape>();
        shapeArr.add(r1);
        shapeArr.add(r2);
        shapeArr.add(r3);
        shapeArr.add(t1);
        shapeArr.add(t2);
        Shape shapeHaslongestLine = shapeArr.get(0);
        double maxLine = shapeArr.get(0).LongestLine();
        for (int i = 1; i < shapeArr.size(); i++) {
            double iLine = shapeArr.get(i).LongestLine();
            if (iLine > maxLine) {
                maxLine = iLine;
                shapeHaslongestLine = shapeArr.get(i);
            }
        }
        System.out.println(shapeHaslongestLine);
    }
}
