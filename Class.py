class House:
    build_method = 'concrete'
    
    def __init__(self, rooms, stories):
        self.rooms = rooms
        self.stories = stories
my_house = House(5,3)
print(my_house.rooms)

print(House.build_method)

my_house.build_method = 'wooden'
print(my_house.build_method)

House.build_method = 'unspecified'

print(House.build_method)

from tarfile import PAX_NAME_FIELDS
import time
print(time.__doc__)    # use .__doc__ to see the documentation after you import need



