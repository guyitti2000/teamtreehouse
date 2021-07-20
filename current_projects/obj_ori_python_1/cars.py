class Car:

    wheels = 4
    doors = 2
    engine = True

    def __init__(self, make, model, year, gas=100):
        self.make = make
        self.model = model
        self.year = year
        self.is_moving = False
        self.gas = gas

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model

    def stop(self):
        if self.is_moving:
            print('The car has stopped.')
            self.is_moving = False
        else:
            print('The car has already stopped.')

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print('The car starts moving.')
                self.is_moving = True
            print(f'The car is going {speed}.')
        else:
            print("You've run out of gas!")
            self.stop()

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True


class Dealership:
    def __init__(self):
        self.cars = []

    def __iter__(self):
        yield from self.cars
        # yield from is a KEYWORD that tells python to grab each item from the iterable(list) that we are giving it

    def add_car(self, car):
        self.cars.append(car)


my_dealership = Dealership()
car_one = Car("Mustang", "Model T", 1908)
car_two = Car("Ford", "Focus", 2014)
car_three = Car("Mazda", "MPV ", 2006)

if car_one == car_two:
    print('equal')
else:
    print('not equal')

my_dealership.add_car(car_one)
my_dealership.add_car(car_two)
my_dealership.add_car(car_three)
for car in my_dealership:
    print(car)


print("\n\n\n\n")
print(car_one)
print(str(car_one))
car_one.use_gas()
car_one.stop()
car_one.go("slow")
car_one.go("fast")
car_one.stop()
car_one.stop()

'''
my_car = Car()
print(my_car)
print(type(my_car))
print(isinstance(my_car, Car))
#these are used to check
'''
