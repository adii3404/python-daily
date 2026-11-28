class Account:
    """Base bank account with encapsulated balance and transactions."""

    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self._balance = initial_balance
        self.history = []
        if initial_balance > 0:
            self.history.append(f"Initial deposit: +{initial_balance:.2f}")

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self._balance += amount
        self.history.append(f"Deposited: +{amount:.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self._balance:
            print(f"Insufficient funds: available {self._balance:.2f}")
            return False
        self._balance -= amount
        self.history.append(f"Withdrew: -{amount:.2f}")
        return True

    def __repr__(self) -> str:
        return f"Account(owner='{self.owner}', balance={self._balance:.2f})"


class SavingsAccount(Account):
    """Savings account subclass with annual interest yield."""

    def __init__(self, owner: str, initial_balance: float = 0.0, interest_rate: float = 0.04):
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self) -> float:
        earned = self._balance * self.interest_rate
        self.deposit(earned)
        print(f"Applied annual interest of {earned:.2f} at {self.interest_rate*100:.1f}%")
        return earned


# Demonstration
acc = Account("Aditya", 5000.0)
acc.deposit(1200.0)
acc.withdraw(800.0)
print(acc)
print("Transaction history:", acc.history)

print()

savings = SavingsAccount("Aditya (Savings)", 10000.0, interest_rate=0.05)
savings.apply_interest()
print(savings)
