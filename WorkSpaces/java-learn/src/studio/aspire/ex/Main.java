package studio.aspire.ex;

public class Main {
    public static void main(String[] args) {
        Fish fish = new Fish();
        Cat cat = new Cat("Pu'er");
        Spider spider = new Spider();
        System.out.println(cat.getName());
        cat.walk();
        fish.walk();
        System.out.println(spider.legs);
    }
}
