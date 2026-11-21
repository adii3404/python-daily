class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        else:
            return "D"

s1 = Student("Aditya", 1, 92)
s2 = Student("Rohan", 2, 78)
s3 = Student("Priya", 3, 85)

s1.display()
print("Grade:", s1.grade())

print()

s2.display()
print("Grade:", s2.grade())

print()

students = [s1, s2, s3]
print("All students:")
for s in students:
    print(s.name, "->", s.marks, "->", s.grade())

print()

class Counter:
    count = 0

    def __init__(self):
        Counter.count = Counter.count + 1

    def get_count(self):
        return Counter.count

c1 = Counter()
c2 = Counter()
c3 = Counter()
print("Objects created:", c3.get_count())
