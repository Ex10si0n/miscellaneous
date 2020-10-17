package comp212.assigns.assign2;

public class Complex {
    private double real = 0;
    private double imaginary = 0;

    public Complex(double real, double imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    public Complex() {
        this.real = 0;
        this.imaginary = 0;
    }

    public Complex add(Complex z) {
        return new Complex(this.real + z.real, this.imaginary + z.imaginary);
    }

    public Complex substract(Complex z) {
        return new Complex(this.real - z.real, this.imaginary - z.imaginary);
    }

    public Complex multiply(Complex z) {
        return new Complex(this.real * z.real - this.imaginary * z.imaginary, this.real * z.imaginary + this.imaginary * z.real);
    }

    public String toString() {
        return real + "+" + imaginary + "i";
    }
}
