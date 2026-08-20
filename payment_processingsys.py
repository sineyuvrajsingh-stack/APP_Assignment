from abc import ABC, abstractmethod


# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} processed using Credit Card")


# Concrete Strategy 2
class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} processed using Debit Card")


# Concrete Strategy 3
class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} processed using UPI")


# Context Class
class PaymentProcessor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy is None:
            print("Please select a payment mode.")
        else:
            self.strategy.pay(amount)


# Driver Code
processor = PaymentProcessor()

while True:
    print("\n--------- Payment Processing System ---------")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI Payment")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Thank you for using the Payment System!")
        break

    amount = float(input("Enter the amount: "))

    if choice == 1:
        processor.set_strategy(CreditCardPayment())
    elif choice == 2:
        processor.set_strategy(DebitCardPayment())
    elif choice == 3:
        processor.set_strategy(UpiPayment())
    else:
        print("Invalid choice!")
        continue

    processor.process_payment(amount)