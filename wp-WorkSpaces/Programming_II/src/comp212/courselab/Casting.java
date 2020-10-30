package comp212.courselab;

public class Casting {
    public static void main(String[] args) {
        // Cannot cast a superclass to it's subclass
        Staff staff0 = new Staff();
        // Supervisor newStaff = staff0;


        // It's OK
        Supervisor staff1 = new Supervisor();
        Staff staff2 = staff1;

        System.out.println(staff0 == staff1);
        // System.out.println(staff0 == Staff);
        System.out.println(staff0 instanceof Staff);
        System.out.println(staff0 instanceof Supervisor); // super =x=> sub
        System.out.println(staff0 instanceof Object);     // sub ===> super


    }
}
