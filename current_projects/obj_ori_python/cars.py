class Car:

    wheels = 4
    doors = 2
    engine = True

    def __init__(self, make, model, year=2020, gas=100):
        self.make = make
        self.model = model
        self.year = year
        self.is_moving = False
        self.gas = gas

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    def use_gas(self):
        self.gas -= 50
        print(self.gas)

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

car_one = Car("Mustang", "Model T", 1908)
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
