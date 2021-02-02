package aspires.pattern;

public class PrinterPool {
    /*
    * Class PrinterPool - a Demo of implementing Singleton Pattern
    * It cannot create object manually, it always returns the unique
    * object that was create at the first time declaring as private
    * at the start of class codes.
    */
    private static PrinterPool instance = new PrinterPool();

    private PrinterPool() {
        System.out.println("Printer Pool is an Singleton, You can get the instance via getInstance() Method");
    }

    public static PrinterPool getInstance() {
        return instance;
    }

}
