package studio.aspire.packing;

public class TestMaths {
    public static int myRound(float float_num) {
        return (int) Math.floor(float_num + 0.5);
    }
    public static void main(String[] args) {
        float f1 = 5.4f;
        System.out.println(Math.round(f1));
        System.out.println(Math.round(f1 + 0.1f));
        System.out.println(myRound(f1));
        System.out.println(myRound(f1 + 0.1f));
        System.out.println(Math.random());
        System.out.println(Math.sqrt(2));
        System.out.println(Math.pow(2, 0.5));
        System.out.println(Math.PI);
        System.out.println(Math.E);

        // ex-01
        double exp = 0;
        int n = Integer.MAX_VALUE;
        exp += Math.pow((1 + 1.0 / (float) n), n);

        System.out.println("\n===== 计算自然对数 =====");
        System.out.println(Math.E);
        System.out.println(exp);


    }
}
