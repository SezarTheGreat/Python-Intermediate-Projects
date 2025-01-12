# Rock Paper Scissors game 
import random

options = ("Rock","Paper","Scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a Choice (Rock,Paper,Scissors): ").capitalize

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print(f"Both players selected {player}. It's a tie!")
    elif player == "rock" and computer == "Scissors":
        print("Player Wins!")
    elif player == "paper" and computer == "rock":
        print("Player Wins!")
    elif player == "scissors" and computer == "paper":
        print("Player Wins!")
    else:
        print("Player Loses!")
    if not input("Do you want to play again(Y/N): ").lower() =='y':
        running = False

print("Thanks for playing :)")