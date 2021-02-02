package aspires.relationship.aggregation;

public class YearTutor {
    private String schoolName = "ESCA";
    private String tutorList[] = {"Calana", "Edmund"};
    private String tutorName;

    public YearTutor(int studentID) {
        tutorName = (studentID > 201500000) ? tutorList[0] : tutorList[1];
    }

    public String getSchoolName() {
        return this.schoolName;
    }

    public String getTutorName() {
        return tutorName;
    }
}
