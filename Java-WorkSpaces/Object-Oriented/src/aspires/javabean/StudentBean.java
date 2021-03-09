package aspires.javabean;

public class StudentBean implements java.io.Serializable{
    /*
    A JavaBean is just a standard

    * All properties are private (use getters/setters)
    * A public no-argument constructor
    * Implements Serializable.

    That's it. It's just a convention. Lots of libraries depend on it though.
    JavaBean can contain Bean Variables -- (Nested)
    */
    private String firstName = null;
    private String lastName = null;
    private int age = 0;

    public StudentBean() {};

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public int getAge() {
        return age;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
