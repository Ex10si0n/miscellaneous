package Miscellaneous.SubtypePolymorphism;

import java.util.ArrayList;
import java.util.List;

public class AutoTrader {

    public static List<SportCar> carList = new ArrayList<>();

    public static int getTotalSeats() {
        int totalSeat = 0;
        for (int i = 0; i < carList.size(); i++) totalSeat += carList.get(i).getCapacity();
        return totalSeat;
    }

    public static void main(String[] args) {
        AutoTrader.carList.add(new CovertibleSportCar());
        AutoTrader.carList.add(new MinivanSportCar());
        AutoTrader.carList.add(new SUVSportCar());
        System.out.println(AutoTrader.getTotalSeats());
    }

}
