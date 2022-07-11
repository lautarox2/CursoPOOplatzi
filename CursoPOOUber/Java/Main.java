package java;

class Main {
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        Car car = new Car();
        car.license = "AMQ123";
        car.driver = "Lauti Fleitas";
        car.passenger = 4;
        car.printDataCar();

        Car car2 = new Car();
        car2.license = "QWE546";
        car2.driver = "Emi Lerin";
        car2.passenger = 3;
        car2.printDataCar();

}