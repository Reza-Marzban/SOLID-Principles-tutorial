
"""
Single-responsibility Principle



bad -  problem : have two jobs    -    easy to use
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass




"""
better  - two class, each have one job   - a little messy to use
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass




"""
Best   -   using facade   -   each class have one job - easier to use
"""


class Animal:
    def __init__(self, name: str):
        self.name = name
        self.db = AnimalDB()

    def get_name(self):
        return self.name

    def get(self, id):
        return self.db.get_animal(id)

    def save(self):
        self.db.save(animal=self)


