#Python Banking Program

def show_balance(balance):
    print("*******************")
    print(f"Your balance is Rs.{balance:.2f}")
    print("*******************")

def deposit():
    print("*******************")
    amount = float(input("Enter a amount to be deposited: "))
    print("*******************")

    if amount < 0:
        print("*******************")
        print("Invalid amount. Please enter a positive number.")
        print("*******************")
        return 0
    else:
        return amount

def withdrawal(balance):
    print("*******************")
    amount = float(input("Enter amount ot be withdrawn: "))
    print("*******************")

    if amount > balance:
        print("*******************")
        print("Insufficient Funds.")
        print("*******************")
        return 0
    elif amount > 0:
        print("*******************")
        print("Amount must be greater than zero.")
        print("*******************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("**********************************************")
        print("   Banking Program   ")
        print("**********************************************")
        print("1.Show Balance\n2.Deposit\n3.Withdraw\n4.Exit")
        print("**********************************************")

        choice = input("Enter your choice (1-4):")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdrawal(balance)
        elif choice == '4':
            is_running = False
        else:
            print("*******************")
            print("Not a valid choice.")
            print("*******************")
    print("**********************************************")
    print("Thank You! Have a nice day!")
    print("**********************************************")

if __name__ == '__main__':
    main()