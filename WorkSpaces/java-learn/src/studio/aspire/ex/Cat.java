package studio.aspire.ex;

public class Cat extends Animal implements Pet{
    String name;
    public Cat(String name) {
        super(4);
        this.name = name;
    }

    public Cat() {
        this(null);
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
        System.out.println("正在玩");
    }

    public void eat() {
        System.out.println("正在吃");
    }



}
