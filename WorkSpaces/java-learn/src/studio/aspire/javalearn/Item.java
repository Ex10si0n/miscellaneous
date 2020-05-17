package studio.aspire.javalearn;

public class Item {
    String name;
    int price;

    void sold() {
        System.out.println(name + " 已卖出");
    }

    void effect() {
        System.out.println("物品产生效果");
    }

    public static void main(String[] args) {
        Item bottle = new Item();
        bottle.name = "Bottle";
        bottle.price = 50;

        Item shoes = new Item();
        shoes.name = "Shoes";
        shoes.price = 300;

        Item sword = new Item();
        sword.name = "Sword";
        sword.price = 350;

        Portion portion = new Portion();
        LifePortion lifeportion = new LifePortion();
        portion.effect();
        lifeportion.effect();
        // 方法得到重载


    }

}

class Portion extends Item {
    String name;
    int price;

    public void buy() {
        System.out.println("买入");
    }

    public void effect() {
        System.out.println("效果产生");
    }
}

class LifePortion extends Portion {
    public void effect() {
        System.out.println("恢复生命");
    }
}

class MagicPortion extends Portion {
    public void effect() {
        System.out.println("恢复法力");
    }
}

