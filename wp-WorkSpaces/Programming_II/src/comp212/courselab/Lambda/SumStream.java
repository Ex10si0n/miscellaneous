package comp212.courselab.Lambda;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class SumStream {
    private static int sumStream(ArrayList<Integer> list) {
        return list.stream().filter(i -> i > 10).mapToInt(i -> i).sum();
    }

    public static void main(String[] args) {
        ArrayList<Integer> l = new ArrayList<Integer>();
        l.add(9);
        l.add(10);
        l.add(11);
        l.add(12);
        int sum = sumStream(l);
        System.out.println("Sum: " + sum);

        Stream<Integer> stream = Stream.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15);
        Stream<Integer> stream_1 = Stream.of(new Integer[]{1, 2, 3, 4});
        Stream<String> stream_2 = Stream.generate(() -> {return "abc";});

        stream.map(x -> x * x).filter(x -> x % 2 == 0).forEach(y -> System.out.print(y + " "));
        sum = stream_1.reduce(0, (ans, i) -> ans + i);
        System.out.println("\n" + sum);

        // Convertion
        List<Integer> myList = new ArrayList<>();
        for (int i = 0; i < 10; i++) myList.add(i);
        Stream<Integer> sequentialStream = myList.stream();
        Stream<Integer> parallelStream = myList.parallelStream();

        int[] values = {3, 10, 6, 1, 4, 8, 2, 5, 9, 7};
        System.out.print("Original values: ");
        IntStream.of(values).forEach(value -> System.out.printf("%d ", value));
        System.out.print("\nSorted values: ");
        IntStream.of(values).sorted().forEach(value -> System.out.printf("%d ", value));
        System.out.println("\nSum: " + IntStream.of(values).reduce(0, (x, y) -> x + y));
        System.out.println("Sum Square: " + IntStream.of(values).reduce(0, (x, y) -> x + y * y));

        // PrimeGenerator
        IntStream.range(2, 100).filter(x -> IntStream.range(2, (int)Math.sqrt(x) + 1).filter(t -> x % t == 0).count() == 0).forEach(x -> System.out.print(x + " "));

        String[] strings = {"Red", "Orange", "Yellow", "Green", "Blue", "indigo", "Violet"};
        System.out.printf("\nStrings less than n sorted ascending: %s%n", Arrays.stream(strings).filter(s -> s.compareToIgnoreCase("n") < 0) .sorted(String.CASE_INSENSITIVE_ORDER) .collect(Collectors.toList()));


    }
}

