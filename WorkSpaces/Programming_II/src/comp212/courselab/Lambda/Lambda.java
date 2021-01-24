package comp212.courselab.Lambda;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Lambda {
    private static void filter(List<Hero> heros, HeroChecker checker) {
        for (Hero hero: heros) {
            if (checker.test(hero))
                System.out.println(hero);
        }
    }

    public static boolean testHero(Hero h) {
        return h.hp > 100 && h.damage < 50;
    }

    public static void main(String[] args) {
        Random r = new Random();
        List<Hero> heros = new ArrayList<Hero>();
        for (int i = 0; i < 10; i++) {
            heros.add(new Hero("hero" + i, r.nextInt(1000), r.nextInt(100)));
        }
        System.out.println("Sets after init:");
        System.out.println(heros);
        System.out.println("[Anonymous Class] Applying filter:");
        HeroChecker checker = new HeroChecker() {
            @Override
            public boolean test(Hero h) {
                return (h.hp > 100 && h.damage < 50);
            }
        };
        HeroChecker checker2 = (h) -> h.hp > 100 && h.damage < 50;
        filter(heros, checker);
        filter(heros, checker2);
        System.out.println("[Lambda] Applying filter:");
        filter(heros, (h) -> h.hp > 100 && h.damage < 50);
        System.out.println("[Static Method in Lambda] Applying filter:");
        filter(heros, h -> testHero(h));
        System.out.println("[Static Method] Applying filter:");
        filter(heros, Lambda::testHero);
    }
}
