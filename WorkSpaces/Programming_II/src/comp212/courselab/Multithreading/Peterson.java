package comp212.courselab.Multithreading;

import java.util.concurrent.TimeUnit;

public class Peterson implements Runnable {
    int cs = 0;
    boolean flag_0 = false;
    boolean flag_1 = false;
    int turn = 0;

    void thread_0() throws InterruptedException {
        flag_0 = true;
        turn = 1;
        while (flag_1 && turn == 1);
        for (int i = 0; i < 10; i++) {
            cs += 1;
            System.out.println("Thread_0: cs=" + cs);
            // TimeUnit.SECONDS.sleep(1);
        }
        flag_0 = false;
    }

    void thread_1() throws InterruptedException {
        flag_0 = false;
        turn = 0;
        while (flag_0 && turn == 0) ;
        for (int i = 0; i < 10; i++) {
            cs += 100000;
            System.out.println("Thread_1: cs=" + cs);
            // TimeUnit.SECONDS.sleep(1);
        }
        flag_1 = false;
    }

    // Thread t0 = new Thread(thread_0);
    // Thread t1 = new Thread(thread_1);

    @Override
    public void run() {

    }
}
