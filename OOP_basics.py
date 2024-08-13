from car import Car
from car import Electric
from car import Hybrid
from car import Ford


class Prey:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def flee(self):
        print("This animal flees")
        return self
class Predator:

    def hunt(self):
        print("This animal is hunting")
        return self

class Fish(Prey, Predator):
    def __init__(self, length, width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width

    def hunt(self):
        print("This fish is hunting")
        return self
class Rabbit(Prey):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.length*self.width*self.height

fish=Fish(3,4)
rabbit=Rabbit(2,3,5)
print(fish.area())
print(rabbit.volume())

fish.hunt()\
    .flee()


car_1 = Car("Porsche","911", 2021, "blue")
car_2 = Car("Ferrari","F355", 1998, "red")

print(car_1.color)
print(car_2.year)
car_1.drive()
car_2.stop()
car_2.wheels = 2
print(car_1.wheels)
print(car_2.wheels)
print(Car.wheels)
Car.wheels = 5
print(car_1.wheels)

car2 = Electric("Nissan","Qashqai", 2012, "orange")
print(car2.wheels)
car2.battery()

ford = Ford("Ford","Focus", 2024, "yellow")
print(ford.wheels)
ford.hybrid()
ford.ford()
