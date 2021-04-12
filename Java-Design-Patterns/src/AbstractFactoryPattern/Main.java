package AbstractFactoryPattern;

public class Main {
    public static void main(String[] args) {
        AbstractFactory shapeFactory = FactoryProducer.getFactory("Shape");
        Shape shape1 = shapeFactory.getShape("Circle");
        Shape shape2 = shapeFactory.getShape("Triangle");
        Shape shape3 = shapeFactory.getShape("Square");
        shape1.draw();
        shape2.draw();
        shape3.draw();
        AbstractFactory colorFactory = FactoryProducer.getFactory("Color");
        Color color1 = colorFactory.getColor("Red");
        Color color2 = colorFactory.getColor("Green");
        Color color3 = colorFactory.getColor("Blue");
        color1.fill();
        color2.fill();
        color3.fill();
    }
}
