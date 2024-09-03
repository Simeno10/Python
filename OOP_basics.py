from car import Car
from car import Electric
from car import Hybrid
from car import Ford
from car import Vehicle
from car import Motorcycle


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

def change_color(object, color):
    object.color=color
def funkcja():
    print("Elo")
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    print(func("Hello"))
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

fish=Fish(3,4)
rabbit=Rabbit(2,3,5)
print(fish.area())
print(rabbit.volume())
elo = divisor(2)(10)
print(elo)

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
car_1.go()
car_1.stop()
motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()
print(ford.color)
change_color(ford, "green")
print(ford.color)

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
x=funkcja
y=print
x()
y("Cześć")
hello(loud)
hello(quiet)

students = (("Marek","F",14),
            ("Hela","A",25),
            ("Igor", "C",19),
            ("Maria","D",44))
wiek = lambda roczniki:roczniki[2]
ocena = lambda oceny:oceny[1]
#students.sort(key=wiek, reverse=True)
sorted_students = sorted(students, key=ocena)
for i in sorted_students:
    print(i)
print("////////////////////////\n")
wiek_pelnoletni = lambda roczniki:roczniki[2] >=18
drinking_buddies = list(filter(wiek_pelnoletni, sorted_students))
for i in drinking_buddies:
    print(i)
