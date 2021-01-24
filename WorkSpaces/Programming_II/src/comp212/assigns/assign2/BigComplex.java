package comp212.assigns.assign2;

import java.math.BigDecimal;

public class BigComplex {
    private BigDecimal real = java.math.BigDecimal.valueOf(0.0);
    private BigDecimal imaginary = java.math.BigDecimal.valueOf(0.0);

    public BigComplex (BigDecimal real, BigDecimal imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    public BigComplex(double v, double v1) {
        this.real = java.math.BigDecimal.valueOf(0);
        this.imaginary = java.math.BigDecimal.valueOf(0);
    }

    public BigComplex add(BigComplex z) {
        return new BigComplex(this.real.add(z.real), this.imaginary.add(z.imaginary));
    }

    public BigComplex subtract(BigComplex z) {
        return new BigComplex(this.real.subtract(z.real), this.imaginary.subtract(z.imaginary));
    }

    public BigComplex multiply(BigComplex z) {
        return new BigComplex(this.real.multiply(z.real).subtract(this.imaginary.multiply(z.imaginary)), this.real.multiply(z.imaginary).add(this.imaginary.multiply(z.real)));
    }

    public String toString() {
        return real + "+" + imaginary + "i";
    }
}
