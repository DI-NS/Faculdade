class Car {
    private String carName;
    private String carModel;
    private String carCapacity;

    public Car() {
        this.carName = "";
        this.carModel = "";
        this.carCapacity = "";
    }

    
    public Car(String name, String model) {
        this.carName = name;
        this.carModel = model;
        this.carCapacity = ""; // Inicializa carCapacity como uma string vazia
    }

  
    public Car(String name, String model, String capacity) {
        this.carName = name;
        this.carModel = model;
        this.carCapacity = capacity;
    }

    // Método para retornar os detalhes do carro
    public String getDetails() {
        return "Name: " + this.carName + ", Model: " + this.carModel + ", Capacity: " + this.carCapacity;
    }
}

// Main.java
public class Main {
    public static void main(String[] args) {
        // Criar instâncias da classe Car
        Car car1 = new Car(); // Usando o construtor padrão
        Car car2 = new Car("Toyota", "Corolla"); // Usando o construtor parametrizado 1
        Car car3 = new Car("Ford", "Mustang", "100"); // Usando o construtor parametrizado 2

        // Imprimir detalhes dos carros
        System.out.println("Car 1 details: " + car1.getDetails());
        System.out.println("Car 2 details: " + car2.getDetails());
        System.out.println("Car 3 details: " + car3.getDetails());
    }
}
