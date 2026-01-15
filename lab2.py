class BankAccount:
    """Bank Account protected by a pin number."""

    def __init__(self, pin):
        """Initial account balance is 0 and pin is 'pin'."""
        self.pin = pin
        self.balance = 0.0

    def deposit(self, pin, amount):
        """Increment account balance by amount and return new balance."""
        if pin != self.pin:
            return "Pin error"
        self.balance += round(self.balance + amount, 2)
        return self.balance

    def withdraw(self, pin, amount):
        """Decrement account balance by amount and return amount withdrawn."""
        if pin != self.pin:
            return "Pin error"
        if amount > self.balance:
            return "Insufficient balance"
        self.balance = round(self.balance - amount, 2)
        return amount

    def get_balance(self, pin):
        """Return account balance."""
        if pin != self.pin:
            return "Pin error"
        return self.balance

    def change_pin(self, oldpin, newpin):
        """Change pin from oldpin to newpin."""
        if oldpin != self.pin:
            return "Old pin not matched"
        self.pin = newpin
        return "New pin successfully changed"

class SavingsAccount(BankAccount):
    def __init__(self, pin, interest_rate):
        super().__init__(pin)
        self.interest_rate = interest_rate

    def add_interest(self,pin):
        """Calculate interest and add it to balance."""
        if pin != self.pin:
            return "Pin error"
        interest = round(self.balance * self.interest_rate, 2)
        self.balance = round(self.balance + interest, 2)
        return self.balance

class FeeSavingsAccount(SavingsAccount):
    def __init__(self, pin, interest_rate, fee):
        super().__init__(pin, interest_rate)
        self.fee = fee

    def withdraw(self, pin, amount):
        """Decrement account balance by amount and return amount withdrawn."""
        if pin != self.pin:
            return "Pin error"
        total_amount = round(amount + self.fee, 2)
        if total_amount > self.balance:
            return "Insufficient balance"
        self.balance = round(self.balance - total_amount, 2)
        return amount