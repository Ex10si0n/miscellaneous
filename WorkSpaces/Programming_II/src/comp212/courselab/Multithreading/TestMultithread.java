package comp212.courselab.Multithreading;

public class TestMultithread {
    public static void main(String[] args) {
        PrintNum printA = new PrintNum("Annie", 10);
        PrintNum printB = new PrintNum("Bob", 10);

        Thread t1 = new Thread(printA);
        Thread t2 = new Thread(printB);

        t1.start();
        t2.start();
    }
}

