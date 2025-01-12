# Python Dice Roller Program

#unicode characters 

#  print("\u25CF \u250c \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

'┌─────────┐'
'│         │'
'│         │'
'│         │'
'└─────────┘'
# Box art

import random

dice_art = {1:('┌─────────┐',
               '│         │',
               '│    ●    │',
               '│         │',
               '└─────────┘'),
            2:("┌─────────┐",
               "│  ●      │",
               "│         │",
               "│      ●  │",
               "└─────────┘"),
            3:("┌─────────┐",
               "│  ●      │",
               "│    ●    │",
               "│      ●  │",
               "└─────────┘"),
            4: ("┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),
            6: ("┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
print(dice)
#It prints the dice number that is randomly generated form which the dice is later printed.

#This line is written to give the dice a horizontal orientation by the means of printing the first line of all the dice in it on the first line and so on.
print("----------------------------------------")
print("HORIZONTAL")
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end='')
    print()

#This line is written to print the dice in a vertical orientation by the means of printing all the lines of a single dice and afterwards printing the lines of the rest of the dices.
print("----------------------------------------")
print("VERTICAL")
for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)
    
for die in dice:
    total += die 
print(f"Total: {total}")