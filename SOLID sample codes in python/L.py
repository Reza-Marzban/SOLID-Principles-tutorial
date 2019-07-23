"""
Liskov Substitution Principle



bad
"""


def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))


animal_leg_count(animals)

"""
better
if we follow LSP, there is no need for above if and else statement. As a sub-class must be substitutable for its super-class
"""


def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())


animal_leg_count(animals)



class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):


