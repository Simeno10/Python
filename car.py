from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    wheels = 4  #class variable

    def go(self):
        print("You drive the car.")
    def stop(self):
        print("This car is stopped.")

    def __init__(self,make,model,year,color):
        self.make = make    #instance variable
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.make+" "+self.model+" is driving")
    def stop(self):
        print("This car is stopped")

class Electric(Car):
    def battery(self):
        print("Battery 100%")
class Hybrid(Car):
    def hybrid(self):
        print("This is hybrid car")

class Ford(Hybrid):
    def ford(self):
        print("This Ford is hybrid car")

class Motorcycle(Vehicle):
    def go(self):
        print("You drive the motorcycle.")

    def stop(self):
        print("This motorcycle is stopped.")
