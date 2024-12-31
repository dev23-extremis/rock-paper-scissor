rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

import random

options = ["rock","paper","scissors"]

length_options = len(options)

random_option = options[random.randint(0,length_options-1)]

input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Rock
if input == 0 and random_option == 'rock':
    print("You choose: \n", rock)
    print("Computer choose: \n", rock)
    print("It's draw")

elif input == 1 and random_option == 'rock':
    print("You choose: \n", paper)
    print("Computer choose: \n", rock)
    print("You win!")

elif input == 2 and random_option == 'rock':
    print("You choose: \n", scissors)
    print("Computer choose: \n", rock)
    print("You lose!")

# Paper
elif input == 0 and random_option == 'paper':
    print("You choose: \n", rock)
    print("Computer choose: \n", paper)
    print("You lose!")

elif input == 1 and random_option == 'paper':
    print("You choose: \n", paper)
    print("Computer choose: \n", paper)
    print("It's draw")

elif input == 2 and random_option == 'paper':
    print("You choose: \n", scissors)
    print("Computer choose: \n", paper)
    print("You win!")

# Scissors
elif input == 0 and random_option == 'scissors':
    print("You choose: \n", rock)
    print("Computer choose: \n", scissors)
    print("You win!")

elif input == 1 and random_option == 'scissors':
    print("You choose: \n", paper)
    print("Computer choose: \n", scissors)
    print("You lose!")

elif input == 2 and random_option == 'scissors':
    print("You choose: \n", scissors)
    print("Computer choose: \n", scissors)
    print("It's draw")
