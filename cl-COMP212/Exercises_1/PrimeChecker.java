/* sid = p1908326
 * sname = 'Steve'
 * Code by Ex10si0n
 * */
import java.util.Scanner;
public class PrimeChecker{
    public static boolean isPrime(int n) {
        if(n == 1) return false;
        if(n == 2) return true;
        int i;
        for(i = 2; i <= Math.sqrt(n)+1; ++i) {
            if(n % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int number = scan.nextInt();
        System.out.println("Is Prime: " + isPrime(number));
        scan.close();
    }
}
