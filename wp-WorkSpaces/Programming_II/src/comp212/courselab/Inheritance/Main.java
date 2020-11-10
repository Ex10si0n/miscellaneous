package comp212.courselab.Inheritance;

import javax.swing.plaf.synth.SynthTabbedPaneUI;

public class Main {

    public static void main(String[] args) {

        // Creation of Instances
        Staff steve = new Staff("ST101", "Steve", 10000);
        Staff cheris = new Staff("ST102", "Cheris", 12000);
        Supervisor stephen = new Supervisor("SU801", "Jack", 20000);
        Staff king = new Staff("ST103", "King", 10000);
        Staff alston = new Staff("ST104", "Alston", 15000);
        Supervisor jane = new Supervisor("SU802", "Jane", 25000);
        Staff Kevin = new Staff("ST105", "Kevin", 10000);
        Staff allen = new Staff("ST106", "Allen", 10000);
        Staff jason = new Staff("ST107", "Jason", 10000);
        Staff admin = new Staff();


        // Supervisor Add Staff
        stephen.addStaff("ST101");
        stephen.addStaff("ST102");
        jane.addStaff("ST103");
        jane.addStaff("ST104");
        jane.addStaff("ST105");


        // Select All Staffs
        Staff.allInfo();
        System.out.println("\nNumber of Staff: " + Staff.getStaffNumber());
        if (Staff.getStaffNumber() >= 10) {
            System.out.println("[Warning] Staff Number Too High!");
        }
    }
}