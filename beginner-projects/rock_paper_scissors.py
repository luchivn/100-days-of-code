import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
bot_choice = random.randint(0,2)

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("invalid input!")

print("Computer chose:")

if bot_choice == 0:
    print(rock)
elif bot_choice == 1:
    print(paper)
else:
    print(scissors)

if user_choice == bot_choice:
    print("Draw")
elif user_choice > bot_choice and user_choice-bot_choice != 2:
    print("You win")
else:
    print("You lose")
