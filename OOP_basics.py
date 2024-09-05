import time

import car
import threading
from car import Car
from car import Electric
from car import Hybrid
from car import Ford
from car import Vehicle
from car import Motorcycle
from multiprocessing import Process, cpu_count


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
def sleep():
    time.sleep(2)
    print("sleep")
def coffe():
    time.sleep(3)
    print("drink cawfee")
def eat():
    time.sleep(4)
    print("yummy")
def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ",count," seconds")


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
#while food := input("What food do you like?: ") != "quit":
#    foods.append(food)
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
people_age = {'Marek':32, 'Jadzia':18, 'Erenest':90, 'Kilian':45}
people_months = {key: value*12 for (key, value) in people_age.items()}
people_older = {key: value for (key, value) in people_age.items() if value>40}
people_good = {key: ("YOUNG" if value<40 else "OLD") for (key, value) in people_age.items()}
print(people_months)
print(people_older)
print(people_good)
def func(value):
    if value==45:
        return "45 lat minęło!"
    elif value>45:
        return "STARY!"
    else:
        return "YOUNGBOY!"

people_func = {key: func(value) for (key, value) in people_age.items()}
print(people_func)
xxx = threading.Thread(target=eat, args=())
xxx.start()
yyy = threading.Thread(target=coffe, args=())
yyy.start()
zzz = threading.Thread(target=sleep, args=())
zzz.start()
xxx.join()
yyy.join()
zzz.join()
hhh = threading.Thread(target=timer, daemon=True)
hhh.start()

#hhh.setDaemon(True)
#print(hhh.isDaemon())

answer = input("Do you wish toe exit?\n")
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
