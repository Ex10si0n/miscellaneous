package BuilderPattern_II;

public class Main {
    public static void main(String[] args) {
        PersonBean steve = new PersonBean.Builder("Steve", "Yan").setAge(20).setHeight(182).setGender("Male").build();
        PersonBean alston = new PersonBean.Builder("Alston", "Yu").setGender("Male").build();
    }
}
