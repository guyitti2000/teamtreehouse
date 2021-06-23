class Car:
    #class attributes
    wheels = 4
    doors = 2
    engine = True
#objects created in the class (instantiation) are called instances


car_one = Car()
car_two = Car()
print(f'car_one {car_one.doors}')
print(id(car_one.doors))
print(f'car_two {car_two.doors}')
print(id(car_two.doors))
print(f'Car {Car.doors}')
print(id(Car.doors))

Car.doors = 5
car_one.doors = 6
print(f'car_one {car_one.doors}')
print(id(car_one.doors))
print(f'car_two {car_two.doors}')
print(id(car_two.doors))
print(f'Car {Car.doors}')
print(id(Car.doors))







'''
my_car = Car()
print(my_car)
print(type(my_car))
print(isinstance(my_car, Car))
#these are used to check
'''
