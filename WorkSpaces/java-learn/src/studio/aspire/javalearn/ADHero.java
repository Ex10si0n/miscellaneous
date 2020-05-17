package studio.aspire.javalearn;

public class ADHero extends Hero implements AD {
    public ADHero(String name, int hp, int armor, int moveSpeed) {
        super(name, hp=0, armor=0, moveSpeed=0);
        System.out.println("使用子类super方法作为构造函数");
    }

    public static void battleWin() {
        System.out.println("ADHero Win");
    }

    @Override
    public void phyAttack() {
        System.out.println(name + "发起了一次物理攻击");
    }

    public static void main(String[] args) {
        ADHero tracer = new ADHero("Tracer", 150, 0, 100);
        tracer.phyAttack();
        tracer.addSpeed(100);
        System.out.println(tracer.moveSpeed);
        ADHero hanzo = new ADHero("Hanzo", 200, 0, 100);
        hanzo.battleWin();
        // Object 类默认的对象方法
        System.out.println(hanzo.toString());

    }
}
