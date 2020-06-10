package studio.aspire.ex;

public abstract class Animal {
    protected int legs;
    protected Animal(int legs) {
        this.legs = legs;
    }
    public abstract void eat();
    public void walk() {
        System.out.println("用 " + this.legs + " 只脚行走");
    }
}
