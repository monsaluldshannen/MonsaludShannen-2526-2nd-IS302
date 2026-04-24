class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_product_info(self):
        print(f"Product: {self.__name}")
        print(f"Price: {self.__price}")
        print(f"Quantity: {self.__quantity}")

    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.__quantity = new_quantity

    def update_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price

# Example Usage
product1 = Product("Laptop", 45000, 10)
product1.get_product_info()

product1.update_price(47000)
product1.update_quantity(8)
print("\nAfter update:")
product1.get_product_info()
