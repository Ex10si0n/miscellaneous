package comp212.oop;

public class Main {

    public static void main(String[] args) {

        // Creation of Instances
        Staff steve = new Staff("ST101", "Steve", 10000);
        Staff cheris = new Staff("ST102", "Cheris", 12000);
        Supervisor stephen = new Supervisor("SU801", "Jack", 20000);
        Staff king = new Staff("ST103", "King", 10000);
        Staff alston = new Staff("ST104", "Alston", 15000);
        Supervisor jane = new Supervisor("SU802", "Jane", 25000);


        // Supervisor Add Staff
        stephen.addStaff("ST101");
        stephen.addStaff("ST102");
        jane.addStaff("ST103");
        jane.addStaff("ST104");


        // Select All Staffs
        Staff.allInfo();
    }
}