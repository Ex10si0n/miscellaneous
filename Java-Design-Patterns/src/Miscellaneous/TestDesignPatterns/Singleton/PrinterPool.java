package Miscellaneous.TestDesignPatterns.Singleton;

import java.util.ArrayList;

public class PrinterPool {
    private static int inkLevel;
    private static ArrayList<String> printerQueue;
    private static final PrinterPool instance = new PrinterPool();

    private PrinterPool() {
        inkLevel = 100;
        printerQueue = new ArrayList<String>();
    }

    private static PrinterPool getInstance() {
        return instance;
    }

    private void printFile(String fileName) {
        System.out.println("[Printing] " + fileName);
        printerQueue.add(fileName);
        inkLevel -= fileName.length();
    }

    public static void main(String[] args) {
        PrinterPool printer1, printer2, printer3;
        printer1 = PrinterPool.getInstance();
        printer1.printFile("test file 1.txt");
        System.out.println("ink level: " + PrinterPool.inkLevel);
        printer2 = PrinterPool.getInstance();
        printer2.printFile("test file 2.txt");
        System.out.println("ink level: " + PrinterPool.inkLevel);
        printer3 = PrinterPool.getInstance();
        printer3.printFile("test file 3.doc");
        System.out.println("ink level: " + PrinterPool.inkLevel);
        System.out.println("queue: " + PrinterPool.printerQueue);
    }
}
