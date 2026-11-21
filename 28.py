class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(self.name, "says", self.sound)

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed

    def info(self):
        print("Name:", self.name)
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Meow")
        self.color = color

    def info(self):
        print("Name:", self.name)
        print("Color:", self.color)

d = Dog("Bruno", "Labrador")
d.speak()
d.info()

print()

c = Cat("Luna", "White")
c.speak()
c.info()

print()

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

r = Rectangle(10, 5)
print("Rectangle area:", r.area())

c = Circle(7)
print("Circle area:", c.area())
