package SingletonPattern;

public class HurrySingleton {
    private static HurrySingleton instance = new HurrySingleton();

    private HurrySingleton() {
    }

    public static HurrySingleton getInstance() {
        return instance;
    }
}
