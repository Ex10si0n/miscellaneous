package comp212.courselab;

public class Student {
    String name;
    String sid;
    String gender;
    String phone;
    int score;
    public Student(String name, String sid, String gender, String phone, int score) {
        this.name = name;
        this.sid = sid;
        this.gender = gender;
        this.phone = phone;
        this.score = score;
    }
    public void info(String para) {
        if (para == "all")
            System.out.printf("Student Name: %s, Student ID: %s, Gender: %s, Phone: %s, Score: %d\n", this.name, this.sid, this.gender, this.phone, this.score);
        else if (para == "name")
            System.out.printf("Student Name: %s\n", this.name, this.sid, this.gender, this.phone, this.score);
        else
            System.out.printf("Restrictions Error\n");
    }

    public static void main(String[] args) {
        Student steve = new Student("Steve", "p1908326", "male", "68860187", 100);
        Student cheris = new Student("Cheris", "p1902374", "female", "68560127", 100);
        steve.info("all");
        cheris.info("all");
    }
}
