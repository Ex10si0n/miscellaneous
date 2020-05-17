package studio.aspire.ex;

public class Fish implements Pet {
    private String name;

    public Fish() {

    }

    public void walk() {
        System.out.println("鱼不能行走");
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public void play() {

    }
}
