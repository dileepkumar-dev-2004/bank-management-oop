class BankingAccount:
    def __init__(self, name, account_number, balance, pin):
        self.name = name
        self.bank = "HDFC Bank"
        self._account_number = account_number
        self.__balance = balance
        self.__pin = pin
        self.__history = []

    def verify_pin(self, enter_pin):
        return self.__pin == enter_pin
    
    def deposit(self, amount):
        if self.__balance > 0:
            self.__balance += amount
            self.__history.append(f"Deposited ${amount}")
            print(f"${amount} credited to your bank account {self._account_number} successfully.")
        else:
            print("Deposit must be positive please enter the valid amount that you want to add to your bank account")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        elif amount>0:
            self.__balance -= amount
            self.__history.append(f"Withdraw ${amount}")
            print(f"${amount} is debited from your account {self._account_number} successfully")
        else:
            print("Withdraw must be postive please enter a valid amount that you want to withdraw from your bank account")
    
    def current_balance(self):
        print(f"The current available balance in the account is {self.__balance} in your bank account {self._account_number}")

    def final_balance(self):
        print(f"The final balance left in your bank account is {self.__balance}")

    def show_history(self):
        print(f"\n -- Transcation History -- /n")
        if not self.__history:
            print("No transcation history found")
        else:
            for i, entry in enumerate(self.__history, 1):
                print(f"{i}. {entry}")

dileep = BankingAccount("Dileep", 5826, 1000, 4532)

attempts = 3
while attempts > 0:
    try:
        user = int(input("Enter your 4 digit pin: "))
    except ValueError:
        print("Invalid input, please input number only.")
        continue

    if dileep.verify_pin(user):
        print("Access granted.")
        break
    else:
        attempts -= 1
        print(f"You have entered the wrong pin so please try again available attempts left {attempts}")
        
if attempts == 0:
    print("Too many attempts account locked.")
    exit

while True:
    print(" --- Welcome to HDFC bank ---")
    print(" -- bank menu -- ")
    print("1. balance")
    print("2. withdraw")
    print("3. deposit")
    print("4. showbalance")
    print("5. exit")

    customer = int(input("Enter a number from (1 - 5): "))
    if customer == 1:
        dileep.current_balance()
    elif customer == 2:
        try:
            amount = float(input("Enter the amouunt that you want to withdraw: "))
            dileep.withdraw(amount)
        except ValueError:
            print("Please enter a valid number: ")
    elif customer == 3:
        try: 
            amount = float(input("Enter the amount that you want to deposit: "))
            dileep.deposit(amount)
        except ValueError:
            print("Please enter a valid number: ")
    elif customer == 4:
        dileep.show_history()
    elif customer == 5:
        dileep.final_balance()
        print("Thankyou for choosing HDFC Bank")
        break
    else:
        print("Invalid choice, please try again")

    
