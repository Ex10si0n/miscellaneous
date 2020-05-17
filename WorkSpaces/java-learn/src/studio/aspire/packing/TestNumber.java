package studio.aspire.packing;

import java.nio.file.FileSystemNotFoundException;

public class TestNumber {
    public static void main(String[] args) {
        int i = 5;
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



    }
}
