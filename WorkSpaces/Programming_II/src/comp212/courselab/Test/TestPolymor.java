package comp212.courselab.Test;

public class TestPolymor {
    public static void main(String[] args) {
        A a = new A();
        B b = new B();
        C c = new C();

        print(a);
        // print((Object)a);
        print((C)b);
        print((A)c);
    }
    public static void print(C x) {
        System.out.println(x.toString());
    }
}
