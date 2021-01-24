package comp212.courselab.Inheritance;

import java.util.ArrayList;
import java.util.List;

public class Supervisor extends Staff{
    private List<String> staffList = new ArrayList<>();

    public Supervisor(String sid, String name, int salary) {
        super(sid, name, salary);
        this.suid = sid;
    }
    public Supervisor() {
        super();
        this.suid = "test-id";
    }
    public boolean addStaff(String sid){
        boolean staffFound = false;
        for (int i = 0; i < Staff.allStaff.size(); i++) {
            if (Staff.allStaff.get(i).getSid() == sid) {
                staffFound = true;
                Staff.allStaff.get(i).setSupervisor(this.suid);
            }
        }
        if (!staffFound) return false;
        this.staffList.add(sid);
        return true;
    }
}
