package comp212.courselab.GUI;

import javax.swing.*;
import java.awt.*;

public class Calculator {

    /*
    * Calculator Class
    * This Class is for implementing
    * GridLayout
    *
    * By Ex10si0n*/

    public static void main(String[] args) {
        JFrame calculatorUI = new JFrame("Calculator UI");
        calculatorUI.setBounds(50, 50, 200, 180);
        calculatorUI.setLayout(new GridLayout(4, 5, 8, 8));
        String[] arr = {"7", "8", "9", "/", "sqrt", "4", "5", "6", "*", "%", "1", "2", "3", "-", "^-1", "0", "+/-", ".", "+", "="};
        for (int i = 0; i < 20; i++) {
            calculatorUI.add(new JButton(arr[i]));
        }
        calculatorUI.setVisible(true);
    }
}

