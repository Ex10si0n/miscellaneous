package aspires.generic;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class Sender {
    public static void sendMsg(String className, String methodName, String value) {
        try {
            Class<?> myClass = Class.forName(className);
            Class<?>[] myParas = new Class[1];
            myParas[0] = String.class;
            Method myMethod = myClass.getDeclaredMethod(methodName, myParas);
            myMethod.invoke(myClass.newInstance(), value);

        } catch (ClassNotFoundException | NoSuchMethodException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InstantiationException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        }
    }
}
