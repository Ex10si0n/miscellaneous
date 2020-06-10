package studio.aspire;

public class Variable {
    public static int var = 1;
    public static boolean newVarName = true;
    public static char[] varList = new char[30];
    public static double doubleValue[] = new double[30];
    public static void clear() {
        var = 1;
        doubleValue[0] = 0;
        for(int i = 1; i < var; i++) {
            doubleValue[i] = 0;
            varList[i] = ' ';
        }
    }
    public static void undo(char s) {
        boolean have = false;
        for(int i = 1; i < 30; i++) {
            if(varList[i] == s) {
                newVar(varList[i], doubleValue[i]);
                have = true;
                break;
            }
        }
        if(!have) {
            newVar(s, 0);
        }
    }
    public static void newVar(char varName, double value) {
        newVarName = true;
        for(int i = 1; i < var; i++) {
            if(varName == varList[i]) {
                doubleValue[i] = value;
                newVarName = false;
                break;
            }
        }
        if(newVarName == true) {
            varList[var] = varName;
            doubleValue[var] = value;
            var ++;
        }
    }

    public static void changeVar(char varName, char symbol) {
        for(int i = 0; i < 30; i++) {
            if(varName == varList[i]) {
                switch (symbol) {
                    case '+': doubleValue[i] = doubleValue[i] + 1.0; break;
                    case '-': doubleValue[i] = doubleValue[i] - 1.0; break;
                    case '*': doubleValue[i] = doubleValue[i] * doubleValue[i]; break;
                    case '/': doubleValue[i] = Math.sqrt(doubleValue[i]); break;
                }
            }
        }
    }
}
