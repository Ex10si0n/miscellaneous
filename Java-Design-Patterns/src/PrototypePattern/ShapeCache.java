package PrototypePattern;

import java.util.Hashtable;

public class ShapeCache {

    private static Hashtable<String, Shape> shapeMap = new Hashtable<>();

    public static Shape getShape(String shapId) {
        Shape cachedShape = shapeMap.get(shapId);
        return (Shape) cachedShape.clone();
    }

    public static void loadCache() {
        Circle circle = new Circle();
        circle.setId("1");
        shapeMap.put(circle.getId(), circle);

        Square square = new Square();
        square.setId("2");
        shapeMap.put(square.getId(), square);

        Triangle triangle = new Triangle();
        triangle.setId("3");
        shapeMap.put(triangle.getId(), triangle);

    }
}
