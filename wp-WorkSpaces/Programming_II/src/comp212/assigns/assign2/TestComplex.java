package comp212.assigns.assign2;

import java.math.BigDecimal;

public class TestComplex {
    public static void main(String[] args) {

        Complex ans = new Complex(1, 2);
        for(int i = 2; i <= 160; i++)
            ans = ans.multiply(new Complex(i, i + 1));
        System.out.println(ans);


        BigComplex bigAns = new BigComplex(new BigDecimal(1), new BigDecimal(2));
        for (int i = 2; i <= 160; i++)
            bigAns = new BigComplex(new BigDecimal(i), new BigDecimal(i+1)).multiply(bigAns);
        System.out.println(bigAns);

    }
}
