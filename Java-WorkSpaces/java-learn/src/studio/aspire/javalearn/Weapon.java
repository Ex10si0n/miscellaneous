package studio.aspire.javalearn;

public class Weapon extends Item {
    int damage;
    public Weapon(String name, int price, int damage) {
        this.name = name;
        this.price = price;
        this.damage = damage;
    }
    public static void main(String[] args) {
        Weapon w = new Weapon("一把刀", 10, 100);

        w.sold();
    }
}
