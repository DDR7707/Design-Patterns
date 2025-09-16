'''
Simple Factory Pattern Example
This code demonstrates a simple factory pattern where a factory class is used to create different types of vehicles (Car, Bike, Truck).
But this still violates the Open/Closed Principle as adding a new vehicle type requires modifying the factory method.
'''

from abc import ABC, abstractmethod

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'bike':
            return Bike()
        elif vehicle_type == 'truck':
            return Truck()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike"

class Truck(Vehicle):
    def drive(self):
        return "Driving a truck"


if __name__ == "__main__":
    # Example usage
    vehicle1 = VehicleFactory.create_vehicle('car')
    print(vehicle1.drive())  # Output: Driving a car

    vehicle2 = VehicleFactory.create_vehicle('bike')
    print(vehicle2.drive())  # Output: Riding a bike

    vehicle3 = VehicleFactory.create_vehicle('truck')
    print(vehicle3.drive())  # Output: Driving a truck

    try:
        vehicle4 = VehicleFactory.create_vehicle('bus')  # This will raise an error
    except ValueError as e:
        print(e)  # Output: Unknown vehicle type: bus
