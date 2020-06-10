/*
A Terrible Programming Language not so terrible (=0w0)=
Copyright. Ex10si0n - Aspire Studio - 2019
*/
package studio.aspire;
import java.util.Scanner;

public class Main {

    public static boolean checkBuffer(String arg) {
        return true;
    }
    public static void runArg(String arg) {
        //Clear Vars
        if(arg.charAt(0) == 'c' && arg.charAt(1) == 'l' && arg.charAt(2) == 'e' && arg.charAt(3) == 'a' && arg.charAt(4) == 'r') {
            Variable.clear();
        }
        //undo Vars
        if(arg.charAt(0) == 'u' && arg.charAt(1) == 'n' && arg.charAt(2) == 'd' && arg.charAt(3) == 'o' && Character.isAlphabetic(arg.charAt(4))){
            Variable.undo(arg.charAt(4));
        }
        //Help Document
        else if(arg.charAt(0) == 'h' && arg.charAt(1) == 'e' && arg.charAt(2) == 'l' && arg.charAt(3) == 'p') {
            Help.getHelp();
        }
        //take the Answer to Variable
        else if(arg.length() == 1 && 'A' < arg.charAt(0) && arg.charAt(0) <= 'Z') {
            Variable.newVar(arg.charAt(0), Variable.doubleValue[0]);
        }
        //new Variable or overwrite a Variable
        else if(arg.length() > 1 && 'A' <= arg.charAt(0) && arg.charAt(0) <= 'Z' && arg.charAt(1) == '=') {
            int exp = (arg.length() - 2);
            double val = 0;
            for(int i = 1; i <= exp; i++) {
                val += (arg.charAt(1 + i) - '0') * Math.pow(10, exp - i);
            }
            Variable.newVar(arg.charAt(0), val);
        }
        //calculate numbers
        else if(Character.isDigit(arg.charAt(0))) {
            int br = 0; double val1 = 0, val2 = 0;
            for(int i = 0; i < arg.length(); i++) {
                if (!Character.isDigit(arg.charAt(i))) {
                    br = i;
                    break;
                }
            }
            for(int j = 0; j < br; j++) {
                val1 += (arg.charAt(j) - '0') * Math.pow(10, br - j - 1);
            }
            for(int j = br + 1; j < arg.length(); j++) {
                val2 += (arg.charAt(j) - '0') * Math.pow(10, arg.length() - 1 - j);
            }
            switch (arg.charAt(br)) {
                case '+': Variable.doubleValue[0] = val1 + val2; break;
                case '-': Variable.doubleValue[0] = val1 - val2; break;
                case '*': Variable.doubleValue[0] = val1 * val2; break;
                case '/': Variable.doubleValue[0] = val1 / val2; break;
            }
        }
        //Syntactic sugar
        else if(Character.isAlphabetic(arg.charAt(0)) && arg.charAt(1) == arg.charAt(2)) {
            switch (arg.charAt(1)) {
                case '+':
                    Variable.changeVar(arg.charAt(0), '+'); break;
                case '-':
                    Variable.changeVar(arg.charAt(0), '-'); break;
                case '*':
                    Variable.changeVar(arg.charAt(0), '*'); break;
                case '/':
                    Variable.changeVar(arg.charAt(0), '/'); break;
            }
        }
        //Calculate sin, cos, tan, arc sin, arc cos, arc tan;
        else if(arg.charAt(0) == 's' && arg.charAt(1) == 'i' && arg.charAt(2) == 'n') {
            int firstDig = 0, digLen = 0; double value = 0;
            for(int i = 2; i < arg.length(); i++) {
                if(Character.isDigit(arg.charAt(i))) {
                    if(firstDig == 0) firstDig = i;
                    digLen++;
                }
            }
            int exp = digLen;
            for(int i = firstDig; i < firstDig + digLen; i++) {
                value += (arg.charAt(i) - '0') * Math.pow(10, --exp);
            }
            Variable.doubleValue[0] = Calc.sin(value * Math.acos(-1) / 180);
        }
        else if(arg.charAt(0) == 'c' && arg.charAt(1) == 'o' && arg.charAt(2) == 's') {
            int firstDig = 0, digLen = 0; double value = 0;
            for(int i = 2; i < arg.length(); i++) {
                if(Character.isDigit(arg.charAt(i))) {
                    if(firstDig == 0) firstDig = i;
                    digLen++;
                }
            }
            int exp = digLen;
            for(int i = firstDig; i < firstDig + digLen; i++) {
                value += (arg.charAt(i) - '0') * Math.pow(10, --exp);
            }
            Variable.doubleValue[0] = Calc.cos(value * Math.acos(-1) / 180);
        }
        else if(arg.charAt(0) == 't' && arg.charAt(1) == 'a' && arg.charAt(2) == 'n') {
            int firstDig = 0, digLen = 0; double value = 0;
            for(int i = 2; i < arg.length(); i++) {
                if(Character.isDigit(arg.charAt(i))) {
                    if(firstDig == 0) firstDig = i;
                    digLen++;
                }
            }
            int exp = digLen;
            for(int i = firstDig; i < firstDig + digLen; i++) {
                value += (arg.charAt(i) - '0') * Math.pow(10, --exp);
            }
            Variable.doubleValue[0] = Calc.tan(value * Math.acos(-1) / 180);
        }
        else if(arg.charAt(0) == 'a' && arg.charAt(1) == 's' && arg.charAt(2) == 'i' && arg.charAt(3) == 'n') {
            int firstDig = 0, digLen = 0; double value = 0;
            for(int i = 2; i < arg.length(); i++) {
                if(Character.isDigit(arg.charAt(i))) {
                    if(firstDig == 0) firstDig = i;
                    digLen++;
                }
            }
            int exp = digLen;
            for(int i = firstDig; i < firstDig + digLen; i++) {
                value += (arg.charAt(i) - '0') * Math.pow(10, --exp);
            }
            if(arg.charAt(firstDig - 1) == '-') {
                value = -value;
            }
            Variable.doubleValue[0] = Calc.asin(value);
        }
        else if(arg.charAt(0) == 'a' && arg.charAt(1) == 'c' && arg.charAt(2) == 'o' && arg.charAt(3) == 's') {
            int firstDig = 0, digLen = 0; double value = 0;
            for(int i = 2; i < arg.length(); i++) {
                if(Character.isDigit(arg.charAt(i))) {
                    if(firstDig == 0) firstDig = i;
                    digLen++;
                }
            }
            int exp = digLen;
            for(int i = firstDig; i < firstDig + digLen; i++) {
                value += (arg.charAt(i) - '0') * Math.pow(10, --exp);
            }
            if(arg.charAt(firstDig - 1) == '-') {
                value = -value;
            }
            Variable.doubleValue[0] = Calc.acos(value);
        }
        else if(arg.charAt(0) == 'a' && arg.charAt(1) == 't' && arg.charAt(2) == 'a' && arg.charAt(3) == 'n') {
            int firstDig = 0, digLen = 0; double value = 0;
            for(int i = 2; i < arg.length(); i++) {
                if(Character.isDigit(arg.charAt(i))) {
                    if(firstDig == 0) firstDig = i;
                    digLen++;
                }
            }
            int exp = digLen;
            for(int i = firstDig; i < firstDig + digLen; i++) {
                value += (arg.charAt(i) - '0') * Math.pow(10, --exp);
            }
            Variable.doubleValue[0] = Calc.atan(value);
        }

        //Syntax Error
        else {
            System.out.println("Syntax Error");
        }




    }
    public static void main(String[] args) {
	    Scanner read = new Scanner(System.in);
	    String buffer;
        Variable.varList[0] = 'A';
        while(true) {
            System.out.print(">>>");
            buffer = read.nextLine();
            buffer = buffer.replaceAll(" ", "");
            if(checkBuffer(buffer)) {
               runArg(buffer);
            }
            Display.print();
        }
    }
}
