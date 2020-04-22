package studio.aspire;

public class Display {
    public static void print() {
        System.out.println("================= Variable List ================");
        for(int i = 0; i < Variable.var; i++) {
            System.out.println(Variable.varList[i] + ": " + Variable.doubleValue[i]);
        }
    }
}
