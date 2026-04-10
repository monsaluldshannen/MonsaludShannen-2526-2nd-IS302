class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_car(self):
        print(self.brand, self.model, self.year)

car1_shnn = Car("Toyota", "Corolla", 2020)
car1_shnn.display_car()