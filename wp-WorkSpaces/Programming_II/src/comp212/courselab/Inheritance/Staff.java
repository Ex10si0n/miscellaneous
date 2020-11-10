package comp212.courselab.Inheritance;

import java.util.ArrayList;
import java.util.List;

public class Staff {
    public static List<Staff> allStaff = new ArrayList<>();
    public static int staffNumber;
    private String sid;
    private String name;
    private int salary;
    public String suid;
    public Staff() {
        this.sid = "test-id";
        this.name = "John Doe";
        this.salary = 10000;
        staffNumber ++;
        allStaff.add(this);
    }
    public Staff(String sid, String name, int salary) {
        this.sid = sid;
        this.name = name;
        this.salary = salary;
        this.suid = "NULL";
        staffNumber ++;
        allStaff.add(this);
    }
    public String getSid() {
        return this.sid;
    }
    public static int getStaffNumber() {return staffNumber;}
    public void setSupervisor(String suid) {
        this.suid = suid;
    }
    public void info() {
        System.out.printf("|%7s |%10s |%8d |%7s |\n", this.sid, this.name, this.salary, this.suid);
    }
    public static void allInfo() {
        System.out.printf("+--------+-----------+---------+--------+\n");
        System.out.printf("|    sid |      name |  salary |   suid |\n");
        System.out.printf("+--------+-----------+---------+--------+\n");
        for (int i = 0; i < Staff.allStaff.size(); i++)
            Staff.allStaff.get(i).info();
        System.out.printf("+--------+-----------+---------+--------+");
    }
}
