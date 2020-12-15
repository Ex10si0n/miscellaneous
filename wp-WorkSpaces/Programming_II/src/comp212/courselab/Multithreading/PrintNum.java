package comp212.courselab.Multithreading;

import java.util.concurrent.TimeUnit;

public class PrintNum implements Runnable{

    private int lastNum;
    private String threadName;

    public PrintNum(String name, int times) {
        this.lastNum = times;
        this.threadName = name;
    }

    PrintNum (int n) {
        this.lastNum = n;
    }

    @Override
    public void run() {
        for (int i = 1; i <= this.lastNum; i++) {
            System.out.println(threadName + ": " + i);
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

}
