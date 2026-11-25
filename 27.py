class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Deposited:", amount, "New Balance:", self.balance)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrew:", amount, "Remaining Balance:", self.balance)
        else:
            print("Insufficient funds")

    def show_balance(self):
        print("Account Holder:", self.owner, "| Balance:", self.balance)

acc = BankAccount("Aditya", 500)
acc.show_balance()
acc.deposit(250)
acc.withdraw(100)
acc.withdraw(1000)

print()

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books = Book.total_books + 1

    def details(self):
        print(self.title, "by", self.author)

b1 = Book("Python Crash Course", "Eric Matthes")
b2 = Book("Automate the Boring Stuff", "Al Sweigart")
b1.details()
b2.details()
print("Total books created:", Book.total_books)
