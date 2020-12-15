package comp212.courselab.Collection;

import java.util.ArrayList;
import java.util.Iterator;

public class TestCollection {
    public static void main(String[] args) {
        ArrayList<String> collection1 = new ArrayList<>();
        collection1.add("New York");
        collection1.add("Portland");
        collection1.add("Atlanta");
        System.out.println("List of cities in collection-1");
        System.out.println(collection1);

        ArrayList<String> collection2 = new ArrayList<>();
        collection2.addAll(collection1);
        System.out.println("List of cities in collection-2");
        System.out.println(collection2);

        ArrayList<String> collection3 = (ArrayList<String>)(collection1.clone());
        System.out.println("List of cities in collection-3");
        System.out.println(collection3);

        // Using iterator to iterate collection arrayList
        Iterator<String> iterator = collection1.iterator();
        System.out.print("[Iterator] ");
        while (iterator.hasNext()) {
            System.out.print(iterator.next().toUpperCase() + " ");
        }
        System.out.println();

        // Using for-each loop
        System.out.print("[ForEach] ");
        for (String element: collection1)
            System.out.print(element.toUpperCase() + " ");
        System.out.println();

    }
}
