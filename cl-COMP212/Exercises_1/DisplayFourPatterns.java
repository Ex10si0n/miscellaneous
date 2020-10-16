/* sid = p1908326
 * sname = 'Steve'
 * Code by Ex10si0n
 * */
public class DisplayFourPatterns {
    public static void printN(String s, int times) {
        while(times-- > 0) {
            System.out.print(s);
        }
    }

    public static void main(String[] args) {
        int i;
        System.out.println("Pattern A");
        for(i = 1; i <= 6; ++i) {
            printN("* ", i);
            System.out.print('\n');
        }

        System.out.println("\nPattern B");
        for(i = 6; i >= 1; --i) {
            printN("* ", i);
            System.out.print('\n');
        }

        System.out.println("\nPattern C");
        for(i = 5; i >= 0; --i) {
            printN("  ", i);
            printN("* ", 6-i);
            System.out.print('\n');
        }

        System.out.println("\nPattern D");
        for(i = 0; i <= 5; ++i) {
            printN("  ", i);
            printN("* ", 6-i);
            System.out.print('\n');
        }
    }
}
