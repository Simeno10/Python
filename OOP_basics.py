from car import Car

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
