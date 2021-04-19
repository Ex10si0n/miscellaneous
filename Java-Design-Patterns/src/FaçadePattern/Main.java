package FaçadePattern;

public class Main {
    public static void main(String[] args) {
        ShapeMaker shapeMaker = new ShapeMaker();

        shapeMaker.drawCircle();
        shapeMaker.drawTriangle();
        shapeMaker.drawSquare();
    }
}
