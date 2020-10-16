/* sid = p1908326
 * sname = 'Steve'
 * Code by Ex10si0n
 * */
public class AverageSpeedInKm{
    public static void main(String[] args) {
        String ans = "Average Speed: ";
        ans += (24.0 * 1.6) / (1 + 40.0 / 60.0 + 35.0 / 3600.0);
        ans += " km/h";
        System.out.println(ans);
    }
}
