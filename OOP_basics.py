from car import Car
from car import Electric
from car import Hybrid
from car import Ford


class Prey:

    def flee(self):
        print("This animal flees")
class Predator:

    def hunt(self):
        print("This animal is hunting")

class Fish(Prey, Predator):
    def hunt(self):
        print("This fish is junting")

fish=Fish()

fish.hunt()
fish.flee()


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

ford = Ford("Ford","Focus", 2024, "yellow")
print(ford.wheels)
ford.hybrid()
ford.ford()
