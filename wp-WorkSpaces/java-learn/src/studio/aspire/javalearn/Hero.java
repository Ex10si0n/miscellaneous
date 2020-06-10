package studio.aspire.javalearn;

public class Hero {
    public static int heroNums = 0;
    String name;
    float hp;
    float armor;
    int moveSpeed;

    public static void battleWin() {
        System.out.println("Hero Win");
    }

    public enum HeroType {
       TANK, WIZARD, ASSASSIN, ASSIST, WARRIOR, RANGED, PUSH, FARMING;
    }

    public boolean equals(Object o) {
        if (o instanceof Hero) {
            Hero h = (Hero) o;
            return this.hp == h.hp;
        }
        return false;
    }

    public Hero() {

    }

    public Hero(String name) {
        this.heroNums ++;
        this.name = name;
    }

    public Hero(String name, float hp, float armor, int moveSpeed) {
        this.heroNums ++;
        this.name = name;
        this.hp = hp;
        this.armor = armor;
        this.moveSpeed = moveSpeed;
        System.out.println("你使用了重载过的构造方法");
    }

    //类方法
    public static void displayHeroNums() {
        System.out.println("目前已创建的英雄数: " + heroNums);
    }

    float getArmor() {
        return armor;
    }

    void addSpeed(int speed) {
        moveSpeed += speed;
    }

    void keng() {
        System.out.println("正在坑队友！");
    }

    float getHp() {
        return hp;
    }

    void useItem(Item item) {
        item.effect();
    }

    void restoreHp(int h) {
        this.hp += h;
        h = 0;
    }

    void attack(Hero ... heros) {
       for (Hero hero: heros) {
           System.out.println(this.name + "攻击了" + hero.name);
       }
    }

    public static void main(String[] args) {
        Hero garen = new Hero("Garen");
        garen.hp = 616.28f;
        garen.armor = 27.53f;
        garen.moveSpeed = 350;

        Hero teemo = new Hero("Teemo");
        teemo.hp = 383f;
        teemo.armor = 14f;
        teemo.moveSpeed = 330;

        Hero annie = new Hero("Annie");
        Hero doomfist = new Hero("Doomfist", 250, 50, 10);


        teemo.keng();
        System.out.println(teemo.moveSpeed);
        teemo.addSpeed(100);
        System.out.println(teemo.moveSpeed);

        System.out.println(garen.getHp());
        garen.attack(teemo, annie);

        doomfist.attack(teemo);
        System.out.println(doomfist.hp);
        doomfist.restoreHp(50);
        System.out.println(doomfist.hp);

        System.out.println(doomfist.heroNums);
        System.out.println(teemo.heroNums);
        System.out.println(Hero.heroNums);

        garen.heroNums -= 1;
        System.out.println(garen.heroNums);
        System.out.println(Hero.heroNums);

        displayHeroNums();

        MagicPortion mp = new MagicPortion();
        LifePortion lp = new LifePortion();

        //枚举类型
        for (HeroType type: HeroType.values()) {
            System.out.println(type);
        }

        //多态
        garen.useItem(lp);
        garen.useItem(mp);

        //超类
        Hero h1 = new Hero();
        h1.hp = 100;
        Hero h2 = new Hero();
        h2.hp = 150;
        Hero h3 = new Hero();
        h3.hp = 100;
        Hero h4 = h3;

        System.out.println(h1.equals(h2));
        System.out.println(h1.equals(h3));

        //同样的哈希值
        System.out.println(h4.hashCode());
        System.out.println(h3.hashCode());
    }
}

//Final 修饰符
final class Assist extends Object{
    String type = "Assist";
    float hp;

    public static void main(String[] args) {
        final int hp;
        hp = 5;
        // hp = 6;

    }
}
