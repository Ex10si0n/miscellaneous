package comp212.courselab.Exercises;

import java.util.ArrayList;
import java.util.Date;

public class ArrayTest {

    public static void main(String[] args) {
        ArrayList<Object> arr = new ArrayList<>();
        Date date = new Date();
        arr.add(date);
        String str = "Hello";
        arr.add(str);

        // Traversal#1
        for (int i = 0; i < arr.size(); i++) {
            System.out.println(arr.get(i));
        }

        // Traversal#2
        for (Object o : arr) {
            System.out.println(o);
        }
    }
}
