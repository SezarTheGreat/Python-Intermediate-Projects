#A begineer slot machine program in python

import random
import time

def spin_row():
    symbols = ['🍒','🍉','🍋','⭐','🔔']
    
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print("*************")
    for i in range(3):
        print(f"| {row[i]} | ", end='')
        time.sleep(1)
    print("\n*************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    elif row[0] == row[1] or row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 1.2
        elif row[0] == '🍉':
            return bet * 1.4
        elif row[0] == '🍋':
            return bet * 1.5
        elif row[0] == '🔔':
            return bet * 2
        elif row[0] == '⭐':
            return bet * 3
    else:
        return 0

def main():
    balance = 1000
    print("************************************")
    print("Welcome to Python Slot Machine")
    print("Symbols: 🍒 🍉 🍋 ⭐ 🔔")
    print("************************************")

    while balance > 0:
        print(f"Current Balance Rs.{balance}")
        bet = input("Place your bets: ")

        if not bet.isdigit():
            print("Enter a valid Number: ")
            continue

        bet = int(bet)
        
        if bet > balance:
            print("Insufficient Balance")
            continue

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        time.sleep(2)
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"You won Rs.{payout}")
        else:
            print("You Lost this round.")

        balance += payout
        play_again = input("Do you want to spin again(Y/N): ").upper()
        
        if play_again != 'Y':
            break

    print(f"Game Over! Your final balance is Rs.{balance}")


if __name__ == '__main__':
    main()