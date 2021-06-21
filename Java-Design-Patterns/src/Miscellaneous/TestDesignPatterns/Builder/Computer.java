package Miscellaneous.TestDesignPatterns.Builder;

public class Computer {
    private String CPU;
    private int RAM;
    private String GPU;
    private int USB;

    private Computer(Builder builder) {
        this.CPU = builder.CPU;
        this.RAM = builder.RAM;
        this.USB = builder.USB;
        this.GPU = builder.GPU;
    }

    @Override
    public String toString() {
        return "Computer{" +
                "CPU='" + CPU + '\'' +
                ", RAM=" + RAM +
                ", GPU='" + GPU + '\'' +
                ", USB=" + USB +
                '}';
    }

    private static class Builder {
        private String CPU;
        private int RAM;
        private String GPU;
        private int USB;

        public Builder(String CPU, int RAMSize) {
            this.CPU = CPU;
            this.RAM = RAMSize;
        }

        public Builder installGPU(String GPU) {
            this.GPU = GPU;
            return this;
        }

        public Builder installUSB(int USBSlots) {
            this.USB = USBSlots;
            return this;
        }

        public Computer build() {
            return new Computer(this);
        }
    }

    public static void main(String[] args) {
        Computer computer1 = new Computer.Builder("Intel Core i7", 32).installGPU("RTX 3090").installUSB(4).build();
        Computer computer2 = new Computer.Builder("Intel Core i7", 32).build();

        System.out.println(computer1);
        System.out.println(computer2);
    }
}
