package DecoratorPattern;

public class Main {
    public static void main(String[] args) {
        Shape circle = new Circle();
        ShapeDecorator redCircle = new RedShapeDecorator(new Circle());
        ShapeDecorator redTriangle = new RedShapeDecorator(new Triangle());

        System.out.println("Circle with normal border");
        circle.draw();;

        System.out.println("\nCircle of red border");
        redCircle.draw();

        System.out.println("\nTriangle of red border");
        redTriangle.draw();
    }
}
