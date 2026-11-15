class BankAccount:
    # Class Attribute
    bank_name = "BOG"
    total_accounts = 0

    def __init__(self, card_type, owner, balance=0):
        # Instance Attributes
        self.card_type = card_type
        self.owner = owner
        self.__balance = balance

        BankAccount.total_accounts += 1

    # Getter
    @property
    def balance(self):
        return self.__balance

    # Setter
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("ბალანსი არ შეიძლება იყოს უარყოფითი")

        self.__balance = amount

    # Deleter
    @balance.deleter
    def balance(self):
        self.__balance = 0

    # თანხის შეტანა
    def deposit(self, amount):
        if amount <= 0:
            print("თანხა უნდა იყოს დადებითი")
            return

        self.balance += amount
        print(f"ჩაირიცხა {amount} ლარი")
        print(f"მიმდინარე ბალანსი: {self.balance} ლარი")

    # თანხის მოხსნა
    def withdraw(self, amount):
        if amount <= 0:
            print("თანხა უნდა იყოს დადებითი")
            return

        if amount > self.balance:
            print("არასაკმარისი თანხა")
            return

        self.balance -= amount
        print(f"მოხსნილია {amount} ლარი")
        print(f"მიმდინარე ბალანსი: {self.balance} ლარი")

    # Class Method
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    # Static Method
    @staticmethod
    def calculate_tax(amount):
        return amount * 0.18


# SavingsAccount


class SavingsAccount(BankAccount):

    def __init__(self, card_type, owner, balance=0,
                 interest_rate=5, fee=2):

        super().__init__(card_type, owner, balance)

        self.interest_rate = interest_rate
        self.fee = fee

    # პროცენტის დარიცხვა
    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest

        print(f"დარიცხული პროცენტი: {interest} ლარი")
        print(f"ახალი ბალანსი: {self.balance} ლარი")

    # Method Overriding
    def withdraw(self, amount):
        total = amount + self.fee

        if amount <= 0:
            print("თანხა უნდა იყოს დადებითი")
            return

        if total > self.balance:
            print("არასაკმარისი თანხა საკომისიოს ჩათვლით")
            return

        self.balance -= total

        print(f"მოხსნილია: {amount} ლარი")
        print(f"საკომისიო: {self.fee} ლარი")
        print(f"მიმდინარე ბალანსი: {self.balance} ლარი")



# CreditAccount
class CreditAccount(BankAccount):

    def __init__(self, card_type, owner, balance=0,
                 credit_limit=2000):

        super().__init__(card_type, owner, balance)

        self.credit_limit = credit_limit

    # მეთოდის გადატვირთა
    def withdraw(self, amount):
        if amount <= 0:
            print("თანხა უნდა იყოს დადებითი")
            return

        if self.balance - amount < -self.credit_limit:
            print("საკრედიტო ლიმიტი გადაჭარბებულია")
            return

        self.balance -= amount

        print(f"მოხსნილია: {amount} ლარი")
        print(f"მიმდინარე ბალანსი: {self.balance} ლარი")


# აქ ხდება პროგრამის ტესტირება
account1 = BankAccount("Visa", "Giorgi", 1000)

account2 = SavingsAccount(
    "Mastercard", "Nika", 2000, 5, 2
)

account3 = CreditAccount(
    "Visa", "Ana", 500, 2000
)

print("\n--- ჩვეულებრივი ანგარიში ---")
account1.deposit(500)
account1.withdraw(200)

print("\n--- შემნახველი ანგარიში ---")
account2.apply_interest()
account2.withdraw(100)

print("\n--- საკრედიტო ანგარიში ---")
account3.withdraw(1000)

print("\n--- კლასის მეთოდი ---")
BankAccount.change_bank_name("TBC")
print(BankAccount.bank_name)

print("\n--- სტატიკური მეთოდი ---")
print(BankAccount.calculate_tax(1000))

print("\n--- ანგარიშების რაოდენობა ---")
print(BankAccount.total_accounts)

print("\n--- ანგარიშის ინფორმაცია ---")
print(account1.owner)
print(account1.card_type)
print(account1.balance)
