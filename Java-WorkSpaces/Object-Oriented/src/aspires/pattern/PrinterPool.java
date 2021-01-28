package aspires.pattern;

public class PrinterPool {
    private static PrinterPool instance = new PrinterPool();
    private PrinterPool() {
        System.out.println("Printer Pool is an Singleton, You can get the instance via getInstance() Method");
    }

    public static PrinterPool getInstance() {
        return instance;
    }

}
