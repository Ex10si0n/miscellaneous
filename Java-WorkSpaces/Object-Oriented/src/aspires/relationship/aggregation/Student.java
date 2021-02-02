package aspires.relationship.aggregation;

public class Student {
    /*
    * Aggregation: a class has an entity reference
    * Allowed us to reuse codes that we are not need to
    * program YearTutor many times.
    *
    * Code reuse is also best achieved by aggregation
    * when there is no “is a” relationship
    *
    * Information hiding: we can leave the YearTutor class
    * logic alone and Student will never know.
    */

    private int studentID;
    private String name;
    private YearTutor yearTutor;

    public Student(int id, String name) {
        this.yearTutor = new YearTutor(id);
        this.studentID = id;
        this.name = name;
    }
}
