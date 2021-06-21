package Miscellaneous.SubtypePolymorphism;
import java.util.ArrayList;
import java.util.List;

// Not adpoting subtype polymorphism
public class AutoMobile {
    public static List < Object > carList = new ArrayList < Object > ();
    public static int getTotalSeats() {
        int totalSeat = 0;
        for (int i = 0; i < carList.size(); i++) {
            if (carList.get(i) instanceof Convertible) {
                totalSeat += 2;
            } else if (carList.get(i) instanceof Minivan) {
                totalSeat += 6;
            } else if (carList.get(i) instanceof SUV) {
                totalSeat += 4;
            } else {
                totalSeat += 0;
            }
        }
        return totalSeat;
    }

    public static void main(String[] args) {
        AutoMobile.carList.add(new Convertible());
        AutoMobile.carList.add(new Minivan());
        AutoMobile.carList.add(new SUV());
        System.out.println(AutoMobile.getTotalSeats());
    }
}
class Convertible {
    public String getName() {
        return "Convertible";
    }
}
class Minivan {
    public String getName() {
        return "Minivan";
    }
}
class SUV {
    public String getName() {
        return "SUV";
    }
}