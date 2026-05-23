class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input("""
1. Enter 1 to create PIN
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. Enter 4 to check balance
5. Enter 5 to exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            exit()


    def create_pin(self):
        self.pin = input("Enter your new PIN: ")
        print("PIN created successfully!")
        self.menu()


    def deposit(self):
        if self.pin == "":
            print("Please create a PIN first!")
            self.create_pin()
            self.menu()

        else:
            user_pin = input("Enter your PIN: ")
            if user_pin == self.pin:
                amount = float(input("Enter the amount to deposit: "))
                self.balance += amount
                print(f"Amount deposited successfully! Your new balance is: {self.balance}")
                self.menu()
            else:
                print("Incorrect PIN!")
                self.menu()


    def withdraw(self):
        if self.pin == "":
            print("Please create a PIN first!")
            self.create_pin()
            self.menu()

        else:
            user_pin = input("Enter your PIN: ")
            if user_pin == self.pin:
                amount = float(input("Enter the amount to withdraw: "))
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Amount withdrawn successfully! Your new balance is: {self.balance}")
                    self.menu()

                else:
                    print("Insufficient balance!")
                    self.menu()
            else:
                print("Incorrect PIN!")
                self.menu()

    def check_balance(self):
        if self.pin == "":
            print("Please create a PIN first!")
            self.create_pin()
            self.menu()
        else:
            user_pin = input("Enter your PIN: ")
            if user_pin == self.pin:
                print(f"Your current balance is: {self.balance}")
                self.menu()
            else:
                print("Incorrect PIN!")
                self.menu()




meezan = Atm()