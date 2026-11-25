class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(self.brand, self.model, "is starting engine")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display(self):
        print("Car:", self.brand, self.model, "Doors:", self.doors)

class Bike(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc

    def display(self):
        print("Bike:", self.brand, self.model, "Engine CC:", self.cc)

car = Car("Honda", "City", 4)
bike = Bike("Yamaha", "R15", 155)

car.start()
car.display()

print()

bike.start()
bike.display()

print()

class Payment:
    def pay(self, amount):
        print("Processing base payment of", amount)

class UpiPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "via UPI ID")

class CardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "via Credit Card")

methods = [UpiPayment(), CardPayment()]
for m in methods:
    m.pay(1200)
