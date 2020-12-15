package comp212.courselab.Lambda;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Hero {
    public int hp;
    public int damage;
    public String name;

    public Hero(String name, int hp, int damage) {
        this.name = name;
        this.hp = hp;
        this.damage = damage;
    }

    @Override
    public String toString() {
        return "Hero{" +
                "hp=" + hp +
                ", damage=" + damage +
                ", name='" + name + '\'' +
                '}';
    }

    public static void main(String[] args) {
        Hero hanzo = new Hero("Hanzo", 200, 100);
        Hero tracer = new Hero("Tracer", 150, 120);
        Hero winston = new Hero("Winston", 400, 40);
    }
}
