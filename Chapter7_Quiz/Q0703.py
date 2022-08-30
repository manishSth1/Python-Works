class Vehicle:
    wheels_count = 4
    engine = 'Diesel'
    braking_system = 'Drum Brakes'

    def __init__(self, name, brand) -> None:
        self.name = name
        self.brand = brand


class HeavyVehicle(Vehicle):
    def __init__(self, name, brand, max_load, mileage):
        super().__init__(name, brand)
        self.max_load = max_load
        self.mileage = mileage
        self.wheels_count = 6


class Bike(Vehicle):
    def __init__(self, name, brand) -> None:
        super().__init__(name, brand)
        self.wheels_count = 2
        self.__number = 0

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

vehicle1 = Vehicle('SUV', 'Mercedes')

heavyvehicle1 = HeavyVehicle('Truck', 'Volvo', 15000, 12)

print(heavyvehicle1.name)
print(heavyvehicle1.mileage)

bike1 = Bike('Enfield', 'Royal Enfield')

print(isinstance(vehicle1, Vehicle))

print(isinstance(vehicle1, HeavyVehicle))
