class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year

    def display_car(self):
        print(self.brand, self.model, self.year)

car1_shnn = Car("Toyota", "Corolla", 2022)
car1_shnn.display_car()