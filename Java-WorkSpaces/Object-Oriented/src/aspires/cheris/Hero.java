package aspires.cheris;

public class Hero {
    public String name;
    public int hp;
    public static int hCount = 0;

    public Hero(String name, int hp) {
        this.name = name;
        this.hp = hp;
        this.hCount += 1;
    }

    @Override
    public String toString() {
        return "Hero{" +
                "name='" + name + '\'' +
                ", hp=" + hp +
                '}';
    }

    public static void printHeroCount() {
        System.out.println(Hero.hCount + " hero(s) created.");
    }
    public static void main(String[] args) {
        Hero h1 = new Hero("Hanzo", 200);
        Hero h2 = new Hero("Hanzo", 200);
        Hero h3 = new Hero("Hanzo", 200);
        Hero h4 = new Hero("Hanzo", 200);
        Hero h5 = new Hero("Hanzo", 200);
        Hero h6 = new Hero("Hanzo", 200);
        Hero.printHeroCount();
    }
}
