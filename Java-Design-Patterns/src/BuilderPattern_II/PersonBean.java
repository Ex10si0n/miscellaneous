package BuilderPattern_II;

public class PersonBean {
    private final String firstName, lastName, gender;
    private final double height;
    private final int age;

    private PersonBean(Builder builder) {
        this.firstName = builder.firstName;
        this.lastName = builder.lastName;
        this.gender = builder.gender;
        this.height = builder.height;
        this.age = builder.age;
    }

    public String getGender() { return gender; }
    public double getHeight() { return height; }
    public int getAge() { return age; }
    public String getFirstName() { return firstName; }
    public String getLastName() { return lastName; }

    public static class Builder {
        private final String firstName, lastName;
        private String gender;
        private double height;
        private int age;

        public Builder(String firstName, String lastName) {
            this.firstName = firstName;
            this.lastName = lastName;
        }

        public Builder setGender(String gender) { this.gender = gender; return this; }
        public Builder setHeight(double height) { this.height = height; return this; }
        public Builder setAge(int age) { this.age = age; return this; }

        public PersonBean build() {
            return new PersonBean(this);
        }
    }
}
