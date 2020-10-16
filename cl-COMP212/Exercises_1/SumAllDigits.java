/* sid = p1908326
 * sname = 'Steve'
 * Code by Ex10si0n
 * */
import java.util.Scanner;
public class SumAllDigits{
    public static int sumDigits(int n) {
        int ans = 0;
        while(n != 0) {
            ans += n % 10;
            n /= 10;
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int number = scan.nextInt();
        System.out.println("Sum of All Digits: " + sumDigits(number));
        scan.close();
    }
}
