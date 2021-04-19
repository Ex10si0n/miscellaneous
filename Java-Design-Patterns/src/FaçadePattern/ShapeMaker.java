package FaçadePattern;

public class ShapeMaker {
    private Shape circle;
    private Shape triangle;
    private Shape square;

    public ShapeMaker() {
        circle = new Circle();
        triangle = new Triangle();
        square = new Square();
    }

    public void drawCircle() { circle.draw(); }
    public void drawTriangle() { triangle.draw(); }
    public void drawSquare() { square.draw(); }

}
