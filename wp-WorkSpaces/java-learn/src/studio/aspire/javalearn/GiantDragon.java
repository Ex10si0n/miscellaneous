package studio.aspire.javalearn;

//饿汉式单例模式
public class GiantDragon {
    int hp;
    private GiantDragon() {
       this.hp = 2000;
    }
    private static GiantDragon instance = new GiantDragon();

    public static GiantDragon getInstance() {
        return instance;
    }
}

/*public*/ class SmallDragon {
   int hp;
   private SmallDragon() {
       this.hp = 1000;
   }
   private static SmallDragon instance;
   public static SmallDragon getInstance() {
       if (instance == null) {
           instance = new SmallDragon();
       }
       return instance;
   }
}

/*
单例模式三元素
1. 构造方法私有化
2. 静态属性指向实例
3. public static的 getInstance方法，返回第二步的静态属性
*/
