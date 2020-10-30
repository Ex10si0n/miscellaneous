package comp212.courselab;

import java.util.ArrayList;
import java.util.Scanner;

public class Stack {
    private ArrayList<Object> list = new ArrayList<>();

    public boolean isEmpty() {
        return list.isEmpty();
    }

    public int getSize() {
        return list.size();
    }

    public Object peek() {
        return list.get(getSize() - 1);
    }

    public Object pop() {
        Object o = list.get(getSize() - 1);
        list.remove(getSize() - 1);
        return o;
    }

    public void push(Object o) {
        list.add(o);
    }

    @Override
    public String toString() {
        return "stack: " + list.toString();
    }

    public static void main(String[] args) {
        Stack s = new Stack();
        Scanner scan = new Scanner(System.in);
        while (true) {
            System.out.print("[push]> ");
            String obj = scan.nextLine();
            if (obj.equals("pop")) {
                System.out.println("Pop: " + s.pop());
            }
            else
                s.push(obj);
            System.out.println(s);
        }
    }
}
