package studio.aspire.packing;

import java.nio.file.FileSystemNotFoundException;

public class TestNumber {
    // 可重载
    public static int toInteger(String str) { return Integer.parseInt(str); }
    public static String toString(int i) { return String.valueOf(i); }

    public static void main(String[] args) {
        int i = 5;

        // 测试 * 方法
        System.out.println(toInteger("12345"));
        System.out.println(toString(23333));


        // 基本类型 to 封装类型
        Integer integer = new Integer(i);

        // 自动转换 (装箱)
        Integer integer1 = i;

        // 封装类型 to 基本类型 (拆箱)
        int i_1 = integer.intValue();
        int i_2 = integer; //自动转换 (拆箱)

        // int 的封装类
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE);

        // 数字转字符串方法一: 用String类的valueOf方法
        String string = String.valueOf(i);

        // 数字转字符串方法二: 将基本类型装箱，调用Integer类的静态方法toString
        Integer integer2 = i;
        String string2 = integer2.toString();

        System.out.println(string + " " + string2);

        // 字符串转为数字:
        float num = Float.parseFloat(String.valueOf(3.1415926f));
        System.out.println(num);
        

    }
}
