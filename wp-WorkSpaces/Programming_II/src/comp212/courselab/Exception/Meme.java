package comp212.courselab.Exception;

import java.util.Scanner;

public class Meme {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String name;
        System.out.print("Enter Your Name: ");
        name = input.nextLine();
        try {
            if (name.equals("Steve")) {
                int e = 1 / 0;
            }
            System.out.println("Hi, " + name);
        } catch (ArithmeticException e) {
            throw new RuntimeException("That guy is so handsome that cause an Exception.");
        }

    }
}
