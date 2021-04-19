package BuilderPattern_I;

public class Coke extends Drink {
    @Override
    public String name() {
        return "Coke";
    }

    @Override
    public float price() {
        return 15.0f;
    }
}
