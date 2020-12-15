package comp212.courselab.Exception;

import java.util.Scanner;

public class Try {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter two integers: ");
        int number1 = input.nextInt();
        int number2 = input.nextInt();

        try {
            int result = number1 / number2;
            System.out.println(number1 + "/" + number2 + result);
        } catch (ArithmeticException ex) {
            System.out.println("Cannot be divided by zero");
        }

        System.out.println("Program Running...");
    }
}
