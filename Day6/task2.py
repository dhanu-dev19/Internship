from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


# Child Class 1
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key")


# Child Class 2
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with self start")


# Child Class 3
class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started using air pressure system")


car = Car()
bike = Bike()
bus = Bus()

car.start_engine()
bike.start_engine()
bus.start_engine()
